"""
Minimal validation script for the current MVP data-source plan.

What this script validates:
1. Stock basic information for the three selected stocks
2. Stock daily history for the three selected stocks
3. Index market snapshot availability
4. Index history lookup for SSE Composite and CSI 300

Run:
    python src/data/validate_efinance.py
"""

from __future__ import annotations

import sys
from typing import Iterable

import efinance as ef


SELECTED_STOCKS = {
    "601318": "Ping An Insurance",
    "600900": "China Yangtze Power",
    "601899": "Zijin Mining",
}

TRACKED_INDICES = {
    "000001": ["上证指数", "上证综指"],
    "000300": ["沪深300", "CSI 300"],
}

STOCK_HISTORY_REQUIRED_COLUMNS = {"日期", "开盘", "收盘", "最高", "最低"}
INDEX_SNAPSHOT_HINT_COLUMNS = {"代码", "名称"}


def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def summarize_frame(df, required_columns: Iterable[str] | None = None) -> bool:
    if df is None:
        print("Result: None")
        return False
    if getattr(df, "empty", True):
        print("Result: empty DataFrame")
        return False

    columns = list(df.columns)
    print(f"Rows: {len(df)}")
    print(f"Columns: {columns}")

    if required_columns is not None:
        missing = sorted(set(required_columns) - set(columns))
        if missing:
            print(f"Missing required columns: {missing}")
            return False

    print(df.head(3).to_string(index=False))
    return True


def validate_stock_base_info() -> bool:
    print_header("1. Validate stock basic information")
    ok = True
    for code, name in SELECTED_STOCKS.items():
        print(f"\n[Stock Base Info] {code} {name}")
        try:
            result = ef.stock.get_base_info(code)
            if isinstance(result, dict):
                print(f"Keys: {sorted(result.keys())}")
                print(result)
                has_core_keys = any(k in result for k in ("股票代码", "股票名称", "总市值"))
                ok = ok and has_core_keys
                if not has_core_keys:
                    print("Missing expected core fields in dict result.")
            else:
                frame_ok = summarize_frame(result)
                ok = ok and frame_ok
        except Exception as exc:
            print(f"Error: {exc}")
            ok = False
    return ok


def validate_stock_history() -> bool:
    print_header("2. Validate stock daily history")
    ok = True
    for code, name in SELECTED_STOCKS.items():
        print(f"\n[Stock History] {code} {name}")
        try:
            df = ef.stock.get_quote_history(
                code,
                beg="20180101",
                end="20260331",
                klt=101,
                fqt=1,
            )
            frame_ok = summarize_frame(df, STOCK_HISTORY_REQUIRED_COLUMNS)
            ok = ok and frame_ok
        except Exception as exc:
            print(f"Error: {exc}")
            ok = False
    return ok


def validate_index_snapshot() -> bool:
    print_header("3. Validate index market snapshot")
    try:
        df = ef.stock.get_realtime_quotes("沪深系列指数")
        return summarize_frame(df, INDEX_SNAPSHOT_HINT_COLUMNS)
    except Exception as exc:
        print(f"Error: {exc}")
        return False


def try_index_history(identifier: str):
    return ef.stock.get_quote_history(
        identifier,
        beg="20180101",
        end="20260331",
        klt=101,
        fqt=1,
    )


def validate_index_history() -> bool:
    print_header("4. Validate index history")
    ok = True
    for code, aliases in TRACKED_INDICES.items():
        print(f"\n[Index History] {code} aliases={aliases}")
        success = False
        identifiers = [code, *aliases]
        for identifier in identifiers:
            print(f"Trying identifier: {identifier}")
            try:
                df = try_index_history(identifier)
                frame_ok = summarize_frame(df, STOCK_HISTORY_REQUIRED_COLUMNS)
                if frame_ok:
                    print(f"Success with identifier: {identifier}")
                    success = True
                    break
            except Exception as exc:
                print(f"Error with {identifier}: {exc}")
        if not success:
            print(f"Failed to fetch usable history for index {code}")
            ok = False
    return ok


def main() -> int:
    print_header("efinance MVP validation")
    print("Testing selected stocks, tracked indices, and required field availability.")

    checks = {
        "stock_base_info": validate_stock_base_info(),
        "stock_history": validate_stock_history(),
        "index_snapshot": validate_index_snapshot(),
        "index_history": validate_index_history(),
    }

    print_header("5. Summary")
    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")

    if all(checks.values()):
        print("\nOverall result: PASS")
        return 0

    print("\nOverall result: FAIL")
    print("If stock tests pass but index_history fails, keep efinance for stocks and add a fallback plan for index history.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

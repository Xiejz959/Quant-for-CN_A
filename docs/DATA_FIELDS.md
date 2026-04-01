# Data Field Specification

[中文](./DATA_FIELDS.zh-CN.md)

## Scope

This field list is for the first implementation stage only.

Tracked indices:

- SSE Composite Index
- CSI 300 Index

Selected stocks:

- `601318` Ping An Insurance
- `600900` China Yangtze Power
- `601899` Zijin Mining

Primary source:

- `efinance`

## Design Rule

Every field below is classified into one of three groups:

- `Required`: must exist for the first MVP
- `Preferred`: useful and should be collected if available
- `Deferred`: not needed in the first MVP

## 1. Index Metadata

Purpose:

- identify tracked indices
- label visualizations and analysis outputs

### Required

- `index_code`: unique code for the index
- `index_name`: readable index name
- `market`: exchange or market tag if available

### Preferred

- `publisher`: index provider if available
- `base_date`: index base date if available

### Deferred

- `constituent_count`
- `index_category`

## 2. Index Daily Price History

Purpose:

- long-term trend charts
- return window calculation
- moving average calculation
- benchmark comparison against stocks

### Required

- `trade_date`: trading date
- `index_code`: join key to index metadata
- `open`
- `high`
- `low`
- `close`

### Preferred

- `volume`
- `amount`
- `change_pct`
- `change_amount`

### Deferred

- `turnover_rate`
- `amplitude`
- intraday fields

## 3. Stock Metadata

Purpose:

- identify the selected stocks
- label charts
- support future filtering and reporting

### Required

- `stock_code`: unique stock code
- `stock_name`: readable stock name
- `market`: exchange tag such as SSE or SZSE if available

### Preferred

- `listing_date`
- `total_market_value`
- `float_market_value`
- `pe_ratio`
- `pb_ratio`

### Deferred

- `industry`
- `sector`
- `main_business`
- detailed shareholder data

## 4. Stock Daily Price History

Purpose:

- long-term stock trend charts
- moving average calculation
- relative strength calculation versus indices
- volume-supported interpretation

### Required

- `trade_date`
- `stock_code`
- `open`
- `high`
- `low`
- `close`

### Preferred

- `volume`
- `amount`
- `change_pct`
- `change_amount`
- `turnover_rate`
- `adjustment_flag` or a clear statement of the adjustment mode used

### Deferred

- intraday fields
- order-book style data
- capital flow details

## 5. Derived Metrics For The First MVP

These are not raw fields from the source, but they define why the raw fields are needed.

### Index metrics

- `return_20d`
- `return_60d`
- `return_120d`
- `ma_20`
- `ma_60`
- `ma_120`
- `ma_250`
- `trend_label`

### Stock metrics

- `return_20d`
- `return_60d`
- `return_120d`
- `ma_20`
- `ma_60`
- `ma_120`
- `ma_250`
- `relative_strength_vs_sse`
- `relative_strength_vs_csi300`
- `trend_label`

## 6. Validation Checklist For efinance

Before implementation, verify the following:

1. The two tracked indices can be queried consistently.
2. The three selected stocks can be queried consistently.
3. Date fields are returned in a format that can be normalized cleanly.
4. Price fields are numeric and stable enough for rolling metrics.
5. The same adjustment mode can be used consistently for all selected stocks.

## 7. Suggested First Database Tables

- `indices`
- `index_prices`
- `stocks`
- `daily_prices`

That is enough for the current MVP. Sector-related tables can be added later without changing the core structure.

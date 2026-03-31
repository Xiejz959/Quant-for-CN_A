# Quant for CN_A

[中文](./README.zh-CN.md)

An A-share visualization-first quantitative analysis project for individual investors.

## Current Stage

This project is currently in the planning and MVP definition stage.

The first goal is not to build a local website immediately. We will first complete:

1. Public data collection for selected indices and stocks
2. Long-term index trend analysis
3. Long-term stock trend analysis
4. Reproducible visualizations and analysis outputs

After the data and visualization pipeline is stable, we can build a localhost web app and later deploy it to Azure.

## Core MVP Direction

The MVP focuses on index and stock analysis rather than short-term prediction:

- A-share only
- Focus on `SSE Composite Index` and `CSI 300 Index`
- Long-term trend analysis for selected representative stocks
- Explainable trend judgement instead of short-horizon price prediction
- Sector and industry analysis deferred to a later phase

## Data Source Decision

The current primary public data source is `efinance`.

Why this is the current choice:

- Python-friendly and suitable for a student project
- Supports stock history queries through `ef.stock.get_quote_history()`
- Supports stock basic information through `ef.stock.get_base_info()`
- Supports index market snapshots through `ef.stock.get_realtime_quotes()`
- README explicitly mentions `TickFlow` as an alternative when rate limits or network errors occur

Current backup plan:

- `TickFlow` as a fallback source if `efinance` becomes unstable

## Initial Observation Scope

Tracked indices for the first MVP:

- SSE Composite Index
- CSI 300 Index

Suggested first stock candidates:

- `600519` Guizhou Moutai
- `600036` China Merchants Bank
- `601318` Ping An Insurance
- `600900` China Yangtze Power
- `601899` Zijin Mining

These are intended as representative large-cap observation targets for the first development stage, not investment advice.

## Documents

- `docs/MVP.md`: product and scope definition for the first version
- `docs/ROADMAP.md`: staged development plan
- `docs/ARCHITECTURE.md`: recommended technical design for the visualization-first phase
- `docs/TASKS_PHASE1.md`: concrete implementation checklist for the first phase

## Recommended First Build Path

1. Finalize the required fields for the two indices and selected stocks
2. Verify `efinance` coverage for index history, stock history, and stock metadata
3. Build the local database and update scripts
4. Implement long-term trend metrics
5. Produce notebook or script-based visualizations
6. Build a local web interface later

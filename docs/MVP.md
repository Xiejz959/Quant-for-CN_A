# MVP Definition

[中文](./MVP.zh-CN.md)

## Project Goal

Build a Python-based A-share quantitative visualization analysis system for personal use.

The first version should help answer questions like:

- How are the `SSE Composite Index` and `CSI 300 Index` behaving over medium and long horizons?
- How do selected representative stocks compare against those benchmark indices?
- Can long-term trend states be summarized in a simple and explainable way?

## What The MVP Must Do

### 1. Data Collection

The system must be able to collect and locally store:

- selected A-share index metadata
- daily price history for the tracked indices
- stock basic information for selected observation targets
- daily stock price history for selected observation targets

### 2. Index Analysis

The system must provide:

- long-term index price trend charts
- moving average structure for tracked indices
- return windows such as 20, 60, and 120 trading days
- simple trend labels for the indices

### 3. Stock Long-Term Trend Analysis

The system must provide:

- long-term stock price trend charts
- moving average system such as MA20, MA60, MA120, MA250
- volume trend support
- relative strength versus a benchmark index
- trend labels such as `uptrend`, `range`, `weakening`

### 4. Visualization

The MVP should support visualization before any web app is built.

Acceptable first-stage forms:

- Jupyter notebooks
- Python scripts generating charts
- local HTML chart exports
- static image outputs for reports

## Chosen Public Data Source

The current primary source is `efinance`, with `TickFlow` reserved as a fallback.

The current choice is based on the documented availability of:

- stock history queries via `ef.stock.get_quote_history()`
- stock basic information via `ef.stock.get_base_info()`
- index-related market snapshots via `ef.stock.get_realtime_quotes()`

## What The MVP Will Not Do

The first version should explicitly avoid:

- sector and industry analysis
- short-term price prediction for the next few days
- high-frequency or intraday analysis
- automated trading
- full backtesting engine
- user login or multi-user support
- news sentiment analysis
- complex machine learning models

## Initial Observation Targets

Tracked indices:

- SSE Composite Index
- CSI 300 Index

Suggested first stock candidates:

- `600519` Guizhou Moutai
- `600036` China Merchants Bank
- `601318` Ping An Insurance
- `600900` China Yangtze Power
- `601899` Zijin Mining

## Output Style For The MVP

The first working version should produce:

1. At least one long-term trend chart for each tracked index
2. At least one long-term trend chart for each selected stock
3. A simple explainable trend summary for the indices and stocks
4. A reproducible notebook or script that regenerates the same outputs

## Success Criteria

The MVP is successful if you can:

1. Update market data locally with one command or one script
2. Recompute index and stock analysis consistently
3. Generate visual outputs that clearly show long-term trend structure
4. Explain why an index or stock is labeled strong, neutral, or weak

## Recommended Data-First Philosophy

Do not build the website first.

Instead, follow this order:

1. data acquisition
2. data storage
3. metric calculation
4. visualization outputs
5. local web interface
6. Azure deployment

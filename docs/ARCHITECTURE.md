# Recommended Architecture

[中文](./ARCHITECTURE.zh-CN.md)

## Design Principle

The first implementation should be Python-first and visualization-first.

That means:

- analysis quality before UI polish
- stable local data before deployment
- explainable rules before complex modeling

## Suggested Stack

- Language: Python
- Data handling: pandas, numpy
- Storage: SQLite
- Visualization: plotly, matplotlib, or pyecharts
- Notebook/prototyping: Jupyter
- Optional local app later: Streamlit

## Logical Modules

### 1. Data Ingestion

Responsibilities:

- fetch stock metadata
- fetch daily stock prices
- fetch tracked index data

Suggested output:

- normalized raw tables in SQLite

### 2. Data Storage

Responsibilities:

- define table schema
- enforce primary keys
- keep update history consistent

Suggested core tables:

- `stocks`
- `indices`
- `daily_prices`
- `index_prices`

### 3. Analysis Engine

Responsibilities:

- compute index return windows
- compute index moving averages
- compute relative strength
- compute moving averages
- assign trend labels

Suggested outputs:

- analysis tables
- cached intermediate metrics

### 4. Visualization Layer

Responsibilities:

- render index trend charts
- render stock trend charts
- export readable outputs

Possible forms:

- notebook charts
- saved html chart files
- png exports

## Recommended Project Structure

```text
Quant for CN_A/
├── README.md
├── docs/
│   ├── MVP.md
│   ├── ROADMAP.md
│   ├── ARCHITECTURE.md
│   └── TASKS_PHASE1.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
├── src/
│   ├── data/
│   ├── analysis/
│   ├── visualization/
│   └── utils/
├── outputs/
│   ├── charts/
│   └── reports/
└── tests/
```

## Extension Path

Once the first version is stable, the architecture can extend toward:

- sector and industry analysis
- backtesting
- watchlists
- alerts
- cloud deployment
- more advanced factor models

The key is to keep data, analysis, and visualization separated from the start.

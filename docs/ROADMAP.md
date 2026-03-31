# Development Roadmap

[中文](./ROADMAP.zh-CN.md)

## Phase 0: Scope Freeze

Goal:
Lock the project boundary and prevent scope creep.

Deliverables:

- Clear MVP definition
- First version feature list
- Explicit non-goals
- Technical direction centered on Python

Exit condition:
You can describe the project in one sentence and know what not to build yet.

## Phase 1: Data Source Research

Goal:
Choose public data sources that support A-share index and stock trend analysis.

Main questions:

- Which source provides A-share daily prices?
- Which source provides index data?
- Which source provides stock basic information?
- Which source is stable enough for a student project?

Deliverables:

- Data source comparison note
- Final source selection
- Required field list

Exit condition:
You know exactly where each dataset comes from.

## Phase 2: Local Data Pipeline

Goal:
Build a repeatable local data ingestion workflow.

Deliverables:

- SQLite database schema
- Data download scripts
- Update flow for stock and index data
- Data quality checks for missing values and duplicate rows

Exit condition:
You can refresh the core datasets locally without manual edits.

## Phase 3: Analysis Engine

Goal:
Turn raw market data into useful index and stock trend signals.

Deliverables:

- Index return window logic
- Index moving average structure
- Stock moving average and relative strength metrics
- Rule-based trend labels

Exit condition:
You can compute stable analysis tables from local stored data.

## Phase 4: Visualization Layer

Goal:
Make the analysis visible and interpretable before building a website.

Deliverables:

- Index trend charts
- Stock long-term trend charts
- Simple report notebook or export script

Exit condition:
You can inspect results visually without manually digging through raw tables.

## Phase 5: Local App Layer

Goal:
Wrap the data and charts into a localhost app only after the analysis is stable.

Recommended first option:

- Streamlit

Future option:

- FastAPI plus a dedicated frontend

Exit condition:
You already trust the data and visuals, and only need a better interface.

## Phase 6: Azure Deployment

Goal:
Deploy the mature local app to the cloud.

Deliverables:

- Deployment-ready project structure
- Environment configuration
- Cloud database strategy if needed
- Azure deployment workflow

Exit condition:
The project can run outside your machine with predictable setup steps.

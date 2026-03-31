# Phase 1 Task Breakdown

[中文](./TASKS_PHASE1.zh-CN.md)

## Immediate Goal

Finish the data and visualization MVP for indices and selected stocks before building any website.

## Week 1: Project Setup And Data Source Decision

Tasks:

- create the base folder structure
- decide the primary public data source
- list required fields for tracked indices and selected stocks
- write down update frequency assumptions

Completion signal:

- you know what to download, from where, and how often

## Week 2: Database And Ingestion

Tasks:

- create SQLite schema
- build stock metadata ingestion
- build daily stock price ingestion
- build index price ingestion

Completion signal:

- you can populate local storage with core market data

## Week 3: Core Analysis

Tasks:

- compute index returns over multiple windows
- compute index moving average structure
- compute stock moving averages
- compute stock relative strength
- define explainable trend labels

Completion signal:

- you have analysis tables that are stable and interpretable

## Week 4: Visualization Outputs

Tasks:

- generate index trend charts
- generate stock long-term trend charts
- export one reusable notebook or report script

Completion signal:

- you can inspect sector and stock trends visually from local outputs

## Minimum Deliverable Checklist

The first concrete MVP should include:

- one command or script to refresh data
- one SQLite database file
- one analysis script producing index and stock trend outputs
- one visualization script or notebook
- one example output for an index and one for a stock

## Suggested First Implementation Order

1. Index metadata and stock metadata
2. Index and stock daily price history
3. Index trend calculation
4. Stock trend calculation
5. Visual outputs

## Suggested Early Metrics

Use simple and interpretable metrics first:

- 5-day return
- 20-day return
- 60-day return
- 120-day return
- moving average slope
- price above or below long moving average
- relative strength versus SSE Composite or CSI 300

## Important Rules

- prioritize stable data pipeline over elegant UI
- avoid complex prediction before descriptive analysis is trustworthy
- save intermediate outputs so results are reproducible
- keep analysis scripts independent from presentation logic

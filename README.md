# Ohio Crime Data ETL

## Overview
An ETL pipeline that processes Ohio NIBRS arrestee data using Python and Polars, then loads the transformed data into Google BigQuery for analysis.

## Technologies
- Python
- Polars
- Parquet
- Google BigQuery
- uv

## Pipeline
1. **Extract:** Read the raw CSV dataset.
2. **Transform:** Convert arrest dates and create year and month columns.
3. **Validate:** Check missing values, duplicates, dates, and data types.
4. **Store:** Save the processed data as compressed Parquet.
5. **Load:** Upload the data to BigQuery for SQL analysis.

## Dataset
- Source file: `NIBRS_ARRESTEE_GROUPB.csv`
- Records processed: 70,316
- Original columns: 15
- Processed columns: 17

## BigQuery
- Dataset: `ohio_crime`
- Table: `arrestees`
- Location: EU

## Run the Pipeline

```bash
uv sync
uv run python -m ohio_crime_data_etl.transform_data
uv run python -m ohio_crime_data_etl.verify_data
uv run python -m ohio_crime_data_etl.quality_checks
uv run python -m ohio_crime_data_etl.load_to_bigquery
```

Run these commands from the project root. Keep the raw CSV in `data/raw/` before running the pipeline.

## Purpose
This project demonstrates data ingestion, transformation, data-quality validation, columnar storage, and cloud data warehousing.
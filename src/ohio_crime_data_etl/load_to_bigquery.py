from pathlib import Path
from google.cloud import bigquery


PROJECT_ID = "ohio-crime-data-etl"
DATASET_ID = "ohio_crime"
TABLE_ID = "arrestees"

PARQUET_PATH = Path("data/processed/arrestees.parquet")


if not PARQUET_PATH.exists():
    raise FileNotFoundError(
        f"Parquet file not found: {PARQUET_PATH}"
    )

client = bigquery.Client(project=PROJECT_ID)


table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"


job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)

with PARQUET_PATH.open("rb") as parquet_file:
    job = client.load_table_from_file(
        parquet_file,
        table_ref,
        job_config=job_config,
    )

job.result()


table = client.get_table(table_ref)

print("BIGQUERY LOAD COMPLETE")
print(f"Table: {table.project}.{table.dataset_id}.{table.table_id}")
print(f"Rows loaded: {table.num_rows}")
print(f"Columns: {len(table.schema)}")
print(f"Location: {table.location}")

import polars as pl
from pathlib import Path


input_path = Path("data/raw/NIBRS_ARRESTEE_GROUPB.csv")
output_path = Path("data/processed/arrestees.parquet")


df = pl.read_csv(
    input_path,
    infer_schema_length=10000
)

print("EXTRACT")
print(f"Rows loaded: {df.height}")
print(f"Columns loaded: {df.width}")


df = df.with_columns(
    pl.col("arrest_date").str.to_date(
        format="%Y-%m-%d",
        strict=False
    )
)


df = df.with_columns(
    pl.col("arrest_date").dt.year().alias("arrest_year"),
    pl.col("arrest_date").dt.month().alias("arrest_month")
)

print("\nTRANSFORM")
print("Converted arrest_date to Date")
print("Added arrest_year and arrest_month")


duplicate_count = df.is_duplicated().sum()

invalid_dates = df.filter(
    pl.col("arrest_date").is_null()
).height

print("\nVALIDATION")
print(f"Duplicate rows: {duplicate_count}")
print(f"Missing or invalid dates: {invalid_dates}")

if duplicate_count > 0:
    raise ValueError(
        "Duplicate rows detected. Investigate before loading."
    )

if invalid_dates > 0:
    raise ValueError(
        "Missing or invalid arrest dates detected."
    )


output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.write_parquet(
    output_path,
    compression="zstd"
)

print("\nLOAD")
print(f"Rows written: {df.height}")
print(f"Columns written: {df.width}")
print(f"Output file: {output_path}")
print("ETL pipeline completed successfully.")

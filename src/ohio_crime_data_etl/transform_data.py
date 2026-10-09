import polars as pl

input_path = "data/raw/NIBRS_ARRESTEE_GROUPB.csv"
output_path = "data/processed/arrestees.parquet"

df = pl.read_csv(input_path , infer_schema_length= 10000)

print("ORIGINAL DATA")
print(f"Rows: {df.height}")
print(f"Columns: {df.width}")

df = df.with_columns(
    pl.col('arrest_date').str.to_date(
        format ="%Y-%m-%d" ,
        strict =False
    )
)

duplicate_count = df.is_duplicated().sum()
print(f"Duplicate rows: {duplicate_count}")

df.write_parquet(output_path, compression="zstd")

print("TRANSFORMATION COMPLETE")
print(f"Rows: {df.height}")
print(f"Columns: {df.width}")
print(f"Saved to: {output_path}")

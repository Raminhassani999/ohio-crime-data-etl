import polars as pl 
from pathlib import Path
path = Path("data/processed/arrestees.parquet")

df = pl.read_parquet(path)

print("PARQUET VERIFICATION")
print(f"File exists: {path.exists()}")
print(f"File size: {path.stat().st_size / 1024:.2f} KB")
print(f"Rows: {df.height}")
print(f"Columns: {df.width}")

print("\nDATA TYPES")
print(df.schema)

print("\nFIRST FIVE ROWS")
print(df.head())
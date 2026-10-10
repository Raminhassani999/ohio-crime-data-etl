import polars as pl

file_path = "data/processed/arrestees.parquet"

df = pl.read_parquet(file_path)

print("DATA QUALITY REPORT")

print('MISSING VALUES')
print(df.null_count())

print('DUPLICATED VALUES')
print(df.is_duplicated().sum())

print("\n3. INVALID OR MISSING ARREST DATES")

print(df.filter(pl.col("arrest_date").is_null()).height)

print("\n4. AGE VALUES OUTSIDE 0-120")
print(
    df.filter(
        pl.col("age_num").is_not_null()
        & (
            (pl.col("age_num") < 0)
            | (pl.col("age_num") > 120)
        )
    ).height
)

print("ARREST DATA RANGE")
print(df['arrest_date'].min())
print(df['arrest_date'].max())

print("\n6. SEX CODES")
print(df["sex_code"].value_counts().sort("sex_code"))

print("\n7. RESIDENT CODES")
print(
    df["resident_code"]
    .value_counts()
    .sort("resident_code")
)

print("\nQUALITY CHECKS COMPLETE")
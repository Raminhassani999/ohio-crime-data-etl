import polars as pl

File_path = "data/raw/NIBRS_ARRESTEE_GROUPB.csv"

df = pl.read_csv(File_path , infer_schema_length=10000)

print('FIRST FIVE ROWS')
print(df.head())

print('THE NUMBER OF ROWS AND COLUMNS')
print(df.height)
print(df.width)

print('COLUMN NAMES')
print(df.columns)

print('DATA TYPES')
print(df.schema)

print('MISSING VALUES')
print(df.null_count())

print('BASIC STATISTICS')
print(df.describe())
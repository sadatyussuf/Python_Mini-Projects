import pandas as pd
import pathlib as path

parent_path = path.Path(__file__).parent
my_path = parent_path.joinpath('data')


all_csv_files = list(my_path.glob('*.csv'))

df_read_files = (pd.read_csv(f, sep=',') for f in all_csv_files)

df_merged = (pd.concat(df_read_files, ignore_index=True))

df_merged.to_csv(my_path.joinpath('merged.csv'), index=False)
# print(df_merged)

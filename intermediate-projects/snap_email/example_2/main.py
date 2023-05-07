import pandas as pd
import pathlib

TRAIN_DATASET = pathlib.Path(__file__).parent / "training.csv"
TEST_DATASET = pathlib.Path(__file__).parent / "test.csv"

df_train = pd.read_csv(TRAIN_DATASET)
df_test = pd.read_csv(TEST_DATASET)

print(df_train.describe(include="all"))

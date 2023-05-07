import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
import pathlib

DATA_FILE = pathlib.Path(__file__).parent / "spam.csv"

spam = pd.read_csv(DATA_FILE)

z = spam["v2"]  # Sample Messages from the spam dataset
y = spam["v1"]  # Sample Labels from the spam dataset

z_train, z_test, y_train, y_test = train_test_split(z, y, test_size=0.2)


cv = CountVectorizer()
features = cv.fit_transform(z_train)

model = svm.SVC()
model.fit(features, y_train)

features_test = cv.transform(z_test)
print(model.score(features_test, y_test))

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataList = [i for i in range(12,42)]


np.random.seed(33)

normal_data_a = np.random.normal(size = 500, loc = 100, scale = 10)
normal_data_b = np.random.normal(size = 700, loc = 75, scale = 5)

df_normal_a = pd.DataFrame(data = normal_data_a, columns=['score']).assign(group = 'Group A')
df_normal_b = pd.DataFrame(data = normal_data_b, columns=['score']).assign(group = 'Group B')

score_data = pd.concat([df_normal_a, df_normal_b]).drop_duplicates().reset_index(drop=True)

def createHistogram(score_data):
    # print(score_data)

    sns.set()
    sns.histplot(data=score_data,x='score')
    # sns.distplot(dataList)
    plt.show()

createHistogram(score_data)

















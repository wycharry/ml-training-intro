import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# We use display so that we can do multiple nice renderings of dataframes
# in Jupyter
from IPython.display import display

# The file has no headers naming the columns, so we pass header=None
# and provide the column names explicitly in "names"
data = pd.read_csv(
    "adult.data", header=None, index_col=False,
    names=['age', 'workclass', 'fnlwgt', 'education', 'education-num',
           'marital-status', 'occupation', 'relationship', 'race', 'gender',
           'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
           'income'])
# this column is somewhat meaningless in this context
data = data.drop("fnlwgt", axis=1)
display(data.head())

income = data.income
data_features = data.drop("income", axis=1)

display(data_features.head())

data_one_hot = pd.get_dummies(data_features)

X_train, X_test, y_train, y_test = train_test_split(data_one_hot, income)

scaler = MinMaxScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)

print(X_train.shape)

print(y_train.value_counts())

continuous = data.columns[data.dtypes == "int64"]
colors = (y_train.values == " <=50K").astype(np.int)
pd.tools.plotting.scatter_matrix(X_train[continuous], c=plt.cm.tab10(colors),
                                 alpha=.2, figsize=(10, 10));

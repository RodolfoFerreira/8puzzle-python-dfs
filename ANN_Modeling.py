#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# %%
df = pd.read_csv("./data/water_potability.csv")
# %%
df.info()
# %%
df_ = df.dropna()
df_
# %%
df_.describe()
# %%
sns.displot(df,x="Potability")
# %%
df_.info()
# %%
X = df_.drop("Potability", axis = 1).values
y = df_.loc[:, "Potability"].values
# %%
scaler = StandardScaler()
Xt = scaler.fit_transform(X)
# %%
Xt
# %%
nnclf = MLPClassifier(hidden_layer_sizes=(25,), 
                        solver="adam", 
                        learning_rate_init=0.01,
                        max_iter=500, 
                        random_state=51)
# %%
# Faz o treino da rede usando validação cruzada
accs = cross_val_score(nnclf, Xt, y, cv=100, scoring='accuracy')
# %%
accs.mean()
# %%
accs.std()
# %%
pipe = Pipeline(steps=[("scaler", StandardScaler()),
                       ("model", MLPClassifier((25,), random_state=51))])
# %%
# Usa o X total ao inves de X de treino, porque o pipe fará
# o scaler, diferente do que fizemos anteriormente com o fit
# transform
accsp = cross_val_score(pipe, X, y, cv=100, scoring='accuracy')
# %%
accsp.mean()
# %%
accsp.std()
# %%

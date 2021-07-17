#%%
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, plot_confusion_matrix
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#%%
df = pd.read_csv("./data/heart.csv")

#%%
df.head()

#%%
df.info()

#%%
sns.displot(df, x = "output")

#%%
sns.displot(df, x= "output", hue = "sex", kind="kde")

#%%
sns.displot(df, x= "output", hue = "output")

#%%
sns.displot(df, x= "age", hue = "output", kind="kde")

#%%
x = df.drop("output", axis = 1).values
y = df.loc[:, "output"].values

#%%
x.shape

#%%
y.shape

#%%
xtr, xts, ytr, yts = train_test_split(x, y, test_size=.3, shuffle=True, stratify=y, random_state=51)

#%%
dtclf = DecisionTreeClassifier(criterion="entropy", random_state=51, max_depth=3)

#%%
dtclf.fit(xtr, ytr)

#%%
ypr = dtclf.predict(xts)

#%%
accuracy_score(yts, ypr)

#%%
dps = np.arange(3, 20)
accs = np.zeros(len(dps))
for i, depth in enumerate(dps):
    dtclf = DecisionTreeClassifier(criterion="entropy", random_state=51, max_depth=depth)
    dtclf.fit(xtr, ytr)
    ypr = dtclf.predict(xts)
    accs[i] = accuracy_score(yts, ypr)
    print(f"Max Depth: {depth}. Acc: {accs[i]}")

#%%
confusion_matrix(yts, ypr)

#%%
cmd = plot_confusion_matrix(dtclf, xts, yts)
cmd.ax_.set_xticklabels(["No Risk", "Risk"])
cmd.ax_.set_yticklabels(["No Risk", "Risk"])

#%%
print(classification_report(yts, ypr, target_names=["No Risk", "Risk"]))

#%%
dt_1 = DecisionTreeClassifier(criterion="entropy", random_state=51, max_depth=5)
score = cross_val_score(dt_1, x, y, cv=10)

#%%
print(f"Mean Score: {score.mean()} ({score.std()})")
#%%
plt.plot(score)

# %%

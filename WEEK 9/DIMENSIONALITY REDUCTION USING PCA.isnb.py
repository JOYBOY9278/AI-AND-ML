import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("y:\AI and ML\Datasets\iris.csv")
data

y=data.pop("species")
print(data.head())
data.describe()

from sklearn.preprocessing import StandardScaler
Scaler=StandardScaler()
X=data.copy()
X=Scaler.fit_transform(X)
X[:5,:5]

from sklearn.decomposition import PCA
pca=PCA(random_state=42)
pca.fit(X)
pca.components_
pca.explained_variance_ratio_
plt.bar(range(1,len(pca.explained_variance_ratio_)+1),pca.explained_variance_ratio_)
pc2=PCA(n_components=2,random_state=42)
newdata=pc2.fit_transform(X)
newdata.shape


df=pd.DataFrame(newdata,columns=["PC1","PC2"])
df_final=pd.concat([df,y],axis=1)
print(df_final.head())


import seaborn as sns
sns.pairplot(data=df_final,x_vars=["PC1"],y_vars=["PC2"],hue='species',height=5)
plt.show()
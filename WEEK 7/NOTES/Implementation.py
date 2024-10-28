from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
X,y =make_regression (n_features=4,n_informative=2,random_state=0,shuffle=False)
rfr=RandomForestRegressor(max_depth=3)
rfr.fit(X,y)
print(rfr.predict([[0,1,0,1,]]))

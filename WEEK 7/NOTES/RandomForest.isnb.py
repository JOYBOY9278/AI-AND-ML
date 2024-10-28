from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn import linear_model
import numpy as np

# Generate synthetic data
X, y = make_regression(n_features=4, n_informative=2, random_state=0, shuffle=False)
rfr = RandomForestRegressor(max_depth=3)
rfr.fit(X, y)
print(rfr.predict([[0, 1, 0, 1]]))

# Define rng before using it
rng = np.random.RandomState(1)

# Generate data for SVR
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# Fit regression model
lassoReg = linear_model.Lasso(alpha=0.1)
lassoReg.fit(X, y)

# Predict
X_test = np.arange(0.0, 5.0, 1)[:, np.newaxis]  
prediction = lassoReg.predict(X_test)
print(prediction)



import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
import numpy as np
from sklearn import linear_model


data_set = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv'

df = pd.read_csv(data_set)
print(df.columns)
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
print(cdf.head())

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]
print(len(msk))

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='red')
plt.xlabel('ENGINE SIZE')
plt.ylabel('Emission')
plt.show()


regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)

print(regr.coef_)
print(regr.intercept_)

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
plt.xlabel('Engine Size')
plt.ylabel('Emissions')
plt.show()





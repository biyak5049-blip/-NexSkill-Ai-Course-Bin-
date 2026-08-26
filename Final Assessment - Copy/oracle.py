import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Final Assessment/oracle.csv')

print(df.head())

print("df.shape:         " , df.shape)

df.plot.scatter(x='High', y='Low', title='Scatter Plot of High and Low percentages');
plt.show()
plt

df['Date']= pd.to_datetime(df['Date'])
df['year']= df['Date'].dt.year
df['Month']= df['Date'].dt.month
df['Day']= df['Date'].dt.day
print("df.corr():        " , df.corr())



print("df.describe():                    " , df.describe())


print(" df['Low'] :     " , df['Low'])
print("  df['High']   :    ", df['High']   )

y = df['Low'].values.reshape(-1, 1)
X = df['High'].values.reshape(-1, 1)
  


print("y :  " , y)
print("X :   " , X)


print(df['High'].values) 
print(df['High'].values.shape) 

print(X.shape)
print(X)      


SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)


print(X_train) 
print(y_train)


#Training a Linear Regression Model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()



regressor.fit(X_train, y_train)

print(regressor.intercept_)


print(regressor.coef_)

def calc(slope, intercept, High):
    return slope*High+intercept
score = calc(regressor.coef_, regressor.intercept_, 9.5)
print(score) # [[94.80663482]]


score = regressor.predict([[9.5]])
print(score) # 94.80663482



y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)



from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')

#Applying multiple regression on ML n oracle csv.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('Final Assessment/oracle.csv')


print("df.head():  \n",df.head())

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)


import seaborn as sns 

variables =['Open','High','Low','Close','Adj Close','Volume']

for var in variables:
    plt.figure() 
    sns.regplot(x=var, y='Close', data=df).set(title=f'Regression plot of {var} and Close');
    plt.show()

read = input("Wait here: \n")


plt.figure()
df['Date']= pd.to_datetime(df['Date'])
df['year']= df['Date'].dt.year
df['Month']= df['Date'].dt.month
df['Day']= df['Date'].dt.day
correlations = df.corr()
print("correlations...\n" , correlations)
g = sns.heatmap(correlations, annot=True).set(title='Heat map of Close Data - Pearson Correlations')
# Display the plot
plt.show()
read = input("Wait for me....")



y = df['Close']
X = df[['Low', 'High',
       'Adj Close', 'Open']]

SEED = 200
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                    random_state=SEED)

print("X.shape # (48, 4):     \n", X.shape )   



from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

print("regressor.intercept_......\n", regressor.intercept_)

#And at the coefficients of the features
print("regressor.coef_ " , regressor.coef_)


feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients, 
                              index = feature_names, 
                              columns = ['Close'])
print(coefficients_df)


y_pred = regressor.predict(X_test)


results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)



from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')



actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)

print(" R2 also comes implemented by default into the score method of Scikit-Learn's linear regressor class...\n", regressor.score(X_test, y_test))




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


data = pd.read_csv('Final Assessment/oracle.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
Close= data['Close'].astype(float).values.reshape(-1, 1)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(Close)


window_size = 12
X = []
y = []
target_dates = data.index[window_size:]

for i in range(window_size, len(scaled_data)):
    X.append(scaled_data[i - window_size:i, 0])  
    y.append(scaled_data[i, 0])

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test, dates_train, dates_test = train_test_split(
    X, y, target_dates, test_size=0.2, shuffle=False
)

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

model = Sequential()
model.add(LSTM(units=128, return_sequences=True,
          input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=128))
model.add(Dropout(0.2))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.1)

predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions).flatten()
y_test = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()

rmse = np.sqrt(np.mean((y_test - predictions)**2))
print(f'RMSE: {rmse:.2f}')


plt.figure(figsize=(12, 6))
plt.plot(dates_test, y_test, label='Actual Production')
plt.plot(dates_test, predictions, label='Predicted Production')
plt.title('Actual vs Predicted Close')
plt.xlabel('Date')
plt.ylabel('Prediction of next close value')
plt.legend()
plt.show()

# Applying GRU Of ML in oracle Csv
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from tensorflow.keras.optimizers import Adam
from keras.metrics import Precision, Recall


df = pd.read_csv('Final Assessment/oracle.csv', parse_dates=['Date'], index_col='Date')
print(df.head())


scaler = MinMaxScaler(feature_range=(0, 1))

close_data = df[['Close']].values

scaled_data = scaler.fit_transform(close_data)

scaler = MinMaxScaler(feature_range=(0, 1))

close_data = df[['Close']].values

scaled_data = scaler.fit_transform(close_data)


def create_dataset(data, time_step=1):
    X, y = [], []
    for i in range(len(data) - time_step - 1):
        X.append(data[i:(i + time_step), 0])
        y.append(data[i + time_step, 0])
    return np.array(X), np.array(y)


time_step = 100

X, y = create_dataset(scaled_data, time_step)

X = X.reshape(X.shape[0], X.shape[1], 1)


model = Sequential()

model.add(GRU(units=50, return_sequences=True,
              input_shape=(X.shape[1], 1)))

model.add(GRU(units=50))

model.add(Dense(units=1))


METRICS = [
    'accuracy',
    Precision(name='precision'),
    Recall(name='recall')
]

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='mean_squared_error',
    metrics=METRICS
)

model.fit(X, y, epochs=10, batch_size=32)


input_sequence = scaled_data[-time_step:].reshape(1, time_step, 1)

predicted_values = model.predict(input_sequence)

predicted_values = scaler.inverse_transform(predicted_values)

print("The predicted Close for the next day:", predicted_values[0][0])
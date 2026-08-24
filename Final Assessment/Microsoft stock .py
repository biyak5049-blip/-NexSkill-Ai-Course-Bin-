#using linear regression in microsoft stock action.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Final Assessment/MicrosoftStock/Microsoft_stock_action.csv")
print(df.head())
print("df.shape:  ",df.shape)

df.plot.scatter(x= 'Dividends', y='Stock Splits',title= 'scatter plot of Dividends and Stock Splits')
plt.show()
#should not use lable coding for date,convert it into dateline by following method:
print(df['Date'])
df['Date']= pd.to_datetime(df['Date'])
df['year']= df['Date'].dt.year
df['Month']= df['Date'].dt.month
df['Day']= df['Date'].dt.day
print("df.corr():        " , df.corr())

print("df.describe():   ", df.describe)
print("df['Dividends']:  ",   df['Dividends'])
print("df['Stock Splits']:  ", df['Stock Splits'])

x= df['Dividends'].values .reshape(-1,1)
y= df['Stock Splits'].values.reshape(-1,1)
print("x: " ,x)
print("y: ", y)


print(df['Dividends'].values)
print(df['Dividends'].values.shape)
print(x.shape)
print(x)

seed= 42
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train,Y_test= train_test_split(x,y, test_size=0.2,random_state = seed)
print(X_train)
print(Y_train)
#training linear regression model
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(X_train,Y_train) 
print(regressor.intercept_) 
print(regressor.coef_) 
def calc(slope, intercepts,Dividends): 
    return slope*Dividends+intercepts
Stock_Splits= calc(regressor.coef_, regressor.intercept_, 9.5)
print(Stock_Splits)

y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': Y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)


    
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np

mae = mean_absolute_error(Y_test, y_pred)
mse = mean_squared_error(Y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(Y_test, y_pred)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')


#applying multiple linear regression on microstock history.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("Final Assessment/MicrosoftStock/Microsoft_stock_history.csv")

print("df.head():  \n",df.head())

print("df.shape: \n" , df.shape)

print("df.describe().round(2).T:    \n",df.describe().round(2).T)


import seaborn as sns # Convention alias for Seaborn

variables = ['Close','High','Low','Open']

for var in variables:
    plt.figure() 
    sns.regplot(x=var, y='Volume', data=df).set(title=f'Regression plot of {var} and Volume');
    plt.show()

read = input("Wait here: \n")


plt.figure()
# for correlation using datetime data for convert string to float or integer.

df['Date'] = pd.to_datetime(df['Date'])

df['Date_numeric'] = df['Date'].astype('int64')

correlations = df.corr(numeric_only=True)


correlations = df.corr()
print("correlations...\n" , correlations)
g = sns.heatmap(correlations, annot=True).set(title='Heat map of  stock_history - Pearson Correlations')
plt.show()

y = df['Volume']
X = df[['Adj Close','Close','High','Low','Open']]

SEED = 200
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.2, 
                                                 random_state=SEED)

print("X.shape # (48, 4):     \n", X.shape )   


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)

#After fitting the model and finding our optimal solution, we can also look at the intercept:
print("regressor.intercept_......\n", regressor.intercept_)

#And at the coefficients of the features
print("regressor.coef_ " , regressor.coef_)


feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(data = model_coefficients, 
                              index = feature_names, 
                              columns = ['Low'])
print(coefficients_df)


#In the same way we had done for the simple regression model, let's predict with the test data:
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

 applying linear regression on microsoft history csv:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# load dataset
df = pd.read_csv("Final Assessment/MicrosoftStock/Microsoft_stock_history.csv")

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract date features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day


print("df.corr():        " , df.corr())
print("df.describe():                    " , df.describe())
print(df.head())

#We can also check the shape of our dataset via the shape property:
print("df.shape:         " , df.shape)

#So, what's the relationship between these variables? A great way to explore relationships between variables is through Scatter plots. We'll plot the hours on the X-axis and scores on the Y-axis, and for each pair, a marker will be positioned based on their values:
df.plot.scatter(x='Open', y='Close', title='Scatter Plot of Open and Close percentages');
plt.show()





print(" df['Open'] :     " , df['Open'])
print("  df['Close']   :    ", df['Close']   )



y = df['Open'].values.reshape(-1, 1)
X = df['Close'].values.reshape(-1, 1)
  


print("y :  " , y)
print("X :   " , X)

#Scikit-Learn's linear regression model expects a 2D input, and we're really offering a 1D array if we just extract the values:

print(df['Open'].values) 
print(df['Open'].values.shape) 

print(X.shape) # (25, 1)
print(X)  
SEED = 42

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = SEED)


print(X_train) 
print(y_train) 

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train, y_train)
print(regressor.intercept_)


print(regressor.coef_)

def calc(slope, intercept, Open):
    return slope*Open+intercept
Close= calc(regressor.coef_, regressor.intercept_, 9.5)
print(Close) 
y_pred = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)


# Passing 9.5 in double brackets to have a 2 dimensional array
Close = regressor.predict([[9.5]])
print(Close) # 94.80663482

from sklearn import metrics

mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = metrics.root_mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R2 Score:", r2)

applying long_short term memory of RNN on microsoft history csv.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

Data= pd.read_csv('Final Assessment/MicrosoftStock/Microsoft_stock_history.csv')

Data['Date'] = pd.to_datetime(Data['Date'])
Data.set_index('Date', inplace=True)
Close= Data['Close'].astype(float).values.reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(Close)
window_size = 12
X = []
y = []
target_dates = Data.index[window_size:]
for i in range(window_size, len(scaled_data)):
    X.append(scaled_data[i - window_size:i, 0])
    y.append(scaled_data[i, 0])
X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test, dates_train, dates_test = train_test_split(
    X, y, target_dates, test_size=0.2, shuffle=False)
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
plt.plot(dates_test, y_test, label='Actual Close')
plt.plot(dates_test, predictions, label='Predicted Close')
plt.title('Actual vs Predicted Close')
plt.xlabel('Date')
plt.ylabel('Close')
plt.legend()
plt.show()

Applying Gated recurrent unit in RNN using microsoft stock history
 

import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Input
from tensorflow.keras.optimizers import Adam


# Load dataset
df = pd.read_csv(
    'Final Assessment/MicrosoftStock/Microsoft_stock_history.csv'
)

print(df.head())
print(df.columns)


# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort data according to Date
df = df.sort_values('Date')


# We want to predict Close price
close_data = df[['Close']].values


# Scale only Close column
scaler = MinMaxScaler(feature_range=(0, 1))

scaled_data = scaler.fit_transform(close_data)


# Create sequences
def create_dataset(data, time_step=100):

    X = []
    y = []

    for i in range(len(data) - time_step):

        # Previous 100 Close prices
        X.append(data[i:i + time_step, 0])

        # Next Close price
        y.append(data[i + time_step, 0])

    return np.array(X), np.array(y)


time_step = 100

X, y = create_dataset(scaled_data, time_step)


# GRU requires 3D data:
# samples, time_steps, features
X = X.reshape(X.shape[0], X.shape[1], 1)


print("X shape:", X.shape)
print("y shape:", y.shape)


# Create GRU model
model = Sequential()

model.add(Input(shape=(X.shape[1], 1)))

model.add(
    GRU(
        units=50,
        return_sequences=True
    )
)

model.add(GRU(units=50))

model.add(Dense(units=1))


# Compile model
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='mean_squared_error',
    metrics=['mae']
)


# Train model
model.fit(
    X,
    y,
    epochs=10,
    batch_size=32
)


# Last 100 days data
input_sequence = scaled_data[-time_step:]


# Reshape for GRU
input_sequence = input_sequence.reshape(
    1,
    time_step,
    1
)


# Predict next Close price
predicted_value = model.predict(input_sequence)


# Convert prediction back to original price
predicted_close = scaler.inverse_transform(predicted_value)


print("Predicted next Close price:", predicted_close[0][0])



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout



data = pd.read_csv('Final Assessment/MicrosoftStock/Microsoft_stock_spilts.csv')

print("Columns:")
print(data.columns)

print("\nDataset shape:", data.shape)
print("\nFirst 5 rows:")
print(data.head())



data.columns = data.columns.str.strip()

data['Date'] = pd.to_datetime(data['Date'])

data = data.sort_values('Date')

data.set_index('Date', inplace=True)



stock_splits = (
    data['Stock Splits']
    .astype(float)
    .values
    .reshape(-1, 1)
)

print("\nTotal data points:", len(stock_splits))



scaler = MinMaxScaler(feature_range=(0, 1))

scaled_data = scaler.fit_transform(stock_splits)



# Dataset ke according window size
window_size = min(12, max(1, len(scaled_data) // 4))

print("Window size:", window_size)


X = []
y = []

target_dates = []


for i in range(window_size, len(scaled_data)):

    # Previous values
    X.append(scaled_data[i - window_size:i, 0])

    # Next value
    y.append(scaled_data[i, 0])

    # Corresponding date
    target_dates.append(data.index[i])


X = np.array(X)
y = np.array(y)
target_dates = np.array(target_dates)


print("\nX shape:", X.shape)
print("y shape:", y.shape)


# Check enough sequences exist
if len(X) < 2:
    raise ValueError(
        f"Not enough data to train the LSTM. "
        f"Total rows = {len(data)}, window size = {window_size}, "
        f"sequences created = {len(X)}"
    )

split_index = int(len(X) * 0.8)

X_train = X[:split_index]
X_test = X[split_index:]

y_train = y[:split_index]
y_test = y[split_index:]

dates_train = target_dates[:split_index]
dates_test = target_dates[split_index:]


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))



X_train = X_train.reshape(
    X_train.shape[0],
    X_train.shape[1],
    1
)

X_test = X_test.reshape(
    X_test.shape[0],
    X_test.shape[1],
    1)

model = Sequential()

model.add(
    LSTM(
        units=128,
        return_sequences=True,
        input_shape=(X_train.shape[1], 1)
    )
)

model.add(Dropout(0.2))

model.add(LSTM(units=128))

model.add(Dropout(0.2))

model.add(Dense(units=1))



model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)



history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)


predictions = model.predict(X_test)

predictions = scaler.inverse_transform(
    predictions
).flatten()


# Convert actual values back
y_test_actual = scaler.inverse_transform(
    y_test.reshape(-1, 1)
).flatten()



rmse = np.sqrt(
    np.mean(
        (y_test_actual - predictions) ** 2
    )
)

print(f"\nRMSE: {rmse:.4f}")



plt.figure(figsize=(12, 6))

plt.plot(
    dates_test,
    y_test_actual,
    label='Actual Stock Splits'
)

plt.plot(
    dates_test,
    predictions,
    label='Predicted Stock Splits'
)

plt.title('Actual vs Predicted Microsoft Stock Splits')

plt.xlabel('Date')

plt.ylabel('Stock Splits')

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()



# applying GRU RNN microsoft stock split csv:
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Input
from tensorflow.keras.optimizers import Adam


df = pd.read_csv(
    'Final Assessment/MicrosoftStock/Microsoft_stock_spilts.csv'
)

# Remove spaces from column names
df.columns = df.columns.str.strip()

print("Columns:")
print(df.columns)

print("\nDataset:")
print(df.head())


df['Date'] = pd.to_datetime(df['Date'])

df = df.sort_values('Date')

df.set_index('Date', inplace=True)



stock_splits = df[['Stock Splits']].astype(float).values

print("\nStock Splits Shape:")
print(stock_splits.shape)



scaler = MinMaxScaler(feature_range=(0, 1))

scaled_data = scaler.fit_transform(stock_splits)

print("\nScaled Data Shape:")
print(scaled_data.shape)



# Dataset chhota ho to 12 force nahi karein
time_step = 12

# Agar rows kam hain to automatic smaller window
if len(scaled_data) <= time_step:
    time_step = max(1, len(scaled_data) - 2)

print("\nTime Step:", time_step)



def create_dataset(data, time_step):

    X = []
    y = []

    for i in range(len(data) - time_step):

        # Previous time_step values
        X.append(data[i:i + time_step])

        # Next value
        y.append(data[i + time_step])

    return np.array(X), np.array(y)


X, y = create_dataset(scaled_data, time_step)


print("\nX Shape:", X.shape)
print("y Shape:", y.shape)

if len(X) == 0:
    raise ValueError(
        f"No sequences were created. "
        f"Dataset rows: {len(scaled_data)}, "
        f"time_step: {time_step}"
    )

if X.shape[1] == 0:
    raise ValueError(
        "Time steps are 0. Cannot train GRU."
    )



print("\nFinal GRU Input Shape:")
print(X.shape)



model = Sequential([
    
    Input(shape=(X.shape[1], X.shape[2])),

    GRU(
        units=50,
        return_sequences=True
    ),

    GRU(
        units=50
    ),

    Dense(
        units=1
    )
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='mean_squared_error',
    metrics=['mae']
)


model.summary()



model.fit(
    X,
    y,
    epochs=10,
    batch_size=min(32, len(X)),
    verbose=1
)


# Last time_step values
input_sequence = scaled_data[-time_step:]

# Shape:
# (1, time_steps, features)
input_sequence = input_sequence.reshape(
    1,
    time_step,
    1
)


# Predict
predicted_scaled = model.predict(input_sequence)


# Convert back to original scale
predicted_value = scaler.inverse_transform(
    predicted_scaled
)



print("MICROSOFT STOCK SPLIT PREDICTION")


print(
    "Predicted next Stock Split value:",
    predicted_value[0][0]
)



#applying classification dataset for microsoft info csv:

import pandas as pd

df_raw = pd.read_csv(
    "Final Assessment/MicrosoftStock/Microsoft_stock_info.csv",
    header=None,
    names=["column", "value"]
)

print("Raw Data:")
print(df_raw.head())


df = df_raw.set_index("column").T.reset_index(drop=True)

print("\nMicrosoft Dataset:")
print(df)

print("\nColumn Names:")
print(df.columns.tolist())


numeric_cols = [
    "profitMargins",
    "revenueGrowth",
    "operatingMargins",
    "currentRatio",
    "returnOnAssets",
    "debtToEquity",
    "returnOnEquity",
    "totalRevenue",
    "totalCash",
    "totalDebt",
    "marketCap",
    "priceToBook",
    "trailingPE",
    "previousClose",
    "regularMarketPrice"
]

for col in numeric_cols:
     df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df["label"] = (
    df["regularMarketPrice"] >
    df["previousClose"]
).astype(int)

print("\nTarget Label:")
print(df["label"])

feature_cols = [
    "profitMargins",
    "revenueGrowth",
    "operatingMargins",
    "currentRatio",
    "returnOnAssets",
    "debtToEquity",
    "returnOnEquity",
    "totalRevenue",
    "totalCash",
    "totalDebt",
    "marketCap",
    "priceToBook",
    "trailingPE"
]

X = df[feature_cols]

y = df["label"]


X = X.fillna(0)


print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(
    random_state=16,
    max_iter=1000
)


print("\nNumber of samples:", len(X))
print("Number of classes:", y.nunique())


if len(X) < 2:

    print("\nERROR:")
    print("Logistic Regression cannot be trained.")
    print("Your dataset contains only one sample.")

else:

    logreg.fit(X, y)

    y_pred = logreg.predict(X)

    print("\nPredicted Value:")
    print(y_pred)
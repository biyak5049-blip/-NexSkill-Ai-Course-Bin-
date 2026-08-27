

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Final Assessment/Salesforce (CRM) From 2004 To Dec-2024.csv")

print(df.head())

print('df.shape: ', df.shape)


# Log Returns

returns = np.log(
    df['Close'] / df['Close'].shift(1)
)

# Optional: save returns in dataframe
df['Log_Return'] = returns


# Scatter Plot

df.plot.scatter(
    x='High',
    y='Low',
    title='Scatter plot of High and Low'
)

plt.show()


# Convert Date to datetime

df['Date'] = pd.to_datetime(
    df['Date'],
    utc=True
)
df['year'] = df['Date'].dt.year

df['Month'] = df['Date'].dt.month

df['Day'] = df['Date'].dt.day


# Correlation

print(
    "df.corr():",
    df.corr(numeric_only=True)
)


# Describe

print(
    "df.describe():",
    df.describe()
)


print(
    "df['High']:",
    df['High']
)


print(
    "df['Low']:",
    df['Low']
)



y = df['High'].values.reshape(-1, 1)

X = df['Low'].values.reshape(-1, 1)


print("y:", y)

print("X:", X)


print(df['High'].values)

print(df['High'].values.shape)

print(X.shape)

print(X)



SEED = 42

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=SEED
)


print(X_train)

print(y_train)


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(
    X_train,
    y_train
)


print(regressor.intercept_)

print(regressor.coef_)



def calc(slope, intercept, High):

    return slope * High + intercept


Close = calc(
    regressor.coef_,
    regressor.intercept_,
    9.5
)

print(Close)



Low = regressor.predict([[9.5]])

print(Low)




y_pred = regressor.predict(X_test)


df_preds = pd.DataFrame({
    'Actual': y_test.squeeze(),
    'Predicted': y_pred.squeeze()
})

print(df_preds)



from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test,
    y_pred
)


print(f'Mean absolute error: {mae:.2f}')

print(f'Mean squared error: {mse:.2f}')

print(f'Root mean squared error: {rmse:.2f}')

print(f'R2 Score: {r2:.2f}')


# ADDITIONAL PROFESSIONAL ANALYSIS

import seaborn as sns


# 1. DATA VALIDATION

print("\nMISSING VALUES:")

print(df.isnull().sum())


print("\nDUPLICATE ROWS:")

print(df.duplicated().sum())


print("\nDATA TYPES:")

print(df.dtypes)



plt.figure(figsize=(12, 6))

plt.plot(
    df['Date'],
    df['Close']
)

plt.title('Salesforce Historical Close Price')

plt.xlabel('Date')

plt.ylabel('Close Price')

plt.grid()

plt.show()



plt.figure(figsize=(12, 8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    fmt='.2f'
)

plt.title('Saleforce(CRM) from 2004 to Dec-2024 Correlation Heatmap')

plt.show()


plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    y_pred
)

plt.xlabel('Actual High Price')

plt.ylabel('Predicted High Price')

plt.title(
    'Linear Regression: Actual vs Predicted'
)

plt.grid()

plt.show()



residuals = (
    y_test.squeeze()
    -
    y_pred.squeeze()
)


plt.figure(figsize=(8, 6))

sns.histplot(
    residuals,
    kde=True
)

plt.title(
    'Linear Regression Residual Distribution'
)

plt.xlabel(
    'Actual - Predicted'
)

plt.show()


# Daily percentage return

df['Return'] = (
    df['Close'].pct_change()
)


# Annualized Volatility

annual_volatility = (
    df['Return'].std()
    *
    np.sqrt(252)
)


print(
    "\nAnnualized Volatility:",
    annual_volatility
)


# Cumulative Return

cum_return = np.cumprod(
    1 + df['Return'].fillna(0)
)


# Running Maximum

running_max = np.maximum.accumulate(
    cum_return
)


# Drawdown

drawdown = (
    cum_return - running_max
) / running_max


df['Drawdown'] = drawdown


print(
    "\nMaximum Drawdown:",
    df['Drawdown'].min()
)


# Drawdown Plot

plt.figure(figsize=(12, 6))

plt.plot(
    df['Date'],
    df['Drawdown']
)

plt.title(
    'Saleforce(CRM) from 2004 to Dec-2024 Stock Drawdown Analysis'
)

plt.xlabel('Date')

plt.ylabel('Drawdown')

plt.grid()

plt.show()





print(f"MAE: {mae:.4f}")

print(f"MSE: {mse:.4f}")

print(f"RMSE: {rmse:.4f}")

print(f"R2 SCORE: {r2:.4f}")

print(f"ANNUAL VOLATILITY: {annual_volatility:.4f}")

print(
    f"MAXIMUM DRAWDOWN: "
    f"{df['Drawdown'].min():.4f}"
)


APPLYING MULTIPLE LINEAR REGRESSION IN SALESFORCE CSV

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



df = pd.read_csv(
    "Final Assessment/Salesforce (CRM) From 2004 To Dec-2024.csv"
)

print("df.head():\n", df.head())

print("\ndf.shape:\n", df.shape)

print(
    "\ndf.describe().round(2).T:\n",
    df.describe().round(2).T
)


print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nColumn Names:")
print(df.columns)


df['Date'] = pd.to_datetime(
    df['Date'],
    utc=True
).dt.tz_localize(None)



df['year'] = df['Date'].dt.year

df['Month'] = df['Date'].dt.month

df['Day'] = df['Date'].dt.day



df['MA20'] = (
    df['Close']
    .rolling(20)
    .mean()
)

df['STD20'] = (
    df['Close']
    .rolling(20)
    .std()
)



import seaborn as sns


variables = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume"
]

for var in variables:

    plt.figure()

    sns.regplot(
        x=var,
        y='Close',
        data=df
    ).set(
        title=f'Regression plot of {var} and Close'
    )

    plt.show()


df['Return'] = (
    df['Close']
    .pct_change()
)


plt.figure()

sns.histplot(
    df['Return'].dropna(),
    kde=True
)

plt.title(
    'Salesforce Return Distribution'
)

plt.xlabel('Daily Return')

plt.show()



correlations = df.corr(
    numeric_only=True
)

print(
    "\nCorrelations...\n",
    correlations
)



plt.figure(
    figsize=(12, 8)
)

sns.heatmap(
    correlations,
    annot=True,
    fmt='.2f'
)

plt.title(
    'Heat Map of Salesforce Data - Pearson Correlations'
)

plt.show()


#  MULTIPLE LINEAR REGRESSION

y = df['Close']


X = df[
    [
        'Low',
        'High',
        'Open',
        'Volume'
    ]
]



# 14. REMOVE MISSING VALUES


model_data = pd.concat(
    [X, y],
    axis=1
).dropna()


X = model_data[
    [
        'Low',
        'High',
        'Open',
        'Volume'
    ]
]

y = model_data['Close']



SEED = 200

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=SEED
)


print(
    "\nX.shape:\n",
    X.shape
)



from sklearn.linear_model import LinearRegression


regressor = LinearRegression()


regressor.fit(
    X_train,
    y_train
)


print(
    "\nregressor.intercept_:\n",
    regressor.intercept_
)


print(
    "\nregressor.coef_:\n",
    regressor.coef_
)


feature_names = X.columns

model_coefficients = regressor.coef_


coefficients_df = pd.DataFrame(
    data=model_coefficients,
    index=feature_names,
    columns=['Close']
)


print(
    "\nModel Coefficients:\n",
    coefficients_df
)



y_pred = regressor.predict(
    X_test
)



results = pd.DataFrame(
    {
        'Actual': y_test,
        'Predicted': y_pred
    }
)


print(
    "\nActual vs Predicted.....\n",
    results
)



from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


mae = mean_absolute_error(
    y_test,
    y_pred
)


mse = mean_squared_error(
    y_test,
    y_pred
)


rmse = np.sqrt(
    mse
)


r2 = r2_score(
    y_test,
    y_pred
)


print(
    f'\nMean absolute error: {mae:.2f}'
)

print(
    f'Mean squared error: {mse:.2f}'
)

print(
    f'Root mean squared error: {rmse:.2f}'
)

print(
    f'R2 Score: {r2:.2f}'
)


print(
    "\nR² using regressor.score():",
    regressor.score(
        X_test,
        y_test
    )
)



plt.figure(
    figsize=(10, 6)
)

plt.plot(
    y_test.values,
    label='Actual'
)

plt.plot(
    y_pred,
    label='Predicted'
)

plt.title(
    'Salesforce: Actual vs Predicted Close Price'
)

plt.xlabel('Test Samples')

plt.ylabel('Close Price')

plt.legend()

plt.grid()

plt.show()



df['Log_Return'] = np.log(
    df['Close'] /
    df['Close'].shift(1)
)


print(
    "\nLog Returns:"
)

print(
    df['Log_Return'].head()
)


annual_volatility = (
    df['Log_Return']
    .std()
    *
    np.sqrt(252)
)


print(
    "\nAnnualized Volatility:",
    annual_volatility
)


df['MA5'] = (
    df['Close']
    .rolling(5)
    .mean()
)

df['MA10'] = (
    df['Close']
    .rolling(10)
    .mean()
)

df['MA50'] = (
    df['Close']
    .rolling(50)
    .mean()
)



plt.figure(
    figsize=(12, 6)
)

plt.plot(
    df['Date'],
    df['Close'],
    label='Close'
)

plt.plot(
    df['Date'],
    df['MA20'],
    label='MA20'
)

plt.plot(
    df['Date'],
    df['MA50'],
    label='MA50'
)

plt.title(
    'Salesforce Close Price with Moving Averages'
)

plt.xlabel('Date')

plt.ylabel('Price')

plt.legend()

plt.grid()

plt.show()



df['Mom5'] = (
    df['Close'] /
    df['Close'].shift(5)
)

df['Mom20'] = (
    df['Close'] /
    df['Close'].shift(20)
)


print(
    "\nMomentum Features:"
)

print(
    df[
        ['Mom5', 'Mom20']
    ].tail()
)



df['HL_Range'] = (
    (df['High'] - df['Low'])
    /
    df['Close']
)



df['Gap'] = (
    (df['Open'] - df['Close'].shift(1))
    /
    df['Close'].shift(1)
)



df['Volume_Ratio'] = (
    df['Volume']
    /
    df['Volume'].rolling(20).mean()
)



df['Vol5'] = (
    df['Log_Return']
    .rolling(5)
    .std()
)

df['Vol10'] = (
    df['Log_Return']
    .rolling(10)
    .std()
)

df['Vol20'] = (
    df['Log_Return']
    .rolling(20)
    .std()
)


cum_return = np.cumprod(
    1 + df['Return'].fillna(0)
)


running_max = np.maximum.accumulate(
    cum_return
)


drawdown = (
    cum_return - running_max
) / running_max


df['Drawdown'] = drawdown


print(
    "\nMaximum Drawdown:",
    df['Drawdown'].min()
)



plt.figure(
    figsize=(12, 6)
)

plt.plot(
    df['Date'],
    df['Drawdown']
)

plt.title(
    'Salesforce Stock Drawdown Analysis'
)

plt.xlabel('Date')

plt.ylabel('Drawdown')

plt.grid()

plt.show()



residuals = (
    y_test.values
    -
    y_pred
)


plt.figure(
    figsize=(10, 6)
)

sns.histplot(
    residuals,
    kde=True
)

plt.title(
    'Multiple Regression Residual Distribution'
)

plt.xlabel(
    'Actual - Predicted'
)

plt.show()


# 

print(
    f"MAE  : {mae:.4f}"
)

print(
    f"MSE  : {mse:.4f}"
)

print(
    f"RMSE : {rmse:.4f}"
)

print(
    f"R²   : {r2:.4f}"
)

print(
    f"Annualized Volatility : "
    f"{annual_volatility:.4f}"
)

print(
    f"Maximum Drawdown : "
    f"{df['Drawdown'].min():.4f}"
)

# APPLYING LSTM AND GRU IN SALESFORCE CSV



 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout


df = pd.read_csv(
    "Final Assessment/Salesforce (CRM) From 2004 To Dec-2024.csv"
)

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns.tolist())


# Convert Date to datetime
# utc=True handles mixed timezones

df['Date'] = pd.to_datetime(
    df['Date'],
    utc=True
).dt.tz_localize(None)


# Sort according to Date

df = df.sort_values(
    'Date'
).reset_index(
    drop=True
)



production = df['Close'].astype(float).values.reshape(-1, 1)

scaler = MinMaxScaler(
    feature_range=(0, 1)
)

scaled_data = scaler.fit_transform(
    production
)


print("\nScaled Data:")
print(scaled_data[:5])



window_size = 60

X = []
y = []

for i in range(
    window_size,
    len(scaled_data)
):

    X.append(
        scaled_data[
            i - window_size:i,
            0
        ]
    )

    y.append(
        scaled_data[
            i,
            0
        ]
    )


X = np.array(X)

y = np.array(y)


print("\nX Shape:")
print(X.shape)

print("\ny Shape:")
print(y.shape)



train_size = int(
    len(X) * 0.8
)

X_train = X[:train_size]

X_test = X[train_size:]

y_train = y[:train_size]

y_test = y[train_size:]




X_train = X_train.reshape(
    X_train.shape[0],
    X_train.shape[1],
    1
)

X_test = X_test.reshape(
    X_test.shape[0],
    X_test.shape[1],
    1
)


print("\nX_train Shape:")
print(X_train.shape)

print("\nX_test Shape:")
print(X_test.shape)


# 5. BUILDING THE LSTM MODEL


model_lstm = Sequential()

model_lstm.add(
    LSTM(
        units=128,
        return_sequences=True,
        input_shape=(
            X_train.shape[1],
            1
        )
    )
)

model_lstm.add(
    Dropout(0.2)
)

model_lstm.add(
    LSTM(
        units=128
    )
)

model_lstm.add(
    Dropout(0.2)
)

model_lstm.add(
    Dense(1)
)


model_lstm.compile(
    optimizer='adam',
    loss='mean_squared_error'
)


print("\nLSTM Model Summary:")

model_lstm.summary()


# 6. TRAINING THE LSTM MODEL

history_lstm = model_lstm.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.1
)


# 7. MAKING LSTM PREDICTIONS

predictions_lstm = model_lstm.predict(
    X_test
)


# 8. INVERSE TRANSFORMING LSTM PREDICTIONS

predictions_lstm = scaler.inverse_transform(
    predictions_lstm
).flatten()


y_test_actual = scaler.inverse_transform(
    y_test.reshape(-1, 1)
).flatten()



# 9. LSTM RMSE


rmse_lstm = np.sqrt(
    np.mean(
        (y_test_actual - predictions_lstm) ** 2
    )
)


print(
    f"\nLSTM RMSE: {rmse_lstm:.2f}"
)


# 10. LSTM ACTUAL VS PREDICTED

plt.figure(
    figsize=(12, 6)
)

plt.plot(
    y_test_actual,
    label='Actual Close'
)

plt.plot(
    predictions_lstm,
    label='Predicted Close'
)

plt.title(
    'Salesforce (CRM) - LSTM Actual vs Predicted'
)

plt.xlabel(
    'Test Samples'
)

plt.ylabel(
    'Close Price'
)

plt.legend()

plt.grid()

plt.show()




# 1. IMPORTING GRU LIBRARIES

from tensorflow.keras.layers import GRU

from tensorflow.keras.optimizers import Adam


df_gru = pd.read_csv(
    "Final Assessment/Salesforce (CRM) From 2004 To Dec-2024.csv"
)

print("\nGRU Dataset:")
print(df_gru.head())


# Convert Date

df_gru['Date'] = pd.to_datetime(
    df_gru['Date'],
    utc=True
).dt.tz_localize(None)


# Sort Date

df_gru = df_gru.sort_values(
    'Date'
).reset_index(
    drop=True
)


scaler_gru = MinMaxScaler(
    feature_range=(0, 1)
)

scaled_data_gru = scaler_gru.fit_transform(
    df_gru['Close']
    .astype(float)
    .values
    .reshape(-1, 1)
)



def create_dataset(
    data,
    time_step=1
):

    X, y = [], []

    for i in range(
        len(data) - time_step - 1
    ):

        X.append(
            data[
                i:(i + time_step),
                0
            ]
        )

        y.append(
            data[
                i + time_step,
                0
            ]
        )

    return (
        np.array(X),
        np.array(y)
    )


# Sir's code uses time_step = 100

time_step = 100


X_gru, y_gru = create_dataset(
    scaled_data_gru,
    time_step
)


print("\nGRU X Shape:")
print(X_gru.shape)

print("\nGRU y Shape:")
print(y_gru.shape)


"""
X.reshape()

GRU expects 3D input:

[samples, time steps, features]
"""

X_gru = X_gru.reshape(
    X_gru.shape[0],
    X_gru.shape[1],
    1
)





model_gru = Sequential()


model_gru.add(
    GRU(
        units=50,
        return_sequences=True,
        input_shape=(
            X_gru.shape[1],
            1
        )
    )
)


model_gru.add(
    GRU(
        units=50
    )
)


model_gru.add(
    Dense(
        units=1
    )
)


# 6. COMPILE GRU MODEL

model_gru.compile(
    optimizer=Adam(
        learning_rate=0.001
    ),
    loss='mean_squared_error'
)


print("\nGRU Model Summary:")

model_gru.summary()


# 7. TRAINING GRU MODEL

model_gru.fit(
    X_gru,
    y_gru,
    epochs=10,
    batch_size=32
)


# 8. MAKING GRU PREDICTION

input_sequence = (
    scaled_data_gru[-time_step:]
    .reshape(
        1,
        time_step,
        1
    )
)


predicted_values = model_gru.predict(
    input_sequence
)


# 9. INVERSE TRANSFORMING GRU PREDICTION

predicted_values = scaler_gru.inverse_transform(
    predicted_values
)


print(
    "\nPredicted Salesforce Close Price "
    "for Next Trading Day:"
)

print(
    f"${predicted_values[0][0]:.2f}"
)


# 10. GRU TRAINING PREDICTION

gru_predictions = model_gru.predict(
    X_gru
)


gru_predictions = scaler_gru.inverse_transform(
    gru_predictions
).flatten()


gru_actual = scaler_gru.inverse_transform(
    y_gru.reshape(-1, 1)
).flatten()


# 11. GRU RMSE

rmse_gru = np.sqrt(
    np.mean(
        (gru_actual - gru_predictions) ** 2
    )
)


print(
    f"\nGRU RMSE: {rmse_gru:.2f}"
)


# 12. GRU ACTUAL VS PREDICTED

plt.figure(
    figsize=(12, 6)
)

plt.plot(
    gru_actual,
    label='Actual Close'
)

plt.plot(
    gru_predictions,
    label='Predicted Close'
)

plt.title(
    'Salesforce (CRM) - GRU Actual vs Predicted'
)

plt.xlabel(
    'Samples'
)

plt.ylabel(
    'Close Price'
)

plt.legend()

plt.grid()

plt.show()



print(
    f"LSTM RMSE: {rmse_lstm:.2f}"
)

print(
    f"GRU RMSE: {rmse_gru:.2f}"
)

print(
    f"Next Day GRU Prediction: "
    f"${predicted_values[0][0]:.2f}"
)


import pandas as pd
df=pd.read_csv('FastFoodRestaurants.csv', delimiter=',', parse_dates=[9],date_format={'date_added:','%d-%m-%y'})
print(df)
print('df-data types', df.dtypes)
print('df.info():', df.info())
print()

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()



# access the Name column
longitude = df['longitude']
print("access the Name column: df : ")
print(longitude)
print()



# access multiple columns
longitude_latitude = df[['longitude','latitude']]
print("access multiple columns: df : ")
print(longitude_latitude)
print()

#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()


#Conditional selection of rows using .loc
second_row4 = df.loc[df['latitude'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()
#Selecting a single column using .loc
second_row5 = df.loc[:1,'latitude']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:,['latitude','longitude']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'province':'latitude']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['latitude'] == 'Gateway Properties','province':'latitude']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here

df_index_col= pd.read_csv('FastFoodRestaurants.csv', delimiter=',', parse_dates=[9],date_format={'date added:','%d-%m-%y'},index_col= 'longitude')
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

#Selecting a single row using .loc
second_row = df_index_col.loc[-74.89021]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[-74.89021, -83.44526]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[-74.89021:-83.44526]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['latitude'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#electing a single column using .loc
second_row5 = df_index_col.loc[:-74.89021,'latitude']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:-74.89021,['latitude','province']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:-74.89021,'country':'latitude']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['latitude'] == 'Gateway Properties','country':'latitude']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()
df.loc[len(df.index)]= ['address','city','country','keys','latitude','longitude','name','postalCode','province','websites']

print("Modified DataFrame - add a new row:")
print(df)
print()
# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)



# delete age column
df.drop('keys', axis=1, inplace=True)
# delete marital status column
df.drop(columns='latitude', inplace=True)
# delete height and profession columns
df.drop(['longitude', 'city'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete keys , latitude , longitude , city , column :")
print(df)


#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'province_name': 'province_nameChanged'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'keys': 'keys_Changed', 'name':'name_Changed'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)


#Example: Rename Row Labels
# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)








# calculate the sum of price for each category
grouped = df.groupby('websites')['province'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with unknown
df.fillna('unknown',inplace=True)

print("\nData after filling NaN with 0:\n", df)
# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()













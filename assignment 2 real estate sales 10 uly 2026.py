import pandas as pd
df=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',',parse_dates=[13])
print(df)
print("df-data types", df.dtypes)

print("df.info: ", df.info)


 #display the last three rows
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

 #access the Name column
SaleAmount= df['Sale Amount']
print('access the name of column: df: ')
print(SaleAmount)
print()
# access multiple columns
SaleAmount_SalesRatio= df[['Sale Amount','Sales Ratio']]
print("access multiple columns: df : ")
print(SaleAmount_SalesRatio)
print()
#Using .loc method here
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
second_row4 = df.loc[df['Sale Amount'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()
#Selecting a single column using .loc
second_row5 = df.loc[:1,'Sale Amount']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'Sale Amount':'Sales Ratio']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['Sale Amount'] == 'Gateway Properties','Sales Ratio':'Sale Amount']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here

df_index_col=pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=",",parse_dates=[13],index_col='Serial Number')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
# Second cycle - with index_col as Serial Number
#Selecting a single row using .loc
second_row = df_index_col.loc[2020225]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[2020225, 2020348]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[2020225:2020348]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['Sale Amount'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()


#Selecting a single column using .loc
second_row5 = df_index_col.loc[:2020348,'Sale Amount']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:2020348,['Sale Amount','Sales Ratio']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:2020348,'List Year':'Sale Amount']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['Sale Amount'] == 'Gateway Properties','List Year':'Sale Amount']
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
#pandas dataframe manuplation
df.loc[len(df.index)]= ['Serial Number','List Year', 'Date Recorded','Town','Address','Assessed Value','Sale Amount','Sales Ratio','Property Type','Residential Type','Non Use Code','Assessor Remarks','OPM remarks','Location']
print("Modified DataFrame - add a new row:")
print(df)
print()
#Remove Rows/Columns from a Pandas DataFrame


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
df.drop('Serial Number', axis=1, inplace=True)
# delete marital status column
df.drop(columns='Sales Ratio', inplace=True)
# delete height and profession columns
df.drop(['Town', 'Address'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete Serial Number ,Sales Ratio , Town, Address , column :")
print(df)
#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'Assessed Value': 'Assessed Value_Changed'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'Town': 'Town_Changed', 'Sales Ratio':'Sales Ratio_Changed'}, axis=1, inplace=True)
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





# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='Date Recorded')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'List Year' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['Sale Amount', 'List Year'])

print("Sorting by 'Sale Amount' (ascending) and then by 'List Year' (ascending):\n")
print(df1.to_string(index=False))
grouped = df.groupby('List Year')['Sale Amount'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


#Pandas Data Cleaning
#Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with unknown
df.fillna("Unknown", inplace=True)

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


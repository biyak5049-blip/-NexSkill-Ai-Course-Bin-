import pandas as pd
df= pd.read_csv('startup_growth_investment_data (1).csv',delimiter=',',parse_dates=[8],date_format={'date_added:' '%d-%m-%y'})
print(df)
print('df_data types',df.dtypes)
print('df.info():',df.info())

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

# access the Name column
FundingRounds = df['Funding Rounds']
print("access the Name column: df : ")
print(FundingRounds)
print()
# access multiple columns
Industry_Country=df[['Industry', 'Country']]
print('access multiple column :df:')
print(Industry_Country)
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
second_row4 = df.loc[df['Country'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:1,'Country']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:,['Country','Industry']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()
#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'Country':'Industry']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()


#Combined row and column selection using .loc
second_row8 = df.loc[df['Industry'] == 'Gateway Properties','Country':'Industry']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here

df_index_col=pd.read_csv('startup_growth_investment_data (1).csv',delimiter=',',parse_dates=[8],date_format={'date added:''%d-%m-%y'},index_col='Investment Amount (USD)')



print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())


#Selecting a single row using .loc
second_row = df_index_col.loc[2781498219.93]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[2781498219.93, 3309031930.22]]
print("#Selecting multiple rows using .loc")
print(second_row2)
#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[2781498219.93: 3309031930.22]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['Funding Rounds'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[2781498219.93,'Country']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:2781498219.93,['Country','Industry']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:2781498219.93,'Industry':'Country']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['Country'] == 'Gateway Properties','Industry':'Country']
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

# Case 3 : Using .iloc - ends here

df.loc[len(df.index)]=('Startup Name','Industry','Funding Rounds','Investment Amount (USD)','Valuation (USD)','Number of Investors','Country','Year Founded','Growth Rate (%)')

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
df.drop('Funding Rounds', axis=1, inplace=True)
# delete marital status column
df.drop(columns='Startup Name', inplace=True)
# delete height and profession columns
df.drop(['Industry', 'Country'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete Funding Rounds ,Startup Name, Industry , Country , column :")
print(df)



# rename column 'Name' to 'First_Name'
df.rename(columns= {'Startup Name': 'Startup NameChanged'}, inplace=True)
# rename columns 'Industry' and 'Country'
df.rename(mapper= {'Indusrty': 'Industry_Changed', 'Country':'Country_Changed'}, axis=1, inplace=True)
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


 #sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='Growth Rate (%)')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['Growth Rate (%)', 'Year Founded'])

print("Sorting by 'Growth Rate (%)' (ascending) and then by 'Year Founded' (ascending):\n")
print(df1.to_string(index=False))


grouped = df.groupby('Growth Rate (%)')['Investment Amount (USD)'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with 0
df.fillna(0, inplace=True)

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







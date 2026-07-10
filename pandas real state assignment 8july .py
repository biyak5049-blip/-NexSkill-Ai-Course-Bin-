import pandas as pd
df= pd.read_csv("RealEstate-USA.csv",delimiter=",", parse_dates=[11], date_format={'date_added':'%d-%m-%y'})
print(df)
print("df-data type", df.dtypes)
print("df.info():",df.info())
#display last 3 rows:
print('last three rows:')
print(df.tail(3))
#display last 3 column
print('last three column:')
print(df.head(3))
print()
# summary of  statistic of dataframe using describe method()
print("summary of statistic of dataframe using describe() method",df.describe())
# counting rows and columns of dataframe using shape()
print('counting rows and columns of dataframe using shape(): ',df.shape)
print()
#acess the name column:
bed = df['bed']
print("access the name column: df :")
print(bed) 
print()

#access multiple columns:
bed_bath= df[['bed','bath']]
print("access multiple column: df: ")
print(bed_bath)
print()
#selecting a single row using .loc
second_row= df.loc[1]
print('selecting a single row  using .loc')
print(second_row)
print()
#selecting a multiple row by using.loc
second_row2= df.loc[[1,2]]
print('selecting a multiple rows by using.loc')
print(second_row2)
print()
#selecting a slice of rows by using.loc
second_row3=df.loc[1:4]
print('selecting a slice using.loc')
print(second_row3)
print()
#conditional selection of rows using .loc
second_row4= df.loc[df['price'] == 'Gateway properties']
print('conditional selection of rows using.loc')
print(second_row4)
print()
#selecting a single column using.loc
second_row4=df.loc[:1,['price']]
print('selcting a single column using .loc')
print(second_row4)
print()
#selecting a multiple column by using.loc
second_row4=df.loc[:,['price','bed']]
print('selecting multiple column by using.loc')
print(second_row4)
print()
#selecting a slice of column using .loc
second_row4=df.loc[:1,'price':'bed']
print('selecting a slice of column by using.loc')
print(second_row4)
print()
#combine row and column using .loc
second_row4=df.loc[df['price'] =='Gateway properties','bed':'price']
print('combine row and column using .loc')
print(second_row4)
print()

print("# Case 2 : using .loc with index_col - starts here")
df_index_col=pd.read_csv("RealEstate-USA.csv", delimiter=',', parse_dates=[11], date_format={'date_added': '%d_%m_%y'}, index_col='bed')
print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

#Selecting a single row using .loc
second_row= df_index_col.loc[2]
print('selecting a single row using.loc')
print(second_row)
print()
#selecting multiple rows using .loc
second_row2= df_index_col.loc[[2,4]]
print('#selecting multiple rows using .loc')
print(second_row2)
print()
##selecting slicee rows using .loc
# First, sort the index so Pandas can slice it properly
df_sorted = df_index_col.sort_index()
second_row3 = df_sorted.loc[2:4]
print("Selecting slice rows using .loc (After sorting index):")
print(second_row3)
print()
#conditional selection of rows.loc
second_row3= df_index_col.loc[df_index_col['price'] == 'Gateway properties']
print('conditional selection of rows.loc')
print(second_row3)
print()
# selecting signle column using .loc
second_row5= df_sorted.loc[:2, 'price']
print('selecting single column using.loc')
print(second_row5)
print()
#selecting multiple columns using .loc
second_row4= df_index_col.loc[:, ['price','bath']]
print('select multiple column using .loc')
print(second_row4)
print()
# slice column.loc
second_row4=df_index_col.loc[:,'price':'bath']
print('using slice column.loc')
print(second_row4)
print()
#combine row and column using.loc
second_row4=df_index_col.loc[df_index_col['brokered_by']== 'Gateway properties','status':'street']
print('combining row and column using.loc')
print(second_row4)
print()
#Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here

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
##Selecting a slice of rows using .iloc
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
##Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()
#iloc code ends here
#pandas dataframe manuiplation
df.loc[len(df.index)] = ['brokered_by','status','price','bed','bath','acre_lot','street','city','state','zip_code','house_size','prev_sold_date']

print("Modified DataFrame (Added a New Row):")
print(df)

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
df.drop('brokered_by', axis=1, inplace=True)
# delete marital status column
df.drop(columns='bed', inplace=True)
# delete height and profession columns
df.drop(['bath', 'city'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete brokered_by ,bed, bath , city , column :")
print(df)


#Rename Label in a dataframe
# rename column 'Name' to 'First_Name'
df.rename(columns={'status':'status changed'},inplace=True)
print(df)
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
# select the rows where the price is greater than 10000
df["price"] = pd.to_numeric(df["price"], errors="coerce")

print(df["price"].dtype)
selected_rows = df.query("price > 10000")
print(selected_rows.to_string())
print(len(selected_rows))

#pandas groupby
grouped = df.groupby('prev_sold_date')['price'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))
#cleaning data
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
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()



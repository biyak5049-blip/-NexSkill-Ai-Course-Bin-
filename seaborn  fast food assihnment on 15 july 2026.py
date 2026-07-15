import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FastFoodRestaurants.csv',delimiter=',',  parse_dates=[9],date_format={'date_added:','%d-%m-%y'},index_col='longitude')
print(df.dtypes)
dffilter= df.head(5)
dffilter70= df.head(20)
sns.set(style='darkgrid')
g=sns.displot(data=dffilter, x="city" , y="country" , hue="keys",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=city , y=country, hue=keys,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g=sns.displot(data=dffilter, x="longitude" , y="latitude", kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=longitude , y=latitude, kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g=sns.kdeplot(data=dffilter, x="longitude")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=longitude)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g = sns.histplot(data=dffilter, x='longitude', y='latitude', hue='address', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='longitude', y='price', hue='address', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g = sns.scatterplot(x='latitude', y='longitude', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='latitude', y='longitude', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.lineplot(data=dffilter, x="latitude" , y="longitude"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=latitude , y=longitude  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


sns.set(style='ticks')
g=sns.barplot(data=dffilter, x="latitude", y="longitude", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=latitude, y=longitude, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()



sns.set(style='darkgrid')
sns.set_theme(style="ticks", palette="pastel")
g=sns.boxplot(data=dffilter, x="latitude", y="longitude")
g.figure.suptitle("sns.boxplot(data=df, x=latitude, y=longitude)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()
g=sns.catplot(data=dffilter, x="latitude", y="longitude")
g.figure.suptitle("sns.catplot(data=df, x=latitude, y=longitude)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()
glue = dffilter.pivot(columns="keys", values="latitude")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=keys, values=latitude)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
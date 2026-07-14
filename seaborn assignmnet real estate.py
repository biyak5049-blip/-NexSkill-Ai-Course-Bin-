import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib. pyplot as plt
# sample set



df= pd.read_csv('RealEstate-USA.csv', delimiter=',',parse_dates=[11],date_format={'date_added':'%d-%m-%y'},index_col='bed')
print(df.dtypes)
dffilter= df.head(40)
dffilter100= df.head(100)



sns.set(style='whitegrid')


g=sns.displot(data=dffilter, x="bed" , y="price" , hue="bath",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=bed , y=price , hue=bath,  kind='hist'  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
sns.set(style='darkgrid')

sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'yellow', 'grid.color': 'white'})

g=sns.displot(data=dffilter, x="bed" , y="price" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=bed , y=price, kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
g=sns.kdeplot(data=dffilter, x="bed")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=price)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g = sns.histplot(data=dffilter, x='bed', y='price', hue='bed', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='bed', y='price', hue='bed', multiple=stack)"  )

g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g = sns.scatterplot(x='bed', y='price', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='bed', y='price', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()



g=sns.lineplot(data=dffilter, x="bed" , y="price"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=bed , y=price  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.barplot(data=dffilter, x="bed", y="price", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=bed, y=price, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g=sns.catplot(data=dffilter, x="bed", y="price")
g.figure.suptitle("sns.catplot(data=df, x=bed, y=price)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()
glue = dffilter.pivot(columns= 'street', values="price")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns= street, values=price)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()





















import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib . pyplot as plt

df = pd.read_csv('Real_Estate_Sales_2001-2022_GL-Short.csv',delimiter=',', date_format=[13],index_col='Serial Number')
print(df.dtypes)
dffilter= df.head(20)
dffilter50= df.head(50)
sns.set(style="whitegrid")
sns.set_theme(style='darkgrid', rc={'axes.facecolor': 'grey', 'grid.color': 'white'})

#kind='hist'  
g=sns.displot(data=dffilter, x="Sales Ratio" , y="Sale Amount" , hue="Assessed Value",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Sales Ratio , y=Sale Amount , hue=town,  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
sns.set(style="dark")
g=sns.displot(data=dffilter, x="OPM remarks" , y="Assessed Value" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=List Year, y=Assessed Value, kind='kde'  )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()


g=sns.kdeplot(data=dffilter, x="Sale Amount")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=Sale Amount)"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
g.figure.clear()
g = sns.histplot(data=dffilter, x='Sale Amount', y='Sales Ratio', hue='Assessed Value', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='Sale Amount', y='Sales Ratio', hue='Assessed Value', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g = sns.scatterplot(x='Sale Amount', y='Sales Ratio', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='Sale Amount', y='Sales Ratio', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.lineplot(data=dffilter, x="Sale Amount" , y="Sales Ratio"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=Sale Amount , y= Sales Ratio )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g=sns.barplot(data=dffilter, x="Sale Amount", y="Sales Ratio", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=Sale Amount, y=Sales Ratio, legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()

g=sns.catplot(data=dffilter, x="Sale Amount", y="Sales Ratio")
g.figure.suptitle("sns.catplot(data=df, x=Sale Amount, y=Sales Ratio)"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()




glue = dffilter.pivot(columns="Sale Amount", values="Sales Ratio")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=Sale Amount, values=Sales Ratio)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()






























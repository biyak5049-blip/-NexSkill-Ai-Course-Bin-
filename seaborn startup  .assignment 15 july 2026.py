import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('startup_growth_investment_data (1).csv',delimiter=',',parse_dates=[8],date_format={'date added:''%d-%m-%y'},index_col='Investment Amount (USD)')
print(df.dtypes)
dffilter= df.head(20)
dffilter= df.head(40)
sns.set(style='darkgrid')
#kind='hist'  
g=sns.displot(data=dffilter, x="Industry" , y="Funding Rounds" , hue="Growth Rate (%)",  kind='hist'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Industry , y=Funding Rounds , hue=Growth Rate (%),  kind='hist'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
kind='kde'
g=sns.displot(data=dffilter, x="Funding Rounds" , y="Investment Amount (USD)" , kind='kde'  )
g.figure.suptitle("sns.displot(data=dffilter, x=Funding Rounds , y=Investment Amount (USD) , kind='kde'  )"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")


g=sns.kdeplot(data=dffilter, x="Investment Amount (USD)")
g.figure.suptitle("sns.kdeplot(data=dffilter, x=Investment Amount (USD))"  )

# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g = sns.histplot(data=dffilter, x='Investment Amount (USD)', y='Funding Rounds', hue='Investment Amount (USD)', multiple="stack")
g.figure.suptitle("sns.histplot(data=dffilter, x='Investment Amount (USD)', y='Funding Rounds', hue='Investment Amount (USD)', multiple=stack)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")


g = sns.scatterplot(x='Funding Rounds', y='Investment Amount (USD)', data=dffilter)
g.figure.suptitle("sns.scatterplot(x='Funding Rounds', y='Investment Amount (USD)', data=dffilter)"  )
g.figure.show()
read = input("Wait for me....")


g=sns.lineplot(data=dffilter, x="Investment Amount (USD)" , y="Funding Rounds"  )
g.figure.suptitle("sns.lineplot(data=dffilter, x=Investment Amount (USD) , y=Funding Rounds )"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")

g=sns.barplot(data=dffilter, x="Funding Rounds", y="Investment Amount (USD)", legend=False)
g.figure.suptitle("sns.barplot(data=dffilter, x=Funding Rounds, y=Investment Amount (USD), legend=False)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()
g=sns.catplot(data=dffilter, x="Funding Rounds", y="Investment Amount (USD)")
g.figure.suptitle("sns.catplot(data=df, x=Funding Rounds, y=Investment Amount (USD))"  )
# Display the plot
g.figure.show() 
read = input("Wait for me....")
#g.figure.clear()

glue = dffilter.pivot(columns="Number of Investors", values="Funding Rounds")

g=sns.heatmap(glue)
g.figure.suptitle("sns.heatmap(glue)  - glue = dffilter.pivot(columns=Number of Investors, values=Funding Rounds)"  )
# Display the plot
g.figure.show()
read = input("Wait for me....")
#g.figure.clear()







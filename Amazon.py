import requests
from bs4 import BeautifulSoup
import pandas as pd
with open('week6/Amazon.html', 'r', encoding='utf-8') as file:
    soup1 = BeautifulSoup(file, 'html.parser')
products1 = soup1.select('div[class*="apb-default-slot apb-default-merchandised-search"]')

product_name = []
product_price = []
product_sold = []



for product1 in products1:
    #product Name
    try:
        title_container = product1.select_one('a[href*="#')
        name = title_container.get('title').strip()
    except:
        name = ''

    #product Price
    try:
        price = product1.find('span', class_='ucw-widget-product-card-price').get_text(strip=True).replace('Rs. ', '').replace(',', '')
    except:
        price = ''

    #product Sold
    try:
        sold_tag = product1.select_one("span._1cEkb > span")
        sold_contain = sold_tag.get_text(strip=True)
        sold = sold_contain.replace('.','').replace('K','000').replace(' sold','')
    except:
        sold = ''



    product_name.append(name)
    product_price.append(price)
    product_sold.append(sold)

amazon = pd.DataFrame({
    'Product_Name':product_name,
    'Product_Price':product_price,
    'Product_Sold':product_sold
})

amazon.to_csv('amazon_mobiles_bs4.csv', index=False)
print('Data Saved')
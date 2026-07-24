from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import numpy as np

# ===== SETUP =====
URL = "https://www.amazon.com/s?k=mobile+phones&crid=3O6ORTN1U378Z&sprefix=mobile%2Caps%2C435&ref=nb_sb_ss_p13n-expert-pd-ops-ranker_2_6"
CHROME_PATH = r"C:\\Users\\dell\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# act like real browser (IMPORTANT)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# disable images (faster)
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(CHROME_PATH), options=options)
wait = WebDriverWait(driver, 20)

driver.get(URL)

# ===== CSV SETUP =====
with open("amazon_mobiles.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "product_name", "price",
        "reviews", "rating", "image_link", "product_link"
    ])

    # ===== SCRAPING =====
    for page in range(1, 6):
        print(f"Scraping Page {page}")

        # wait for page load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)

        # scroll for lazy loading
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # ===== DETECT LAYOUT =====
        # use document.querySelectorAll(div.fy26-product-card)
        # to check your selector will work or not
        products = driver.find_elements(By.XPATH, '//div[@data-asin and @data-component-type="s-search-result"]')

        if not products:
            print("Still no products — saving debug...")
            driver.save_screenshot("debug.png")
            print(driver.page_source[:1000])  # preview HTML
            break

        # ===== EXTRACT DATA =====
        for product in products:
            try:
                # product_name
                try:
                    product_name = product.find_element(By.CSS_SELECTOR, "h2 span").text
                    if not product_name:
                        product_name = product.find_element(By.XPATH, ".//h2//span").text
                    # if not product_name:
                    #     product_name = product.find_element(By.TAG_NAME, "h2").text
                except:
                    product_name = np.nan


                # price:
                # <span class="a-offscreen">PKR&nbsp;37,238.13</span>
                try:
                    price = product.find_element(By.XPATH, './/span[contains(@class,"a-offscreen")]').text
                except:
                    price = np.nan


                # reviews
                # <span aria-hidden="true" class="a-size-mini puis-normal-weight-text s-underline-text">(4K)</span>
                try:
                    raw_reviews = product.find_element(By.XPATH, './/span[contains(@class,"a-size-mini")]').text
                    reviews = raw_reviews.replace("(","").replace(")","").strip()

                except:
                    reviews = np.nan

                # rating:
                # <span aria-hidden="true" class="a-size-small a-color-base">4.4</span>
                try:
                    rating = product.find_element(By.XPATH, './/span[contains(@class, "a-size-small")]').text

                except:
                    rating = np.nan

                # image
                try:
                    img = product.find_element(By.CSS_SELECTOR, "img.s-image")
                    image_link = img.get_attribute("src") or img.get_attribute("data-src")
                except:
                    image_link = np.nan

                # link
                try:
                    product_link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
                    if not product_link:
                        product_link = product.find_element(By.XPATH, ".//a//href").text
                        product_link.split('?')[0].strip()

                except:
                    product_link = np.nan

                writer.writerow([product_name, price, reviews, rating, image_link, product_link])

            except Exception as e:
                print("Skipped:", e)

        # ===== NEXT PAGE =====
        try:
            next_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.s-pagination-item"))
            )
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(3)

        except:
            print("No more pages.")
            break

driver.quit()
print(" File saved: amazon_mobiles.csv")
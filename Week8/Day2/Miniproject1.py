from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome()
driver.get('https://www.inmotionhosting.com')
# Extract HTML content and parse with BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
container = soup.find('div', class_='imh-rostrum-container')
plan_names =  container.find_all('h3', class_='imh-rostrum-card-title')
plan_features = container.find_all('div', class_='imh-rostrum-sub-title')
plan_prices = container.find_all('div', class_='imh-rostrum-starting-at-price-discounted')

plan_data = [{'Plan name': plan_name.text.strip(), 'Feature': plan_feature.text.strip(), 'Price': plan_price.text.strip()}
                  for plan_name, plan_feature, plan_price in zip(plan_names, plan_features, plan_prices)]
# Convert to DataFrame and save
df = pd.DataFrame(plan_data)
df.to_csv('inmotion_hosting.csv', index=False)
driver.quit()
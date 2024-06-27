from api import extract_countries, get_data
from database import insert_country

# Step 1 - extracting the data from the API
url = "https://restcountries.com/v3.1/all"
data = get_data(url)
countries_info = extract_countries(data, 10)
print(countries_info)

# Step 2 - storing the data inside the database
for country in countries_info:
    insert_country(country)


# Understanding the data
# Test manually - automise with function (api, database)
# Connect everything inside main.py

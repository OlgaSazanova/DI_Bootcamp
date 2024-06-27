import requests
from typing import Any

# 1. try to understand the data and its structure

# send HTTP Request


def get_data(url: str) -> Any:
    # receice HTTP Response
    # GET - a request used for getting information from an api
    # POST - a request used for performing an action on the api

    # 2xx/200/202 - GOOD
    # 3xx - Redirect
    # 4xx - SOMETHING IS WRONG
    # 5xx - SOMETHING IS WRONG
    response = requests.get(url)
    data = response.json()
    return data


def extract_country_info(country_full_info: dict) -> dict:

    common_name = country_full_info["name"]["common"]  # {'common':"Gambia"}
    capital = country_full_info["capital"][0]  # ["Mata-Utu"]
    flag = country_full_info["flag"]  # 🇼🇫
    subregion = country_full_info["subregion"]  # "Polynesia"
    population = country_full_info["population"]  # 11750

    return {
        "name": common_name,
        "capital": capital,
        "flag": flag,
        "subregion": subregion,
        "population": population,
    }


def extract_countries(data: list[dict], number_of_countries: int) -> list[dict]:
    countries_info_list = []
    for i in range(number_of_countries):
        country_info = extract_country_info(data[i])
        countries_info_list.append(country_info)

    return countries_info_list


def main():
    url = "https://restcountries.com/v3.1/all"
    data = get_data(url)
    countries_info = extract_countries(data, 1)
    print(countries_info)


if __name__ == "__main__":
    main()

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  ## pip install python-dotenv

DBNAME = os.getenv("DBNAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


def insert_country(country_info: dict, table="countries"):
    query = f"insert into {table} (name, capital, flag, subregion, population) values (%s, %s, %s, %s, %s)"

    with psycopg2.connect(
        dbname=DBNAME, user=USER, password=PASSWORD, host=HOST, port=PORT
    ) as connection:

        cursor = connection.cursor()

        cursor.execute(
            query,
            (
                country_info["name"],
                country_info["capital"],
                country_info["flag"],
                country_info["subregion"],
                country_info["population"],
            ),
        )

        connection.commit()


def main():
    country_info = {
        "name": "Wallis and Futuna",
        "capital": "Mata-Utu",
        "flag": "🇼🇫",
        "subregion": "Polynesia",
        "population": 11750,
    }
    insert_country(country_info)


if __name__ == "__main__":
    main()

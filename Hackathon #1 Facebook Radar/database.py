import psycopg2


def create_connection():
    return psycopg2.connect(
        dbname="facebook_radar",
        user="postgres",
        password="0137",
        host="localhost",
        port="5432"
    )

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS reports (
            id SERIAL PRIMARY KEY,
            username VARCHAR NOT NULL,
            topic TEXT NOT NULL,
            link TEXT NOT NULL,
            clicks INTEGER DEFAULT 0,
            report_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """,
    )
    conn = create_connection()
    cursor = conn.cursor()
    try:
        for command in commands:
            cursor.execute(command)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_tables()


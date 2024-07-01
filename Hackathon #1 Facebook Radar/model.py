import psycopg2
from database import create_connection

class Report:
    def __init__(self, username, topic, link):
        self.username = username
        self.topic = topic
        self.link = link

 
    def add_report(username, topic, link):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO reports (username, topic, link) VALUES (%s, %s, %s)",
                (username, topic, link)
            )
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cursor.close()
            conn.close()


    def get_reports():
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM reports")
            reports = cursor.fetchall()
            return reports
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

    def increment_click_count(id):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE reports SET clicks = clicks + 1 WHERE id = %s",
                (id )
            )
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

import psycopg2
from psycopg2 import sql
from database import create_connection

def truncate_table(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        truncate_query = sql.SQL("TRUNCATE TABLE {} RESTART IDENTITY CASCADE;").format(sql.Identifier(table_name))
        cursor.execute(truncate_query)
        conn.commit()
        print(f"Table {table_name} truncated successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error truncating table {table_name}: {error}")
    finally:
        cursor.close()
        conn.close()

def truncate_all_tables():
    tables_to_truncate = ['reports']  # Add more tables if needed
    for table in tables_to_truncate:
        truncate_table(table)
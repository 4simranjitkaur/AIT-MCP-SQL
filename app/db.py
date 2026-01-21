import psycopg2

def get_connection():
    print("get_connection() function reached")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="project1",
            user="postgres",
            password="12345"
        )
        print("PostgreSQL connected successfully")
        return conn
    except Exception as e:
        print("PostgreSQL connection failed")
        print(e)
        return None

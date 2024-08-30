import psycopg2

def list_table_contents():
    try:
        # Establish the database connection
        conn = psycopg2.connect(
            dbname="investment",
            user="postgres",
            password="root",
            host="192.168.178.79",
            port="5432"
        )

        # Create a cursor object
        cur = conn.cursor()

        # List of tables to query
        tables = ['banks', 'accounts', 'account_types', 'taxes', 'transfers']

        for table in tables:
            print(f"\nContents of {table}:")

            # SQL query to select all contents of the table
            cur.execute(f"SELECT * FROM {table};")

            # Fetch all the results
            rows = cur.fetchall()

            # Check if the table has contents
            if rows:
                for row in rows:
                    print(row)
            else:
                print(f"The table {table} is empty.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    list_table_contents()

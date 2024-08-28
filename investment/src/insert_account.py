import psycopg2
from psycopg2 import sql

def insert_account(bank_id, account_number, account_name, account_type_id):
    # Set default values for the other columns
    balance = 100000.00
    account_holder_name = 'me'
    opened_date = '1970-07-01'  # Using the format YYYY-MM-DD
    interest_rate = 0.00
    tax_rate = 0.00

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

        # Define the SQL INSERT query
        insert_query = sql.SQL("""
            INSERT INTO accounts (bank_id, account_number, account_name, balance, account_type_id, account_holder_name, opened_date, interest_rate, tax_rate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING account_id;
        """)

        # Execute the query with the provided and default parameters
        cur.execute(insert_query, (bank_id, account_number, account_name, balance, account_type_id, account_holder_name, opened_date, interest_rate, tax_rate))

        # Commit the transaction
        conn.commit()

        # Fetch the new account_id
        new_account_id = cur.fetchone()[0]
        print(f"Data inserted successfully, new account_id: {new_account_id}")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    # Example usage: Only the essential parameters are passed
    import sys
    insert_account(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

import psycopg2

connection = psycopg2.connect(
    user='',
    password='',
    host='',
    port='5432',
    database='')
cursor = connection.cursor()
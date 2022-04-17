import psycopg2


def connect(database, user, password, host):
    connection = psycopg2.connect(database=database, user=user, password=password, host=host)


if __name__ == '__main__':
    connect("RMS-DB", "postgres", "password5647", "localhost")


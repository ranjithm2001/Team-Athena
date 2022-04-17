import psycopg2


def connect(database, user, password, host):
    return psycopg2.connect(database=database, user=user, password=password, host=host)


def login(username, password):
    cursor = conn.cursor()
    cursor.execute('SELECT password, role, name from users where username = %s', (username,))
    (db_password, role, name) = cursor.fetchone()
    conn.commit()

    if password == db_password:
        print("Log In Successful\nWelcome " + role + " " + name)
        return 1
    else:
        print("Log In Failed. Please Try Again")
        return 0


if __name__ == '__main__':
    conn = connect("RMS-DB", "postgres", "password5647", "localhost")
    log_res = login("cust1", "cust1_pass")
    # print(log_res)




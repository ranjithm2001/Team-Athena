import psycopg2


def connect(database, user, password, host):
    return psycopg2.connect(database=database, user=user, password=password, host=host)


def login(username, password):
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) from users where username = %s', (username,))
    count = cursor.fetchone()[0]
    if not count:
        print("Username does not exist")
        return 0
    cursor.execute('SELECT password, name from users where username = %s', (username,))
    (db_password, name) = cursor.fetchone()
    conn.commit()

    if password == db_password:
        print("Log In Successful\nWelcome" + " " + name)
        return 1
    else:
        print("Log In Failed. Please Try Again")
        return 0


def update_username(old_username, new_username):
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) from users WHERE username = %s', (old_username,))
    count = cursor.fetchone()[0]
    if not count:
        cursor.execute('UPDATE users SET username = %s WHERE username = %s', (new_username, old_username))
        print("Successfully updated username from " + old_username + " to " + new_username)
        conn.commit()
    else:
        print("This username already exists")
        conn.commit()


def update_password(username, new_password):
    cursor = conn.cursor()
    cursor.execute('SELECT password from users WHERE username = %s', (username,))
    old_password = cursor.fetchone()[0]
    cursor.execute('UPDATE users SET password = %s WHERE username = %s', (new_password, username))
    print("Successfully updated password from " + old_password + " to " + new_password)
    conn.commit()


def update_phone(username, new_phone):
    cursor = conn.cursor()
    cursor.execute('SELECT phone from users WHERE username = %s', (username,))
    old_phone = cursor.fetchone()[0]
    cursor.execute('UPDATE users SET phone = %s WHERE username = %s', (new_phone, username))
    print("Successfully updated phone from " + old_phone + " to " + new_phone)
    conn.commit()


def update_address(username, new_address):
    cursor = conn.cursor()
    cursor.execute('SELECT address from users WHERE username = %s', (username,))
    old_address = cursor.fetchone()[0]
    cursor.execute('UPDATE users SET address = %s WHERE username = %s', (new_address, username))
    print("Successfully updated address from " + old_address + " to " + new_address)
    conn.commit()


def update_email(username, new_email):
    cursor = conn.cursor()
    cursor.execute('SELECT email from users WHERE username = %s', (username,))
    old_email = cursor.fetchone()[0]
    cursor.execute('UPDATE users SET email = %s WHERE username = %s', (new_email, username))
    print("Successfully updated email from " + old_email + " to " + new_email)
    conn.commit()


def update_profile(username):
    while True:
        print("Update Options:")
        print("1.Username")
        print("2.Password")
        print("3.Phone")
        print("4.Address")
        print("5.Email")
        print("6.Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            new_username = input("Enter new username: ")
            update_username(username, new_username)
        elif choice == 2:
            new_password = input("Enter new password: ")
            update_password(username, new_password)
        elif choice == 3:
            new_phone = input("Enter new phone: ")
            update_phone(username, new_phone)
        elif choice == 4:
            new_address = input("Enter new address: ")
            update_address(username, new_address)
        elif choice == 5:
            new_email = input("Enter new email: ")
            update_email(username, new_email)
        elif choice == 6:
            print("Exiting..")
            break
        else:
            print("Wrong Choice")


def assign_table(table_no):
    cursor = conn.cursor()
    cursor.execute('SELECT availability from restaurant_table WHERE table_no = %s', (table_no,))
    available = int(cursor.fetchone()[0])

    if available == 1:
        print("This table is available")
        print("Booking the selected table.. please wait")
        cursor.execute('UPDATE restaurant_table SET availability = 0 WHERE table_no = %s', (table_no,))
    else:
        print("Sorry, table is already booked. Please select another table")
    conn.commit()


def view_transactions():
    cursor = conn.cursor()
    cursor.execute("select order_id, amount from order_data where status = 'delivered'")
    transactions = cursor.fetchall()
    conn.commit()
    for i in transactions:
        print("Order Id: " + str(i[0]) + ", Amount: " + i[1])


def deliver_order(order_id):
    cursor = conn.cursor()
    cursor.execute("update order_data set status = 'delivered' where order_id = %s", (order_id,))
    conn.commit()


def receive_order(order_id):
    cursor = conn.cursor()
    cursor.execute("update order_data set status = 'received' where order_id = %s", (order_id,))
    conn.commit()


def cancel_order(order_id):
    cursor = conn.cursor()
    cursor.execute("update order_data set status = 'cancelled' where order_id = %s", (order_id,))
    conn.commit()


def feedback():
    fb = input("Kindly provide your valuable feedback: ")
    cursor = conn.cursor()
    cursor.execute("insert into feedback_data (feedback) values (%s);", (fb,))
    conn.commit()


def update_employee_password(employee_id, new_password):
    cursor = conn.cursor()
    cursor.execute('SELECT password from employee WHERE employee_id = %s', (employee_id,))
    old_password = cursor.fetchone()[0]
    cursor.execute('UPDATE employee SET password = %s WHERE employee_id = %s', (new_password, employee_id))
    print("Successfully updated password from " + old_password + " to " + new_password)
    conn.commit()


def update_employee_phone(employee_id, new_phone):
    cursor = conn.cursor()
    cursor.execute('SELECT phone from employee WHERE employee_id = %s', (employee_id,))
    old_phone = cursor.fetchone()[0]
    cursor.execute('UPDATE employee SET phone = %s WHERE employee_id = %s', (new_phone, employee_id))
    print("Successfully updated phone from " + old_phone + " to " + new_phone)
    conn.commit()


def update_employee_access_type(employee_id, new_role):
    cursor = conn.cursor()
    cursor.execute('SELECT access_type from employee WHERE employee_id = %s', (employee_id,))
    old_role = cursor.fetchone()[0]
    cursor.execute('UPDATE users SET access_type = %s WHERE username = %s', (new_role, employee_id))
    print("Successfully updated role from " + old_role + " to " + new_role)
    conn.commit()


def update_employee_email(employee_id, new_email):
    cursor = conn.cursor()
    cursor.execute('SELECT email from employee WHERE employee_id = %s', (employee_id,))
    old_email = cursor.fetchone()[0]
    cursor.execute('UPDATE employee SET email = %s WHERE employee_id = %s', (new_email, employee_id))
    print("Successfully updated email from " + old_email + " to " + new_email)
    conn.commit()


def update_employee_details(employee_id):
    while True:
        print("Update Options:")
        print("1.Password")
        print("2.Phone")
        print("3.Access Type")
        print("4.Email")
        print("5.Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            new_password = input("Enter new password: ")
            update_employee_password(employee_id, new_password)
        elif choice == 2:
            new_phone = input("Enter new phone: ")
            update_employee_phone(employee_id, new_phone)
        elif choice == 3:
            new_access = input("Enter new role/access: ")
            update_employee_access_type(employee_id, new_access)
        elif choice == 4:
            new_email = input("Enter new email: ")
            update_employee_email(employee_id, new_email)
        elif choice == 5:
            print("Exiting..")
            break
        else:
            print("Wrong Choice")


def view_revenue():
    cursor = conn.cursor()
    cursor.execute('SELECT amount from order_data')
    amount = cursor.fetchall()
    revenue = 0
    for i in amount:
        revenue += int(i[0])
    print(revenue)
    conn.commit()


if __name__ == '__main__':
    conn = connect("RMS-DB", "postgres", "password5647", "localhost")
    # log_res = login("cust1", "cust1_pass")
    # update_username("cust1", "new_cust1")
    view_revenue()
    # print(log_res)

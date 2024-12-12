import flet as ft
import sqlite3
from views.loginView import current_id

#! FINISH the view desing

#! It should allow the user to change their direction/other things and it would automatically update on the sql

def validate_id(id):
    conn = sqlite3.connect("delivery.db")
    cursor = conn.cursor()
    query = "SELECT * FROM Customers WHERE customerID = ?"
    cursor.execute(query, (id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data


def profile_View(router):
    global current_id
    print(current_id)
    if current_id == 0:
        content = ft.Text("No user is currently logged in.", size=30)
        router.update()
        return content
    
    user_data = validate_id(current_id)

    print(user_data)

    if user_data:
        content = ft.Column(
            controls=[
                ft.Text(f"Welcome, {user_data[1]} {user_data[2]}!", size=30),
                ft.Text(f"Email: {user_data[3]}"),
                ft.Text(f"Phone: {user_data[4]}"),
            ]
        )
    else:
        content = ft.Text("User not found.", size=30)
        print("Content created for user not found.")

    router.update()
    print("Router updated after content creation.")
    return content
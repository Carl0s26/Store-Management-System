import flet as ft
import sqlite3


current_id = int()

def validate_user(email, password):
    conn = sqlite3.connect("delivery.db")
    cursor = conn.cursor()
    query = """
    SELECT * FROM Customers 
    WHERE (email = ?) AND password = ?
    """
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    conn.close()
    return result

def login_View(router):
    global current_id


    show_password = False

    def toggle_password_visibility(e):
        nonlocal show_password
        show_password = not show_password
        password_field.password = not show_password
        router.update()

    def submit(e):
        global current_id
        email = email_field.value.strip().lower()
        password = password_field.value.strip()
        
        if not email or not password:
            message.value = "Please fill in all fields."
        else:
            user = validate_user(email, password)
            if user:
                current_id = int(user[0])
                message.value("")
                router.go("/")
            else:
                message.value = "Invalid email or password."
        router.update()

    def signup(e):
        router.go("/signUp")

    #* Defining view content
    email_field = ft.TextField(label="Email", width=300)
    password_field = ft.TextField(label="Password", password=True, width=250)
    message = ft.Text(color=ft.colors.RED)
    eye_button = ft.IconButton(ft.icons.REMOVE_RED_EYE, on_click=toggle_password_visibility)

    content = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text("Shop Name", size=50, weight="bold"),
                padding=ft.padding.only(top=60, bottom=50),
            ),
            ft.Text("Login", size=30),
            email_field,
            ft.Row(
                controls=[password_field, eye_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.ElevatedButton("Submit", on_click=submit),
            message,
            ft.Row(
                controls=[
                    ft.Text("New to shop?"),
                    ft.TextButton("Create an Account", on_click=signup),
                ],alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return content








def validate_id(id):
    conn = sqlite3.connect("delivery.db")
    cursor = conn.cursor()
    query = "SELECT * FROM Customers WHERE customerID = ?"
    cursor.execute(query, (id,))
    user_data = cursor.fetchone()
    conn.close()
    return user_data

def update_customer(id):
    conn = sqlite3.connect("delivery.db")
    cursor = conn.cursor()
    query = """
    UPDATE Customers
    SET firstName = ?, lastName = ?, email = ?, phone = ?, address = ?, birthdate = ?, password = ?
    WHERE customerID = ?
    """
    birthdate = f"{month_dropdown.value} {day_field.value}, {year_field.value}"
    try:
        cursor.execute(query, (
            first_name_field.value.strip(),
            last_name_field.value.strip(),
            email_field.value.strip().lower(),
            phone_field.value.strip(),
            address_field.value.strip(),
            birthdate,
            password_field.value.strip(),
            id
        ))
        conn.commit()
        success = True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        success = False
    finally:
        conn.close()
    
    return success

email_field = ft.TextField(label="Email", width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
password_field = ft.TextField(label="Password", width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
first_name_field = ft.TextField(label="First Name", width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
last_name_field = ft.TextField(label="Last Name", width=300)
phone_field = ft.TextField(label="Phone", width=300)
address_field = ft.TextField(label="Address", width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
month_dropdown = ft.Dropdown(
    label="Month",
    options=[ft.dropdown.Option(month) for month in ["Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]],
    width=150
)
day_field = ft.TextField(label="Day", width=100)
year_field = ft.TextField(label="Year", width=100)
message = ft.Text(color=ft.colors.RED)

def profile_View(router):
    global current_id

    def load_profile():
        user_data = validate_id(current_id)
        if user_data:
            first_name_field.value = user_data[1]
            last_name_field.value = user_data[2]   
            email_field.value = user_data[3].lower()       
            phone_field.value = user_data[4]
            address_field.value = user_data[5]
            birthdate = user_data[6]
            birthdate_parts = birthdate.split(" ")
            if len(birthdate_parts) == 3:
                month_dropdown.value = birthdate_parts[0]
                day_field.value = birthdate_parts[1].strip(",") 
                year_field.value = birthdate_parts[2]
            password_field.value = user_data[8]
        router.update()

    def save_changes(e):
        
        if month_dropdown.value != "Month":
            try:
                day = int(day_field.value) if day_field.value else None
                year = int(year_field.value) if year_field.value else None
                
                if (day is not None and (day < 1 or day > 31)) or (year is not None and (year <= 0 or year < 1924 or year > 2023)):
                    raise ValueError
            except ValueError:
                message.value = "Input a reasonable date."
                router.update()
                return
        
        if update_customer(current_id):
            message.value = "Profile updated successfully!"
        else:
            message.value = "Failed to update profile."
        router.update()

    load_profile()

    content = ft.Column(
        controls=[
            first_name_field,
            last_name_field,
            email_field,
            phone_field,
            address_field,
            ft.Text("Birthdate", size = 30),
            ft.Row(
                controls=[month_dropdown, day_field, year_field],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            password_field,
            ft.ElevatedButton("Save Changes", on_click=save_changes),
            message,
            ft.ElevatedButton("Sign Out", on_click=lambda _: router.go('/login')),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return content
import flet as ft
import sqlite3

def create_customer(firstName, lastName, email, phone, address, birthdate, password):
    conn = sqlite3.connect("delivery.db")
    cursor = conn.cursor()
    query = """
    INSERT INTO Customers (firstName, lastName, email, phone, address, birthdate, password)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(query, (firstName, lastName, email, phone, address, birthdate, password))
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False
    finally:
        conn.close()
    
    return success

def signUp_View(router):
    def submit(e):
        firstName = first_name_field.value.strip()
        lastName = last_name_field.value.strip()
        email = email_field.value.strip().lower()
        phone = phone_field.value.strip()
        address = address_field.value.strip()
        birthdate = f"{month_dropdown.value} {day_field.value}, {year_field.value}"
        password = password_field.value.strip()
        confirm_password = confirm_password_field.value.strip()
    
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

            birthdate = f"{month_dropdown.value} {day if day else ''}, {year if year else ''}"
        else:
            birthdate = None



        if not all([firstName, email, address, password, confirm_password]):
            message.value = "Please fill in all fields."
        elif password != confirm_password:
            message.value = "Passwords do not match."
        else:
            if create_customer(firstName, lastName, email, phone, address, birthdate, password):
                message.value("")
                router.go("/")
        router.update()

    # Form fields
    first_name_field = ft.TextField(label="First Name", width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
    last_name_field = ft.TextField(label="Last Name", width=300)
    email_field = ft.TextField(label="Email", width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
    phone_field = ft.TextField(label="Phone Number", width=300)
    address_field = ft.TextField(label="Address", width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))

    month_dropdown = ft.Dropdown(
        label="Month",
        options=[ft.dropdown.Option(month) for month in ["Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]],
        width=150
    )


    
    day_field = ft.TextField(label="Day", width=100)
    year_field = ft.TextField(label="Year", width=100)

    password_field = ft.TextField(label="Password", password=True, width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
    confirm_password_field = ft.TextField(label="Confirm Password", password=True, width=300, suffix_text="*", suffix_style=ft.TextStyle(color=ft.colors.RED))
    message = ft.Text(color=ft.colors.RED)

    content = ft.Column(
        controls=[
            ft.Text("Sign Up", size=30, weight="bold"),
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
            confirm_password_field,
            ft.ElevatedButton("Submit", on_click=submit),
            message,
            ft.Row(
                controls=[
                    ft.Text("Already have an account?"),
                    ft.TextButton("Login", on_click=lambda _: router.go("/login")),
                ], alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return content

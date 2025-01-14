import flet as ft
import requests
import base64

API_URL = "http://127.0.0.1:8000" 

def add_View(router):
    you_data = ft.Column()
    preview = ft.Image(visible=False, width=100, height=100, fit="contain") # type: ignore
    txt_name = ft.TextField(label="Item name:", width=500, visible= False)
    txt_price = ft.TextField(label="Price:", width=500, visible= False)
    txt_stock = ft.TextField(label="Stock:", width=500, visible= False)
    txt_description = ft.TextField(label="Description:", width=500, visible= False)
    save = ft.ElevatedButton("Save", icon=ft.icons.SAVE, disabled=True)
    convertImgToString = ''

    def propers(e):
        nonlocal convertImgToString
        if table.value == 'Game':
            txt_description.visible = categories.visible = rating.visible = txt_name.visible = txt_price.visible = txt_stock.visible = True
        else:
            txt_description.visible = categories.visible = rating.visible = False
            txt_name.visible = txt_price.visible = txt_stock.visible = True
        router.update()
        
    table = ft.Dropdown(
        options=[
            ft.dropdown.Option("Drink"),
            ft.dropdown.Option("Game"),
        ],
        label="Choose a table",
        width=500,
        on_change=propers,
    )

    categories = ft.Dropdown(
        options=[
            ft.dropdown.Option("Action"),
            ft.dropdown.Option("Platformer"),
            ft.dropdown.Option("Fighting"),
            ft.dropdown.Option("Shooter"),
            ft.dropdown.Option("Beat 'em Up"),
            ft.dropdown.Option("Hack-and-Slash"),
            ft.dropdown.Option("Adventure"),
            ft.dropdown.Option("Open World"),
            ft.dropdown.Option("Narrative-Driven"),
            ft.dropdown.Option("Metroidvania"),
            ft.dropdown.Option("RPG"),
            ft.dropdown.Option("Action RPG"),
            ft.dropdown.Option("Turn-Based RPG"),
            ft.dropdown.Option("Tactical RPG"),
            ft.dropdown.Option("MMORPG"),
            ft.dropdown.Option("Dungeon Crawler"),
            ft.dropdown.Option("Simulation"),
            ft.dropdown.Option("Life Simulation"),
            ft.dropdown.Option("Vehicle Simulation"),
            ft.dropdown.Option("Management/Building Simulation"),
            ft.dropdown.Option("Strategy"),
            ft.dropdown.Option("Real-Time Strategy"),
            ft.dropdown.Option("Turn-Based Strategy"),
            ft.dropdown.Option("Tower Defense"),
            ft.dropdown.Option("Sports"),
            ft.dropdown.Option("Racing"),
            ft.dropdown.Option("Horror"),
            ft.dropdown.Option("Survival Horror"),
            ft.dropdown.Option("Psychological Horror"),
            ft.dropdown.Option("Puzzle"),
            ft.dropdown.Option("Logic Puzzle"),
            ft.dropdown.Option("Physics-Based Puzzle"),
            ft.dropdown.Option("Casual"),
            ft.dropdown.Option("Party Games"),
            ft.dropdown.Option("Idle Games"),
            ft.dropdown.Option("Sandbox"),
            ft.dropdown.Option("Rhythm/Music"),
            ft.dropdown.Option("Roguelike/Roguelite"),
            ft.dropdown.Option("Stealth"),
            ft.dropdown.Option("Visual Novels"),
        ],
        label="Choose a category",
        width=500,
        visible = False
    )

    rating = ft.Dropdown(
        options=[
            ft.dropdown.Option("E - Everyone"),
            ft.dropdown.Option("E10+ - Everyone 10 and older"),
            ft.dropdown.Option("T - Teen"),
            ft.dropdown.Option("M - Mature 17+"),
            ft.dropdown.Option("AO - Adults Only 18+"),
            ft.dropdown.Option("RP - Rating Pending"),
        ],
        label="Choose a rating",
        width=500,
        visible= False
    )


    def check(e):
        nonlocal convertImgToString
        if all([txt_name.value, txt_price.value, txt_stock.value, convertImgToString]):
            if table.value == 'Game':
                if all([categories.value, txt_description.value, rating.value]):
                    save.disabled = False
            else:
                save.disabled = False
        else:
            save.disabled = True
        router.update()


    def upload_now(e: ft.FilePickerResultEvent):
        nonlocal convertImgToString
        if e.files:
            for x in e.files:  # type: ignore
                try:
                    with open(x.path, "rb") as image_file:
                        convertImgToString = base64.b64encode(image_file.read()).decode()
                        preview.visible = True
                        preview.src_base64=convertImgToString
                        print(convertImgToString)
                except Exception as e:  # type: ignore
                    print(f"Error: {e}")
        check(e)
        router.update()
            
    def confirm(e):
        nonlocal convertImgToString
        data = {
            "name": txt_name.value,
            "price": txt_price.value,
            "stock": txt_stock.value,
            "image": convertImgToString
        }

        if table.value == 'Game':
            data.update({
                "description": txt_description.value,
                "category": categories.value,
                "rating": rating.value
            })
            response = requests.post(f"{API_URL}/games", json=data)
        else:
            response = requests.post(f"{API_URL}/drinks", json=data)

        if response.status_code == 201:
            print("Item successfully added!")
        else:
            print("Error adding item:", response.text)

        table.value = txt_name.value = txt_description.value = categories.value = rating.value = txt_price.value = convertImgToString = txt_stock.value = ''
        preview.visible = False
        save.disabled = True
        router.update()

    file_picker = ft.FilePicker(on_result=upload_now)

    txt_description.on_change = txt_name.on_change = txt_price.on_change = txt_stock.on_change = categories.on_change = rating.on_change = check
    save.on_click = confirm

    content = ft.Column([
        ft.Text("Item Stocker", size=30),
        table,
        txt_name,
        txt_stock,
        txt_description,
        categories,
        rating,
        txt_price,
        ft.Row([ft.FilledButton("Upload Image",icon=ft.icons.FILE_UPLOAD_OUTLINED, on_click=lambda e: file_picker.pick_files()), 
            save,
            preview,
            ]),
        you_data,
        file_picker,
    ])
    
    return content

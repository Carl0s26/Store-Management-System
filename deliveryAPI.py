from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import sqlite3
from sqlite3 import IntegrityError
import uvicorn

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect("delivery.db")
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer_Game_Record (
            GameID INTEGER NOT NULL REFERENCES Games(gameID),
            CustomerID INTEGER NOT NULL REFERENCES Customers(customerID)
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customer_Pizza_Record (
                PizzaID INTEGER NOT NULL REFERENCES Pizzas(PizzaID),
                CustomerID INTEGER NOT NULL REFERENCES Customers(customerID)
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers (
                customerID INTEGER NOT NULL UNIQUE PRIMARY KEY,
                firstName TEXT,
                lastName TEXT,
                email TEXT,
                phone TEXT,
                address TEXT,
                birthdate TEXT,
                subscription TEXT
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Drinks (
                drinkID INTEGER NOT NULL PRIMARY KEY,
                name TEXT,
                stock INTEGER,
                image TEXT,
                price NUMERIC
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Games (
                gameID INTEGER NOT NULL PRIMARY KEY,
                name TEXT,
                description TEXT,
                category TEXT,
                rating TEXT,
                image TEXT,
                price NUMERIC,
                stock INTEGER
            )
        ''')
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pizzas (
                PizzaID INTEGER NOT NULL UNIQUE PRIMARY KEY,
                crust TEXT,
                size TEXT,
                sauce TEXT
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ingredients (
                ingredientID INTEGER NOT NULL UNIQUE PRIMARY KEY,
                name TEXT,
                stock TEXT
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customer_Game_Record (
                PizzaID INTEGER REFERENCES Pizzas(PizzaID),
                ingredientID INTEGER REFERENCES Ingredients(ingredientID)
            )
        ''')
    
    conn.commit()
    return conn



games_db = []

class Game(BaseModel):

    gameID: int 
    name: str
    description: str
    category: str
    rating: str
    image: str
    price: float
    stock: int

@app.post("/games/", status_code=201)
async def create_game(game: Game):
    if any(existing_game.gameID == game.gameID for existing_game in games_db):
        raise HTTPException(status_code=409, detail="Game ID already exists")
    else:
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Games (gameID, name, description, category, rating, image, price, stock) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (game.gameID, game.name, game.description, game.category, game.rating, 
                  game.image, game.price, game.stock))
            conn.commit()
        except IntegrityError:
            conn.close()
            raise HTTPException(status_code=409, detail="Game ID already exists")
        conn.close()
        return {"message": "Game added successfully"}

@app.get("/games/")
async def get_games(gameID: int = Query(None, description="ID of the game to search for")):
    conn = get_db_connection()
    cursor = conn.cursor()
    if gameID:
        cursor.execute("SELECT * FROM Games WHERE id = ?", (gameID,))
    else:
        cursor.execute("SELECT * FROM Games")
    
    rows = cursor.fetchall()
    conn.close()
    games = [dict(row) for row in rows]
    
    if not games:
        raise HTTPException(status_code=404, detail="Game ID not found")
    return games

@app.put("/games/{gameID}")
async def update_game(gameID: int, updated_game: Game):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE Games SET name = ?, description = ?, category = ?, rating = ?, image = ?, price = ?, stock = ? WHERE gameID = ?
    ''', (updated_game.name, updated_game.description, updated_game.category, updated_game.rating, updated_game.image, updated_game.price, updated_game.stock, updated_game.gameID))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Game not found")
    
    conn.commit()
    conn.close()
    return {"message": "Game updated successfully"}

@app.delete("/games/{gameID}", status_code=204)
async def delete_game(gameID: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Games WHERE gameID = ?", (gameID,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Game not found")
    
    conn.commit()
    conn.close()





drinks_db = []

class Drink(BaseModel):
    drinkID: int
    name: str
    stock: int
    image: str
    price: float

@app.post("/drinks/", status_code=201)
async def create_drink(drink: Drink):
    if any(existing_drink.drinkID == drink.drinkID for existing_drink in drinks_db):
        raise HTTPException(status_code=409, detail="Game ID already exists")
    else:
        conn = get_db_connection()
        cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Drinks (drinkID, name, stock, image, price) VALUES (?, ?, ?, ?, ?)
        ''', (drink.drinkID, drink.name, drink.stock, drink.image, drink.price))
        conn.commit()
    except IntegrityError:
        conn.close()
        raise HTTPException(status_code=409, detail="Drink ID already exists")
    
    conn.close()
    return {"message": "Drink added successfully"}

@app.get("/drinks/")
async def get_drinks(drinkID: int = Query(None, description="ID of the drink to search for")):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if drinkID:
        cursor.execute("SELECT * FROM Drinks WHERE drinkID = ?", (drinkID,))
    else:
        cursor.execute("SELECT * FROM Drinks")
    
    rows = cursor.fetchall()
    conn.close()
    
    drinks = [dict(row) for row in rows]
    if not drinks:
        raise HTTPException(status_code=404, detail="Drink not found")
    
    return drinks

@app.put("/drinks/{drinkID}")
async def update_drink(drinkID: int, updated_drink: Drink):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE Drinks SET name = ?, stock = ?, image = ?, price = ? WHERE drinkID = ?
    ''', (updated_drink.name, updated_drink.stock, updated_drink.image, updated_drink.price, drinkID))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Drink not found")
    
    conn.commit()
    conn.close()
    return {"message": "Drink updated successfully"}

@app.delete("/drinks/{drinkID}", status_code=204)
async def delete_drink(drinkID: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Drinks WHERE drinkID = ?", (drinkID,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Drink not found")
    
    conn.commit()
    conn.close()





pizzas_db = []

class Pizza(BaseModel):
    PizzaID: int
    crust: str
    size: str
    sauce: str

@app.post("/pizzas/", status_code=201)
async def create_pizza(pizza: Pizza):
    if any(existing_pizza.PizzaID == pizza.PizzaID for existing_pizza in pizzas_db):
        raise HTTPException(status_code=409, detail="Pizza ID already exists")
    else:
        conn = get_db_connection()
        cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Pizzas (PizzaID, crust, size, sauce) VALUES (?, ?, ?, ?)
        ''', (pizza.PizzaID, pizza.crust, pizza.size, pizza.sauce))
        conn.commit()
    except IntegrityError:
        conn.close()
        raise HTTPException(status_code=409, detail="Pizza ID already exists")
    
    conn.close()
    return {"message": "Pizza added successfully"}

@app.get("/pizzas/")
async def get_pizzas(PizzaID: int = Query(None, description="ID of the pizza to search for")):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if PizzaID:
        cursor.execute("SELECT * FROM Pizzas WHERE PizzaID = ?", (PizzaID,))
    else:
        cursor.execute("SELECT * FROM Pizzas")
    
    rows = cursor.fetchall()
    conn.close()
    
    pizzas = [dict(row) for row in rows]
    if not pizzas:
        raise HTTPException(status_code=404, detail="Pizza not found")
    
    return pizzas

@app.put("/pizzas/{PizzaID}")
async def update_pizza(PizzaID: int, updated_pizza: Pizza):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE Pizzas SET crust = ?, size = ?, sauce = ? WHERE PizzaID = ?
    ''', (updated_pizza.crust, updated_pizza.size, updated_pizza.sauce, PizzaID))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Pizza not found")
    
    conn.commit()
    conn.close()
    return {"message": "Pizza updated successfully"}

@app.delete("/pizzas/{PizzaID}", status_code=204)
async def delete_pizza(PizzaID: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pizzas WHERE PizzaID = ?", (PizzaID,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Pizza not found")
    
    conn.commit()
    conn.close()





customers_db = []

class Customer(BaseModel):
    customerID: int
    firstName: str
    lastName: str
    email: str
    phone: str
    address: str
    birthdate: str
    subscription: str

@app.post("/customers/", status_code=201)
async def create_customer(customer: Customer):
    if any(existing_customer.customerID == customer.customerID for existing_customer in customers_db):
        raise HTTPException(status_code=409, detail="Customer ID already exists")
    else:
        conn = get_db_connection()
        cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Customers (customerID, firstName, lastName, email, phone, address, birthdate, subscription) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (customer.customerID, customer.firstName, customer.lastName, customer.email, 
              customer.phone, customer.address, customer.birthdate, customer.subscription))
        conn.commit()
    except IntegrityError:
        conn.close()
        raise HTTPException(status_code=409, detail="Customer ID already exists")
    
    conn.close()
    return {"message": "Customer added successfully"}

@app.get("/customers/")
async def get_customers(customerID: int = Query(None, description="ID of the customer to search for")):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if customerID:
        cursor.execute("SELECT * FROM Customers WHERE customerID = ?", (customerID,))
    else:
        cursor.execute("SELECT * FROM Customers")
    
    rows = cursor.fetchall()
    conn.close()
    
    customers = [dict(row) for row in rows]
    if not customers:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    return customers

@app.put("/customers/{customerID}")
async def update_customer(customerID: int, updated_customer: Customer):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE Customers SET firstName = ?, lastName = ?, email = ?, phone = ?, 
        address = ?, birthdate = ?, subscription = ? WHERE customerID = ?
    ''', (updated_customer.firstName, updated_customer.lastName, updated_customer.email, 
          updated_customer.phone, updated_customer.address, updated_customer.birthdate, 
          updated_customer.subscription, customerID))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    
    conn.commit()
    conn.close()
    return {"message": "Customer updated successfully"}

@app.delete("/customers/{customerID}", status_code=204)
async def delete_customer(customerID: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Customers WHERE customerID = ?", (customerID,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    
    conn.commit()
    conn.close()





ingredients_db = []

class Ingredient(BaseModel):
    ingredientID: int
    name: str
    stock: str

@app.post("/ingredients/", status_code=201)
async def create_ingredient(ingredient: Ingredient):
    if any(existing_ingredient.ingredientID == ingredient.ingredientID for existing_ingredient in ingredients_db):
        raise HTTPException(status_code=409, detail="Ingredient ID already exists")
    else:
        conn = get_db_connection()
        cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO Ingredients (ingredientID, name, stock) VALUES (?, ?, ?)
        ''', (ingredient.ingredientID, ingredient.name, ingredient.stock))
        conn.commit()
    except IntegrityError:
        conn.close()
        raise HTTPException(status_code=409, detail="Ingredient ID already exists")
    
    conn.close()
    return {"message": "Ingredient added successfully"}

@app.get("/ingredients/")
async def get_ingredients(ingredientID: int = Query(None, description="ID of the ingredient to search for")):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if ingredientID:
        cursor.execute("SELECT * FROM Ingredients WHERE ingredientID = ?", (ingredientID,))
    else:
        cursor.execute("SELECT * FROM Ingredients")
    
    rows = cursor.fetchall()
    conn.close()
    
    ingredients = [dict(row) for row in rows]
    if not ingredients:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return ingredients

@app.put("/ingredients/{ingredientID}")
async def update_ingredient(ingredientID: int, updated_ingredient: Ingredient):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE Ingredients SET name = ?, stock = ? WHERE ingredientID = ?
    ''', (updated_ingredient.name, updated_ingredient.stock, ingredientID))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    conn.commit()
    conn.close()
    return {"message": "Ingredient updated successfully"}

@app.delete("/ingredients/{ingredientID}", status_code=204)
async def delete_ingredient(ingredientID: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Ingredients WHERE ingredientID = ?", (ingredientID,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    conn.commit()
    conn.close()



#! uvicorn "Store-Management-System.deliveryApi:app" --reload

def run_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)
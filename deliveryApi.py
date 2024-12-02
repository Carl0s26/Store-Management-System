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
            rating INTEGER,
            image TEXT,
            price NUMERIC,
            stock INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pizzas (
            PizzaID INTEGER NOT NULL PRIMARY KEY,
            crust TEXT,
            size TEXT,
            sauce TEXT,
            ingredients TEXT
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
    rating: int
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



# @app.put("/games/{gameID}")
# async def update_game(gameID: int, updated_block: Block):
#     conn = get_db_connection()
#     cursor = conn.cursor()
    
#     cursor.execute('''
#         UPDATE blocks SET name = ?, description = ? WHERE id = ?
#     ''', (updated_block.name, updated_block.description, updated_block.block_id))
    
#     if cursor.rowcount == 0:
#         conn.close()
#         raise HTTPException(status_code=404, detail="Block not found")
    
#     conn.commit()
#     conn.close()
#     return {"message": "Block updated successfully"}




# @app.delete("/blocks/{block_id}", status_code=204)
# async def delete_block(block_id: int):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM blocks WHERE id = ?", (block_id,))
    
#     if cursor.rowcount == 0:
#         conn.close()
#         raise HTTPException(status_code=404, detail="Block not found")
    
#     conn.commit()
#     conn.close()



#! uvicorn "Store-Management-System.deliveryApi:app" --reload

def run_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)
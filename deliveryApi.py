from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import sqlite3
from sqlite3 import IntegrityError

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect("delivery.db")
    conn.row_factory = sqlite3.Row  
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer-Game Record (
            GameID INTEGER NOT NULL REFERENCES Games(gameID),
            CustomerID INTEGER NOT NULL REFERENCES Customers(customerID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Customer-Pizza Record (
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
            Subscription TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS liquids (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            speed FLOAT NOT NULL,
            description TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            height INTEGER NOT NULL,
            length INTEGER NOT NULL,
            description TEXT
        )
    ''')
    
    conn.commit()
    return conn

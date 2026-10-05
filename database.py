import sqlite3
from datetime import datetime


DB_NAME = "decisions.db"


def create_database():

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            category TEXT,
            price REAL,
            score REAL,
            performance_weight INTEGER,
            battery_weight INTEGER,
            portability_weight INTEGER,
            gaming_weight INTEGER,
            created_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_decision(
    product,
    category,
    price,
    score,
    performance_weight,
    battery_weight,
    portability_weight,
    gaming_weight
):

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO decisions (
            product,
            category,
            price,
            score,
            performance_weight,
            battery_weight,
            portability_weight,
            gaming_weight,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product,
        category,
        price,
        score,
        performance_weight,
        battery_weight,
        portability_weight,
        gaming_weight,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_decisions():

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            product,
            category,
            price,
            score,
            created_at
        FROM decisions
        ORDER BY id DESC
    """)

    decisions = cursor.fetchall()

    connection.close()

    return decisions
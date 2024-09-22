# The sqlite3 provides an SQL interface
import sqlite3

# Initialize or create the database
def initialize_database():
    # Connect to SQLite database (if it doesn't exist, it will create it)
    conn = sqlite3.connect('recipes.db') # Connection to the database.
    cursor = conn.cursor() # An object used to execute SQL commands and retrieve results from the database.

    # Create recipes table
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        ingredients TEXT NOT NULL,
                        instructions TEXT NOT NULL,
                        date_added DATE DEFAULT (datetime('now'))
                    )''')

    # Create categories table
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )''')

    # Create a relationship between recipes and categories
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipe_categories (
                        recipe_id INTEGER,
                        category_id INTEGER,
                        FOREIGN KEY (recipe_id) REFERENCES recipes(id),
                        FOREIGN KEY (category_id) REFERENCES categories(id)
                    )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()
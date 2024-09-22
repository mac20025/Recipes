# The sqlite3 provides an SQL interface
import sqlite3

# Insert recipes to the database
def insert_recipe(name, ingredients, instructions, category_id):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (name, ingredients, instructions) VALUES (?, ?, ?)", (name, ingredients, instructions))
    
    recipe_id = cursor.lastrowid  # Get the last inserted recipe ID
    cursor.execute("INSERT INTO recipe_categories (recipe_id, category_id) VALUES (?, ?)", (recipe_id, category_id))
    
    conn.commit()
    conn.close()

# Modify recipes in the database
def modify_recipe(recipe_id, name=None, ingredients=None, instructions=None):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    if name:
        cursor.execute("UPDATE recipes SET name = ? WHERE id = ?", (name, recipe_id))
    if ingredients:
        cursor.execute("UPDATE recipes SET ingredients = ? WHERE id = ?", (ingredients, recipe_id))
    if instructions:
        cursor.execute("UPDATE recipes SET instructions = ? WHERE id = ?", (instructions, recipe_id))

    conn.commit()
    conn.close()

# Delete recipes from the database
def delete_recipe(recipe_id):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM recipe_categories WHERE recipe_id = ?", (recipe_id,))
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    
    conn.commit()
    conn.close()

# Retrieve all recipes from the database
def retrieve_recipes():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT recipes.id, recipes.name, recipes.ingredients, recipes.instructions, recipes.date_added, categories.name as category
                      FROM recipes
                      JOIN recipe_categories ON recipes.id = recipe_categories.recipe_id
                      JOIN categories ON recipe_categories.category_id = categories.id''')

    recipes = cursor.fetchall()

    for recipe in recipes:
        print(f"Recipe ID: {recipe[0]}")
        print(f"Name: {recipe[1]}")
        print(f"Ingredients: {recipe[2]}")
        print(f"Instructions: {recipe[3]}")
        print(f"Date Added: {recipe[4]}")
        print(f"Category: {recipe[5]}")
        print("----------------------------")
    
    conn.close()

# Retrieve recipes by name
def retrieve_recipes_by_name(recipe_name):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT recipes.id, recipes.name, recipes.ingredients, recipes.instructions, recipes.date_added, categories.name as category
                      FROM recipes
                      JOIN recipe_categories ON recipes.id = recipe_categories.recipe_id
                      JOIN categories ON recipe_categories.category_id = categories.id
                      WHERE recipes.name LIKE ?''', ('%' + recipe_name + '%',))
    
    recipes = cursor.fetchall()
    conn.close()
    
    return recipes

# Retrieve recipes by ingredients
def retrieve_recipes_by_ingredients(ingredient):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT recipes.id, recipes.name, recipes.ingredients, recipes.instructions, recipes.date_added, categories.name as category
                      FROM recipes
                      JOIN recipe_categories ON recipes.id = recipe_categories.recipe_id
                      JOIN categories ON recipe_categories.category_id = categories.id
                      WHERE recipes.ingredients LIKE ?''', ('%' + ingredient + '%',))
    
    recipes = cursor.fetchall()
    conn.close()
    
    return recipes

# Retrieve recipes by category
def retrieve_recipes_by_category(category_name):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT recipes.id, recipes.name, recipes.ingredients, recipes.instructions, recipes.date_added, categories.name as category
                      FROM recipes
                      JOIN recipe_categories ON recipes.id = recipe_categories.recipe_id
                      JOIN categories ON recipe_categories.category_id = categories.id
                      WHERE categories.name LIKE ?''', ('%' + category_name + '%',))
    
    recipes = cursor.fetchall()
    conn.close()
    
    return recipes

# Insert category to the database
def insert_category(category_name):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO categories (name) VALUES (?)", (category_name,))
    
    conn.commit()
    conn.close()

# Display recipes filtered by "retrieve_recipes_by" functions
def display_recipes(recipes):
    if recipes:
        for recipe in recipes:
            print(f"Recipe ID: {recipe[0]}")
            print(f"Name: {recipe[1]}")
            print(f"Ingredients: {recipe[2]}")
            print(f"Instructions: {recipe[3]}")
            print(f"Date Added: {recipe[4]}")
            print(f"Category: {recipe[5]}")
            print("----------------------------")
    else:
        print("No recipes found.")

# Display menu options
def main_menu():
    print("\nRecipe Database Application")
    print("1. Insert a new recipe")
    print("2. Modify a recipe")
    print("3. Delete a recipe")
    print("4. Retrieve all recipes")
    print("5. Insert a new category")
    print("6. Search recipes by name")
    print("7. Search recipes by ingredient")
    print("8. Search recipes by category")
    print("9. Exit")
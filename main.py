#Import functions from db_operations file
from db_operations import (insert_recipe, modify_recipe, delete_recipe, retrieve_recipes, 
                           insert_category, retrieve_recipes_by_name, retrieve_recipes_by_ingredients,
                           retrieve_recipes_by_category, display_recipes, main_menu)

#Import functions from initialize_db file
from initialize_db import (initialize_database)

# Main function to run the program
def main():
    # Create or connect to the database
    initialize_database()

    # While the user don't choose Exit, it keeps displaying the menu
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients: ")
            instructions = input("Enter instructions: ")
            category_id = int(input("Enter category ID: "))
            insert_recipe(name, ingredients, instructions, category_id)
            print("Recipe added successfully!")

        elif choice == "2":
            recipe_id = int(input("Enter recipe ID to modify: "))
            name = input("Enter new name (or leave blank): ")
            ingredients = input("Enter new ingredients (or leave blank): ")
            instructions = input("Enter new instructions (or leave blank): ")
            modify_recipe(recipe_id, name, ingredients, instructions)
            print("Recipe modified successfully!")

        elif choice == "3":
            recipe_id = int(input("Enter recipe ID to delete: "))
            delete_recipe(recipe_id)
            print("Recipe deleted successfully!")

        elif choice == "4":
            retrieve_recipes()

        elif choice == "5":
            category_name = input("Enter new category name: ")
            insert_category(category_name)
            print("Category added successfully!")

        elif choice == "6":
            recipe_name = input("Enter the recipe name to search: ")
            recipes = retrieve_recipes_by_name(recipe_name)
            display_recipes(recipes)

        elif choice == "7":
            ingredient = input("Enter the ingredient to search: ")
            recipes = retrieve_recipes_by_ingredients(ingredient)
            display_recipes(recipes)

        elif choice == "8":
            category_name = input("Enter the category to search: ")
            recipes = retrieve_recipes_by_category(category_name)
            display_recipes(recipes)

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
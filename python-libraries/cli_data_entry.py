from rich.console import Console
from rich.table import Table
import json
import os

console = Console()

console.print("Here is some example food data:", style="bold cyan")

table = Table(title="Food Dataset")
table.add_column("Food")
table.add_column("Cuisine")
table.add_column("Location")

table.add_row("Paneer Butter Masala", "Indian", "Delhi")
table.add_row("Pizza", "Italian", "Naples")
table.add_row("Sushi", "Japanese", "Tokyo")

console.print(table)

console.print("\nNow enter your own food data:\n")

file_name = "food_data.json"
entries = []

while True:

    food = input("Food name: ")
    cuisine = input("Cuisine: ")
    location = input("Location: ")

    console.print(f"\nYou entered: {food}, {cuisine}, {location}")

    confirm = input("Is this correct? (y/n): ")

    if confirm == "y":
        entry = {
            "food": food,
            "cuisine": cuisine,
            "location": location
        }

        entries.append(entry)

        # save after confirmation
        with open(file_name, "w") as f:
            json.dump(entries, f, indent=4)

        console.print("Entry saved.", style="green")

    else:
        console.print("Please re-enter.", style="red")
        continue

    again = input("Add another entry? (y/n): ")
    if again != "y":
        break

console.print("Data saved to:", os.path.abspath(file_name))
# CLI Food Data Entry Script

This Python script allows users to enter food-related cultural data through the command line and saves the confirmed entries to a JSON file.

## What the script does

* Displays example food data using the Rich library
* Prompts the user to enter new food entries
* Shows the entered data and asks for confirmation
* Saves confirmed entries to food_data.json
* Prints the file path so the user can locate the saved data

## How to run the script

From the repository folder:

```
python3 python-libraries/cli_data_entry.py
```

## Example data fields

* Food name
* Cuisine
* Location

## Output

The script generates a file called:

food_data.json

This file contains all confirmed entries in JSON format.

#!/usr/bin/env python3
import tkinter as tk
from datetime import datetime, timedelta
import os
import re
"""
Todo:
build a proper NxN matrix.
build a list of items to arrange in the matix.
save the state of the game.
save the date time in the file.
encode the file to keep the noobs out.


Todo:
Build an exe.
**hand waving**
yes itll build the exe, but can we modify script path in the exe?
I have no idea. Just going to try it. 
pip install pyinstaller
pyinstaller --onefile --noconsole  --collect-all tkinter main.py

"""


# Path to the script itself
SCRIPT_PATH = os.path.abspath(__file__)

# Function to show the tiles and then close the windows
def show_close():
    for i in range(9):
        label = tk.Label(root, text=f"Tile {i + 1}", padx=20, pady=10, borderwidth=1, relief="solid")
        label.grid(row=0, column=i, padx=5, pady=10)
    
    # Calculate the next allowed open date and update the script with it
    next_open_date = datetime.fromisoformat("2024-11-18T19:05:12.011007")
    update_script_date(next_open_date)

    # Close the window after a short delay
    root.after(10000, root.destroy)

# Function to check if the app can be opened
def can_open():
    if os.path.exists("next_open_date.txt"):
        with open("next_open_date.txt", "r") as file:
            next_open_date = datetime.fromisoformat(file.read().strip())
        return datetime.now() >= next_open_date
    return True

# Function to update the script with the new next open date
def update_script_date(next_open_date):
    # Format the date for replacement
    next_date_str = next_open_date.isoformat()
    
    # Read the script's content
    with open(SCRIPT_PATH, "r") as script_file:
        script_content = script_file.read()
    
    # Search for the current date assignment line and replace it
    updated_content = re.sub(
        r'next_open_date = datetime\.now\(\) \+ timedelta\(weeks=1\)',
        f'next_open_date = datetime.fromisoformat("{next_date_str}")',
        script_content
    )

    # Write the updated content back to the script
    with open(SCRIPT_PATH, "w") as script_file:
        script_file.write(updated_content)

if can_open():
    root = tk.Tk()
    root.title("Tiles App")
    show_close()
    root.update()
    root.mainloop()
else:
    print("The app is closed and won't reopen until next week!")


#Todays Challenge is Memory Challenge:Tiles Close & Won't Reopen for a week
#I will use Tkinter library to install pip install tkinter
import tkinter as tk 
from datetime import datetime, timedelta
import os 

#Function to show the tiles and then close the windows
def show_close():
    for i in range(5):
        label = tk.Label(root, text=f"Tile {i + 1}",padx = 20,pady= 10 , borderwidth= 1, relief= "solid")
        label.grid(row=0 , column= i, padx= 5, pady= 10)
    
    #save the next allowed open date 
    next_open_date = datetime.now() + timedelta(weeks= 1)
    with open("next_open_date.txt","w") as file: 
        file.write(next_open_date.isoformat())
    #Close the window    
    root.after(5000,root.destroy)

#function to check if the app can be opened
def can_open():
    if os.path.exists("next_open_date.txt"):
        with open("next_open_date.txt","r") as file:
            next_open_date = datetime.fromisoformat(file.read().strip())
        return datetime.now() >= next_open_date
    return True

if can_open():
    root = tk.Tk()
    root.title("Tiles App")
    show_close()
    root.mainloop()
else:
    print("The app is closed and won't repen until next week!")


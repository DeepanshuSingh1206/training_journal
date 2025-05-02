import tkinter as tk
# Making the main window
root = tk.Tk()
# Setting main window title
root.title("Trainig Journal")
# Setting main window icon
img = tk.PhotoImage(file=f"book.png")
root.iconphoto(False, img)

# Setting the label date
var = tk.StringVar()
var.set("Date")
date = tk.Label(root, textvariable=var)

# Puttind date label on window
date.grid(row = 0, column = 0)

# Making the Year label
var = tk.StringVar()
var.set("Year")
Year_label = tk.Label(root, textvariable = var)
# Putting the Year label on the window 
Year_label.grid(row = 0, column = 1)
# Making the Year entry box
year_input = tk.Entry(root)
# Putting the Year entry box on the window
year_input.grid(row = 0, column = 2)

# Making the Month label
var = tk.StringVar()
var.set("Month")
Month_label = tk.Label(root, textvariable = var)
# Putting the Month Label On the Window
Month_label.grid(row = 0, column = 3)
# Making the Month entry box
month_input = tk.Entry(root)
# Putting the Month entry box on the window
month_input.grid(row = 0, column = 4)

# Making the Day label
var = tk.StringVar()
var.set("Day")
Day_label = tk.Label(root, textvariable = var)
# Putting the Month Label On the Window
Day_label.grid(row = 0, column = 5)

# Making the Day entry box
day_input = tk.Entry(root)
# Putting the Day entry box on the window
day_input.grid(row = 0, column = 6)

# Date button function
def date_button_function():
    try:
        int(year_input.get())
    except ValueError:
        print("Must be an Integer")

# Making the Date button
date_button = tk.Button(root, text = "Enter", command = date_button_function)
date_button.grid(row = 0, column = 7)

# Running the loop
root.mainloop()
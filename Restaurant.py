# Import Modules

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Create dict that stores all kinds of meals
meals = {
    "Pizza": 100,
    "Burger": 300,
    "Nuggets" : 70,
    "Pommes fries": 40,
    "Brosted" : 150,
    "Steak" : 500,
    "Fried chicken":350
}

# store desserts
desserts = {
    "Basbousa" : 150,
    "Kunafa" : 300,
    "Donuts" : 200,
    "Cupcake" : 150,
    "Gateaux": 400,
    "Molten Cake": 600,
    "Baklawa" : 250
}

# Store drinks
drinks = {
    "Mineral Water" : 10,
    "Apple juice" : 30,
    "Orange juice" : 20
}

# Function for submit button
def submit():
    try:
        total = calc()
        customer = customer_entry.get()
        order = order_type.get()
        meal = meal_combo.get()
        dessert = dessert_combo.get()
        drink = drink_combo.get()
        repetitive = num_enter.get()
        service_added = service()

        final = [customer, order, meal, meals[meal], dessert, desserts[dessert], drink, drinks[drink], repetitive, service_added, total]

        with open("orders_db.csv", 'a', newline='') as file:
            file.write(', '.join(map(str, final)) + "\n")

        message = messagebox.showinfo(title="Confirm", message=f"Order made ✅ Price is {total}")
        clear()
    except:
        sad_message = messagebox.showwarning(title="No order made", message="No order made")
        customer_entry.focus_set()
        return

# Calculate price
def calc():
    total = 0
    meal_price = meals[meal_combo.get()]
    dessert_price = desserts[dessert_combo.get()]
    drink_price = drinks[drink_combo.get()]
    service = order_type.get()
    how_many = int(num_enter.get())
    total = (meal_price + dessert_price + drink_price) * how_many

    if service == "At Restaurant":
        total += total * 0.01  
    elif service == "Delivery":
        total += 50  

    return round(total, 2)

# Get service price
def service():
    total = calc()
    service = order_type.get()
    if service == "At Restaurant":
        service_added = total - (total * 0.99)
    elif service == "Delivery":
        service_added = 50
    else:
        service_added = 0

    return round(service_added , 2)

# function for clear button
def clear():
    customer_entry.delete(0, "end")
    meal_combo.delete(0,"end")
    dessert_combo.delete(0,"end")
    drink_combo.delete(0,"end")
    order_type.set("none")
    num_enter.delete(0, "end")
    customer_entry.focus_set()

#######################################################################################################
# Start program
root = Tk()

root.title("Senson and Boz Restaurant")
root.geometry("400x350")
root.resizable(False, False)
# Welcome
welcome = Label(root, text="Make your Order", font="Arial 20 bold", fg="#000000")
welcome.grid(row=0, column=0, pady=10, columnspan=4)

# Customer
customer_label = Label(root, text="Customer Name", fg="#000000")
customer_label.grid(row=1, column=0, pady=10, padx=3)

customer_entry = ttk.Entry(root, width=20)
customer_entry.focus_set()
customer_entry.grid(row=1, column=1, pady=10, sticky="we")

# Order type
order_type = StringVar()
order_type.set("none")

at_rest = ttk.Radiobutton(root, text="At restaurant", variable=order_type, value="At Restaurant")
delivery = ttk.Radiobutton(root, text="Delivery", variable=order_type, value="Delivery")
take_away = ttk.Radiobutton(root, text="Take away", variable=order_type, value="Take away")

at_rest.grid(row=2, column=0, padx=3)
delivery.grid(row=2, column=1, padx=3)
take_away.grid(row=2, column=2, padx=3)

# Meal type
meal_label = Label(root, text="Choose your meal", fg="#000000")
meal_label.grid(row=3, column=0, pady=10, padx=3)

meal_combo = ttk.Combobox(root, values=[i for i in meals.keys()])
meal_combo.state(["readonly"])
meal_combo.grid(row=3, column=1, pady=10, padx=3, sticky="we")

# Dessert type
dessert_label = Label(root, text="Choose your dessert", fg="#000000")
dessert_label.grid(row=4, column=0, pady=10, padx=3)

dessert_combo = ttk.Combobox(root, values=[i for i in desserts.keys()])
dessert_combo.state(["readonly"])
dessert_combo.grid(row=4, column=1, pady=10, padx=3, sticky="we")

# Drink type
drink_label = Label(root, text="Choose your drink", fg="#000000")
drink_label.grid(row=5, column=0, pady=10, padx=3)

drink_combo = ttk.Combobox(root, values=[i for i in drinks.keys()])
drink_combo.state(["readonly"])
drink_combo.grid(row=5, column=1, pady=10, padx=3, sticky="we")

# Number of orders
num_label = Label(root, text="How many?", fg="#000000")
num_label.grid(row=6, column=0, pady=10, padx=3)

num_enter = ttk.Entry(root, width=20)
num_enter.grid(row=6, column=1, pady=10, padx=3, sticky="we")

# Submit button
submit_button = ttk.Button(root, text="Submit Order", command=submit)
submit_button.grid(row=7, column=0, pady=10, padx=3, columnspan=2)

# Cancel button
clear_button = ttk.Button(root, text="Clear Order", command=clear)
clear_button.grid(row=7, column=1, pady=10, padx=3, columnspan=2)

# Update screen
root.mainloop()
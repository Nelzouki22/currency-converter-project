import tkinter as tk
from tkinter import messagebox
import requests

# Function to convert currency
def convert_currency():
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    amount = amount_entry.get()

    if not amount:
        messagebox.showwarning("Input Error", "Please enter an amount to convert.")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric amount.")
        return

    result_label.config(text=f"Fetching conversion rate from {from_currency} to {to_currency}...")
    
    url = f"https://v6.exchangerate-api.com/v6/c03b07b3c9979924be9cc23b/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "conversion_rates" in data:
        if to_currency in data['conversion_rates']:
            rate = data['conversion_rates'][to_currency]
            converted_amount = amount * rate
            result_label.config(
                text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}",
                fg="green"
            )
        else:
            result_label.config(
                text=f"Currency {to_currency} not found.",
                fg="red"
            )
    else:
        result_label.config(
            text="Error fetching conversion rate.",
            fg="red"
        )

# Set up the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Frame for input fields
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

# Input fields
from_currency_label = tk.Label(frame, text="From Currency (e.g. USD):", bg="#f0f0f0")
from_currency_label.grid(row=0, column=0, padx=10, pady=5)
from_currency_entry = tk.Entry(frame, width=15)
from_currency_entry.grid(row=0, column=1, padx=10, pady=5)

to_currency_label = tk.Label(frame, text="To Currency (e.g. EUR):", bg="#f0f0f0")
to_currency_label.grid(row=1, column=0, padx=10, pady=5)
to_currency_entry = tk.Entry(frame, width=15)
to_currency_entry.grid(row=1, column=1, padx=10, pady=5)

amount_label = tk.Label(frame, text="Amount:", bg="#f0f0f0")
amount_label.grid(row=2, column=0, padx=10, pady=5)
amount_entry = tk.Entry(frame, width=15)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10, pady=5)
convert_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()

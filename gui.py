import tkinter as tk
from tkinter import ttk
from api import get_supported_currencies, get_conversion_rate
from converter import convert_currency

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variables
        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        # UI
        self.create_widgets()
        self.load_currency_options()

    def create_widgets(self):
        ttk.Label(self.root, text="From Currency:").pack(pady=5)
        self.from_combo = ttk.Combobox(self.root, textvariable=self.from_currency, state="readonly")
        self.from_combo.pack(pady=5)

        ttk.Label(self.root, text="To Currency:").pack(pady=5)
        self.to_combo = ttk.Combobox(self.root, textvariable=self.to_currency, state="readonly")
        self.to_combo.pack(pady=5)

        ttk.Label(self.root, text="Amount:").pack(pady=5)
        ttk.Entry(self.root, textvariable=self.amount_var).pack(pady=5)

        ttk.Button(self.root, text="Convert", command=self.convert).pack(pady=10)
        ttk.Label(self.root, textvariable=self.result_var, font=("Arial", 12)).pack(pady=10)

    def load_currency_options(self):
        currencies = get_supported_currencies()
        self.from_combo["values"] = currencies
        self.to_combo["values"] = currencies
        if "USD" in currencies:
            self.from_currency.set("USD")
        if "INR" in currencies:
            self.to_currency.set("INR")

    def convert(self):
        base = self.from_currency.get()
        target = self.to_currency.get()
        amount = self.amount_var.get()

        if not amount:
            self.result_var.set("Enter amount")
            return

        rate = get_conversion_rate(base, target)
        if rate:
            converted = convert_currency(amount, rate)
            self.result_var.set(f"{amount} {base} = {converted} {target}")
        else:
            self.result_var.set("Conversion failed. Try again.")

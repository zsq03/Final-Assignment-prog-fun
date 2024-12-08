import pickle  # For storing ticket data
import os  # For file operations
import tkinter as tk
from tkinter import messagebox  # For user-friendly alerts


# Admin Dashboard class for managing tickets
class AdmDash:
    def __init__(self, root):
        self.file = "tickets.pkl"  # Ticket data file
        self.tickets = self.load_tickets()

        self.root = root
        self.root.title("AdmDash Interface")

        # View ticket purchases button
        tk.Button(self.root, text="View Purchases", command=self.view_tix).pack()

        # Modify ticket prices button
        tk.Button(self.root, text="Update Prices", command=self.update_prices).pack()

        # View daily sales button
        tk.Button(self.root, text="Daily Sales", command=self.view_sales).pack()

        # Quit button
        tk.Button(self.root, text="Quit", command=self.quit).pack()

    # Load tickets from file
    def load_tickets(self):
        if os.path.exists(self.file):
            with open(self.file, "rb") as f:
                return pickle.load(f)
        return []

    # Save tickets to file
    def save_tickets(self):
        with open(self.file, "wb") as f:
            pickle.dump(self.tickets, f)

    # View ticket purchases
    def view_tix(self):
        if not self.tickets:
            messagebox.showinfo("No Tickets", "No ticket purchases found.")
            return

        ticket_info = "\n".join([
            f"Type: {t.get_t_type()}, Qty: {t.get_qty()}, Payment: {t.get_pay_method()}, Online: {t.get_online()}"
            for t in self.tickets
        ])
        messagebox.showinfo("Purchases", ticket_info)

    # Update ticket prices
    def update_prices(self):
        def save_new_price():
            t_type = t_type_entry.get()
            new_price = price_entry.get()

            # Validate and save
            try:
                prices = {"1": 275, "2": 480, "3": 1840, "4": 185, "5": 220, "6": 550}
                if t_type in prices:
                    prices[t_type] = float(new_price)
                    messagebox.showinfo("Success", f"Updated Type {t_type} to {new_price} DHS")
                else:
                    messagebox.showerror("Error", "Invalid ticket type.")
            except ValueError:
                messagebox.showerror("Error", "Invalid price format.")

            upd_win.destroy()

        upd_win = tk.Toplevel(self.root)
        upd_win.title("Update Prices")

        tk.Label(upd_win, text="Ticket Type (1-6)").pack()
        t_type_entry = tk.Entry(upd_win)
        t_type_entry.pack()

        tk.Label(upd_win, text="New Price").pack()
        price_entry = tk.Entry(upd_win)
        price_entry.pack()

        tk.Button(upd_win, text="Save", command=save_new_price).pack()

    # View daily sales
    def view_sales(self):
        daily_sales = {}
        for t in self.tickets:
            daily_sales[t.get_t_type()] = daily_sales.get(t.get_t_type(), 0) + t.get_qty()

        sales_info = "\n".join([f"Type {k}: {v} tickets sold" for k, v in daily_sales.items()])
        messagebox.showinfo("Daily Sales", sales_info or "No sales data available.")

    # Quit the application
    def quit(self):
        self.root.quit()

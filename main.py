# Import necessary modules for GUI and features
import tkinter as tk
from account_mgmt import AcctMgmt  # Account Management module
from ticket_purch import TixPurch  # Ticket Purchasing module
from admin_dash import AdmDash  # Admin Dashboard module

# Main program functionality for Adventure Land Ticket Booking
def main():
    # Create the main Tkinter window
    root = tk.Tk()
    root.geometry("1200x1200")  # Set an intuitive window size

    # Program Menu Loop
    while True:
        print("\nWelcome to Adventure Land Ticket Booking System!")
        print("1. Account Management")
        print("2. Ticket Purchasing")
        print("3. Admin Dashboard")
        print("4. Exit")

        # Get user's choice
        choice = input("Enter your choice: ")

        # Navigation to respective modules
        if choice == "1":
            acct_mgmt = AcctMgmt(root)  # Initialize Account Management
            root.mainloop()  # Start Tkinter loop for Account Management
        elif choice == "2":
            tix_purch = TixPurch(root)  # Initialize Ticket Purchasing
            root.mainloop()  # Start Tkinter loop for Ticket Purchasing
        elif choice == "3":
            adm_dash = AdmDash(root)  # Initialize Admin Dashboard
            root.mainloop()  # Start Tkinter loop for Admin Dashboard
        elif choice == "4":
            print("Thanks for using Adventure Land Ticket Booking System!")
            break  # Exit program
        else:
            print("Invalid choice. Please select an option from 1 to 4.")

# Entry point for the program
if __name__ == "__main__":
    main()

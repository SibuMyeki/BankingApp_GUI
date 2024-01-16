import sqlite3
import random as r
from tkinter import messagebox
from datetime import datetime  
import tkinter as tk
from tkinter import *
import string



class welcomeScreen:
    def __init__(self, window=None):
        self.master = window
        self.logged_in_user = None
        window.geometry("600x450+383+106")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("WELCOME TO THEE DECIDERS BANK")
        window.configure(background="#04577c")
        window.configure(cursor="arrow")
        
        self.Canvas1 = tk.Canvas(window, background="#467ebc", borderwidth="0", insertbackground="black",
                                relief="ridge",
                                selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.190, rely=0.228, relheight=0.496, relwidth=0.622)

        self.Button1 = tk.Button(self.Canvas1, command=self.createCustaccount, activebackground="#ececec",
                                activeforeground="#000000", background="#023047", disabledforeground="#a3a3a3",
                                foreground="#fbfbfb", borderwidth="0", highlightbackground="#d9d9d9",
                                highlightcolor="green", pady="0",
                                text='''Register''')
        self.Button1.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button1.place(relx=0.161, rely=0.583, height=24, width=87)

        self.Button2 = tk.Button(self.Canvas1, command=self.selectCustomer, activebackground="#ececec",
                                activeforeground="#000000", background="#023047", disabledforeground="#a3a3a3",
                                foreground="#f9f9f9", borderwidth="0", highlightbackground="#d9d9d9",
                                highlightcolor="green", pady="0",
                                text='''Login''')
        self.Button2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Button2.place(relx=0.617, rely=0.583, height=24, width=87)

        self.Label1 = tk.Label(self.Canvas1, background="#467ebc", disabledforeground="#a3a3a3",
                            font="-family {Segoe UI} -size 12 -weight bold", foreground="#000000",
                            text='''Thee Deciders Bank''')
        self.Label1.place(relx=0.250, rely=0.250, height=38, width=260)
        
        def maximize_window():
            window.attributes('-zoomed', True)  # Maximize the window

        # Create a function to minimize the window
        def minimize_window():
            window.attributes('-zoomed', False)  # Restore to normal size

        # Make the window resizable
        window.resizable(True, True)
        
    def selectCustomer(self):
        self.master.withdraw()
        CustomerLogin(Toplevel(self.master))
        
    def createCustaccount(self):
        createCustomerAccount(Toplevel(self.master))

class CustomerLogin:
    def __init__(self, window=None):
        self.master = window
        self.logged_in_user = None
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        window.geometry("743x494+338+92")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Login")
        window.configure(background="#04577c")

        global Canvas1
        Canvas1 = tk.Canvas(window, background="#ffffff", insertbackground="black", relief="ridge",
                            selectbackground="blue", selectforeground="white")
        Canvas1.place(relx=0.108, rely=0.142, relheight=0.715, relwidth=0.798)

        Label1 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3",
                        font="-family {Segoe UI} -size 14 -weight bold", foreground="#00254a",
                        text="Login")
        Label1.place(relx=0.135, rely=0.142, height=41, width=154)

        global Label2
        Label2 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        Label2.place(relx=0.067, rely=0.283, height=18, width=233)
        global _img0
        _img0 = tk.PhotoImage(file="./images/deciders.png")
        Label2.configure(image=_img0)

        self.Entry1 = tk.Entry(Canvas1, background="#e2e2e2", borderwidth="3", disabledforeground="#a3a3a3",
                            font="TkFixedFont", foreground="#000000", highlightbackground="#b6b6b6",
                            highlightcolor="#004080", insertbackground="black")
        self.Entry1.place(relx=0.609, rely=0.453, height=20, relwidth=0.26)

        self.Entry1_1 = tk.Entry(Canvas1, show='*', background="#e2e2e2", borderwidth="3",
                                disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000",
                                highlightbackground="#d9d9d9", highlightcolor="#004080", insertbackground="black",
                                selectbackground="blue", selectforeground="white")
        self.Entry1_1.place(relx=0.609, rely=0.623, height=20, relwidth=0.26)

        self.Label3 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label3.place(relx=0.556, rely=0.453, height=21, width=34)

        # Make the window resizable
        window.resizable(True, True)
        
        global _img1
        _img1 = tk.PhotoImage(file="./images/user1.png")
        self.Label3.configure(image=_img1)

        self.Label4 = tk.Label(Canvas1)
        self.Label4.place(relx=0.556, rely=0.623, height=21, width=34)
        global _img2
        _img2 = tk.PhotoImage(file="./images/lock1.png")
        self.Label4.configure(image=_img2, background="#ffffff")

        self.Label5 = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label5.place(relx=0.670, rely=0.142, height=71, width=74)
        global _img3
        _img3 = tk.PhotoImage(file="./images/bank1.png")
        self.Label5.configure(image=_img3)

        self.Button = tk.Button(Canvas1, text="Login", borderwidth="0", width=10, background="#00254a",
                                foreground="#ffffff",
                                font="-family {Segoe UI} -size 10 -weight bold",
                                command= self.login)
        self.Button.place(relx=0.765, rely=0.755)

        self.Button_back = tk.Button(Canvas1, text="Back", borderwidth="0", width=10, background="#00254a",
                                    foreground="#ffffff",
                                    font="-family {Segoe UI} -size 10 -weight bold",
                                    command=self.back)
        self.Button_back.place(relx=0.545, rely=0.755)

        global customer_img
        # customer_img = tk.PhotoImage(file="./images/customer.png")

    def back(self):
        self.master.withdraw()
        welcomeScreen(Toplevel(self.master))

    @staticmethod
    def setImg():
        settingIMG = tk.Label(Canvas1, background="#ffffff", disabledforeground="#a3a3a3", foreground="#000000")
        settingIMG.place(relx=0.067, rely=0.283, height=181, width=233)
        # settingIMG.configure(image=customer_img)

    def login(self):
        first_name = self.Entry1.get()
        password = self.Entry1_1.get()
        if first_name == "" or password == "":
            custom_message = "Please enter both name and password."
            CustomMessageBox(self.master, "Try Again",custom_message)
        result = self.c.execute('SELECT * FROM Bank WHERE account_name LIKE ? AND password = ?', (f"{first_name}%", password)).fetchone()
        if result:
            self.logged_in_user = result
            self.master.withdraw()
            customerMenu.logged_in_user = self.logged_in_user
            customerMenu(Toplevel(self.master))
        else:
            Error(Toplevel(self.master))
            Error.setMessage(self, message_shown="Invalid Credentials!")
            self.setImg()

class customerMenu:
    def __init__(self, window=None):
        self.master = window
        customerMenu.logged_in_user = self.logged_in_user
        # self.logged_in_user = None
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        window.geometry("743x494+329+153")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Menu")
        window.configure(background="#04577c")

        self.Labelframe1 = tk.LabelFrame(window, relief='groove', font="-family {Segoe UI} -size 13 -weight bold",
                                        foreground="#000000", text='''Thee Deciders Bank''', background="#fffffe")
        self.Labelframe1.place(relx=0.081, rely=0.081, relheight=0.415, relwidth=0.848)

        self.Button1 = tk.Button(self.Labelframe1, command=self.selectWithdraw, activebackground="#ececec",
                                activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Withdraw''')
        self.Button1.place(relx=0.667, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button2 = tk.Button(self.Labelframe1, command=self.selectDeposit, activebackground="#ececec",
                                activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Deposit''')
        self.Button2.place(relx=0.04, rely=0.195, height=34, width=181, bordermode='ignore')

        self.Button3 = tk.Button(self.Labelframe1, command=self.exit, activebackground="#ececec",
                                activeforeground="#000000",
                                background="#39a9fc",
                                borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11",
                                foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                text='''Exit''')
        self.Button3.place(relx=0.667, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Button4 = tk.Button(self.Labelframe1, command=self.selectChangePIN, activebackground="#ececec",
                                activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Change PIN''')
        self.Button4.place(relx=0.04, rely=0.439, height=34, width=181, bordermode='ignore')

        self.Button6 = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                background="#39a9fc", borderwidth="0", disabledforeground="#a3a3a3",
                                font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                text='''Check your balance''', command=self.checkBalance)
        self.Button6.place(relx=0.04, rely=0.683, height=34, width=181, bordermode='ignore')
        
        self.Button_balance = tk.Button(self.Labelframe1, activebackground="#ececec", activeforeground="#000000",
                                        background="#39a9fc", borderwidth="0", disabledforeground="#a3a3a3",
                                        font="-family {Segoe UI} -size 11", foreground="#fffffe",
                                        highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                        text='''Check Balance''', command=self.checkBalance)
        self.Button_balance.place(relx=0.04, rely=0.683, height=34, width=181, bordermode='ignore')

        self.Button_transactions = tk.Button(self.Labelframe1, activebackground="#ececec",
                                        activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                        disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11",
                                        foreground="#fffffe", highlightbackground="#d9d9d9",
                                        highlightcolor="black", pady="0", text='''View Transactions''',
                                        command=self.viewTransactions)
        self.Button_transactions.place(relx=0.667, rely=0.683, height=34, width=181, bordermode='ignore')
        
        def maximize_window():
            window.attributes('-zoomed', True)  # Maximize the window

        # Create a function to minimize the window
        def minimize_window():
            window.attributes('-zoomed', False)  # Restore to normal size

        # Make the window resizable
        window.resizable(True, True)

        # Add buttons to maximize and minimize the window
        
        
        global Frame1_1_2
        # Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="2", background="#04577c")
        # Frame1_1_2.place(relx=0.081, rely=0.767, relheight=0.195, relwidth=0.848)
        
        self.Button_logout = tk.Button(self.Labelframe1, activebackground="#ececec",
                                    activeforeground="#000000", background="#39a9fc", borderwidth="0",
                                    disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 11",
                                    foreground="#fffffe", highlightbackground="#d9d9d9", highlightcolor="black",
                                    pady="0", text='''Logout''', command=self.logout)
        self.Button_logout.place(relx=0.667, rely=0.879, height=34, width=181, bordermode='ignore')
        
    def logout(self):
        self.logged_in_user = None
        self.master.withdraw()
        welcomeScreen(Toplevel(self.master))
        
    # def viewTransactions(self):
    #     self.logged_in_user =None
    #     account_name = self.logged_in_user[0]  # Assuming account name is at index 0 in the user tuple
    #     # Retrieve transactions from the database
    #     transactions = self.c.execute('SELECT * FROM Transactions WHERE account_name = ?', (account_name,)).fetchall()

    #     if transactions:
    #         # Format transaction data
    #         transaction_history = "Transaction History:\n\n"
    #         for transaction in transactions:
    #             transaction_history += f"Type: {transaction[1]}, Amount: {transaction[2]}, Date: {transaction[3]}\n"
    #         # Display transaction history (you can adjust how to display this information)
    #         messagebox.showinfo("Transaction History", transaction_history)
    #     else:
    #         messagebox.showinfo("Transaction History", "No transactions found.")
    
    def viewTransactions(self):
        if self.logged_in_user is None:
            messagebox.showerror("Error", "Please log in first.")
            return

        account_name = self.logged_in_user[0]  # Assuming account name is at index 0 in the user tuple

    # Retrieve transactions from the database
        transactions = self.c.execute('SELECT * FROM Transactions WHERE account_name = ?', (account_name,)).fetchall()

        if transactions:
            # Format transaction data
            transaction_history = "Transaction History:\n\n"
            for transaction in transactions:
                transaction_history += f"Type: {transaction[1]}, Amount: {transaction[2]}, Date: {transaction[3]}\n"

            # Display transaction history (you can adjust how to display this information)
            messagebox.showinfo("Transaction History", transaction_history)
        else:
            messagebox.showinfo("Transaction History", "No transactions found.")

    # def viewTransactions(self):
        # transactions(Toplevel(self.master))
        # Frame1_1_2 = tk.Frame(window, relief='groove', borderwidth="2", background="#fffffe")
        # Frame1_1_2.place(relx=0.081, rely=0.547, relheight=0.415, relwidth=0.848)

    def selectDeposit(self):
        depositMoney(Toplevel(self.master))

    def selectWithdraw(self):
        withdrawMoney(Toplevel(self.master))

    def selectChangePIN(self):
        changePIN(Toplevel(self.master))

    def exit(self):
        self.master.withdraw()
        CustomerLogin(Toplevel(self.master))

    def checkBalance(self):
        if self.logged_in_user is not None:
            account_name = self.logged_in_user[0]  # Assuming account name is at index 0 in the user tuple
            # Retrieve balance from the database
            user_data = self.c.execute('SELECT balance FROM Bank WHERE account_name = ?', (account_name,)).fetchone()
            if user_data:
                current_balance = user_data[0]  # Assuming balance is the first column returned
                messagebox.showinfo("Current Balance", f"Your current balance is: R {current_balance:.2f}")
            else:
                messagebox.showerror("Error", "Failed to fetch balance. Please try again.")
        else:
            messagebox.showerror("Error", "Please log in first.")


    def printMessage(self, output):
        # clearing the frame
        for widget in Frame1_1_2.winfo_children():
            widget.destroy()
        # getting output_message and displaying it in the frame
        output_message = Label(Frame1_1_2, text=output, background="#fffffe")
        output_message.pack(pady=20)

    def printMessage_outside(output):
        # clearing the frame
        for widget in Frame1_1_2.winfo_children():
            widget.destroy()
        # getting output_message and displaying it in the frame
        output_message = Label(Frame1_1_2, text=output, background="#fffffe")
        output_message.pack(pady=20)


class changePIN:
    def __init__(self, window=None):
        self.master = window
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        self.logged_in_user = None
        window.geometry("411x111+505+223")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Change Passowrd")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                            text='''ID No:''')
        self.Label1.place(relx=0.243, rely=0.144, height=21, width=93)

        self.Label2 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                            text='''New PIN:''')
        self.Label2.place(relx=0.268, rely=0.414, height=21, width=82)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.528, rely=0.144, height=20, relwidth=0.229)

        self.Entry2 = tk.Entry(window, show="*", background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", insertbackground="black")
        self.Entry2.place(relx=0.528, rely=0.414, height=20, relwidth=0.229)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                disabledforeground="#a3a3a3", foreground="#ffffff", borderwidth="0",
                                highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0", text='''Change''',
                                command= self.submit)
        self.Button1.place(relx=0.614, rely=0.721, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                disabledforeground="#a3a3a3", foreground="#ffffff", borderwidth="0",
                                highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0", text="Back", command=self.back)
        self.Button2.place(relx=0.214, rely=0.721, height=24, width=67)
        
        def maximize_window():
            window.attributes('-zoomed', True)  # Maximize the window

        # Create a function to minimize the window
        def minimize_window():
            window.attributes('-zoomed', False)  # Restore to normal size

        # Make the window resizable
        window.resizable(True, True)
        
    def update_password(self, id_number, new_pin):
        self.c.execute('UPDATE Bank SET password = ? WHERE id_number = ?', (new_pin, id_number))
        self.con.commit()
        messagebox.showinfo("Success", "Password changed successfully!")

    def submit(self):
        id_number = self.Entry1.get()
        new_pin = self.Entry2.get()
        # if self.logged_in_user is not None and self.logged_in_user[3] == id_number:
        if new_pin !="" and len(new_pin) >3:
            user_data = self.c.execute('SELECT * FROM Bank WHERE id_number = ?', (id_number,)).fetchone()
            if user_data:
                self.update_password(id_number, new_pin)
            else:
                custom_message = "Invalid details. Password change failed."
                CustomMessageBox(self.master, "Error", custom_message)
        else:
            custom_message = "Four or more Digits."
            CustomMessageBox(self.master, "Error", custom_message)
    def back(self):
        self.master.withdraw()

class withdrawMoney:
    def __init__(self, window=None):
        self.master = window
        self.logged_in_user = customerMenu.logged_in_user 
        # self.logged_in_user = None
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        window.geometry("411x117+519+278")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Withdraw money")
        p1 = PhotoImage(file='./images/withdraw_icon.png')
        window.iconphoto(True, p1)
        window.configure(borderwidth="2")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3",
                            font="-family {Segoe UI} -size 9", foreground="#000000",
                            text='''Enter amount to withdraw :''')
        self.Label1.place(relx=0.146, rely=0.171, height=21, width=164)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", insertbackground="black", selectforeground="#ffffffffffff")
        self.Entry1.place(relx=0.535, rely=0.171, height=20, relwidth=0.253)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                disabledforeground="#a3a3a3", borderwidth="0", foreground="#ffffff",
                                highlightbackground="#000000",
                                highlightcolor="black", pady="0", text='''Withdraw''',
                                command=self.submit)
        self.Button1.place(relx=0.56, rely=0.598, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                disabledforeground="#a3a3a3", borderwidth="0", font="-family {Segoe UI} -size 9",
                                foreground="#ffffff",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                command=self.back)
        self.Button2.place(relx=0.268, rely=0.598, height=24, width=67)
        
        def maximize_window():
            window.attributes('-zoomed', True)  # Maximize the window

        # Create a function to minimize the window
        def minimize_window():
            window.attributes('-zoomed', False)  # Restore to normal size

        # Make the window resizable
        window.resizable(True, True)

    def submit(self):
        amount = self.Entry1.get()
        cleaned_withdrawal_amount = amount.replace(" ", "").strip()
        if cleaned_withdrawal_amount.replace(".", "", 1).isdigit() and float(cleaned_withdrawal_amount) > 0:
            withdrawal_amount = float(cleaned_withdrawal_amount)
            if withdrawal_amount<=0:
                messagebox.showerror("Error", "Enter valid amount")
                return
            if self.logged_in_user is None:
                messagebox.showerror("Error", "Please login first.")
                return
            current_balance = self.logged_in_user[2]
            
            if withdrawal_amount >current_balance:
                messagebox.showerror("Error", "Inssuffient funds.")
                return
            account_name = self.logged_in_user[0]
            new_balance = current_balance - withdrawal_amount
            self.c.execute('UPDATE Bank SET balance = ? WHERE account_name = ?', (new_balance, account_name))
            self.con.commit()
            # Update transaction table
            transaction_data = (account_name, "Withdrawal", withdrawal_amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.c.execute('INSERT INTO Transactions VALUES (?, ?, ?, ?)', transaction_data)
            self.con.commit()
            messagebox.showinfo("Success", f"Withdrawn {withdrawal_amount:.2f} successfully. New balance: {new_balance:.2f}")
        
        else:
            messagebox.showerror("Error", "Invalid amount.")

    # def submit(self, amount):
    #     amount = self.Entry1.get()
    #     cleaned_deposit_amount = amount.replace(" ", "").strip()
    #     if cleaned_deposit_amount.replace(".", "", 1).isdigit() and float(cleaned_deposit_amount) > 0:
    #         deposit_amount = float(cleaned_deposit_amount)
    #         if self.logged_in_user is None:
    #             Error(Toplevel(self.master))
    #             Error.setMessage(self, message_shown="User Information not found!")
    #             return
    #         current_balance = self.logged_in_user[2]
    #         new_balance = current_balance + deposit_amount
    #         account_name = self.logged_in_user[0]
    #         self.c.execute('UPDATE Bank SET balance = ? WHERE account_name = ?', (new_balance, account_name))
    #         self.con.commit()
            
    #         transaction_data = (account_name, "Deposit", deposit_amount, datetime.now().strftime("%Y-%m-%d %H:%M"))
    #         self.c.execute('INSERT INTO Transactions VALUES (?, ?, ?, ?)', transaction_data)
    #         self.con.commit()
            
    #         messagebox.showinfo("Success", f"Deposited {deposit_amount:.2f} successfully. New balance: {new_balance:.2f}")
    #     else:
    #         Error(Toplevel(self.master))
    #         Error.setMessage(self, message_shown="Invalid amount!")
                
                
    def back(self):
        self.master.withdraw()

class depositMoney:
    def __init__(self, window=None):
        self.master = window
        self.logged_in_user = customerMenu.logged_in_user
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        window.geometry("411x117+519+278")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Deposit money")
        p1 = PhotoImage(file='./images/deposit_icon.png')
        window.iconphoto(True, p1)
        window.configure(borderwidth="2")
        window.configure(background="#f2f3f4")

        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3",
                            font="-family {Segoe UI} -size 9", foreground="#000000", borderwidth="0",
                            text='''Enter amount to deposit :''')
        self.Label1.place(relx=0.146, rely=0.171, height=21, width=164)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", insertbackground="black", selectforeground="#ffffffffffff")
        self.Entry1.place(relx=0.535, rely=0.171, height=20, relwidth=0.253)

        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                disabledforeground="#a3a3a3", borderwidth="0", foreground="#ffffff",
                                highlightbackground="#000000",
                                highlightcolor="black", pady="0", text='''Deposit''',
                                command= self.submit)
        self.Button1.place(relx=0.56, rely=0.598, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9", foreground="#ffffff",
                                highlightbackground="#d9d9d9", borderwidth="0", highlightcolor="black", pady="0",
                                text='''Back''',
                                command=self.back)
        self.Button2.place(relx=0.268, rely=0.598, height=24, width=67)
        
        
        def maximize_window():
            window.attributes('-zoomed', True)  # Maximize the window

        # Create a function to minimize the window
        def minimize_window():
            window.attributes('-zoomed', False)  # Restore to normal size

        # Make the window resizable
        window.resizable(True, True)
    
    def submit(self):
        amount = self.Entry1.get()
        cleaned_deposit_amount = amount.replace(" ", "").strip()
        if cleaned_deposit_amount.replace(".", "", 1).isdigit() and float(cleaned_deposit_amount) > 0:
            deposit_amount = float(cleaned_deposit_amount)
            if self.logged_in_user is None:
                messagebox.showerror("Error", "Please log in first.")
                return
            current_balance = self.logged_in_user[2]  # Assuming the balance is in the third position of user data
            # Calculate new balance after deposit
            new_balance = current_balance + deposit_amount
            # Update the balance in the database for the logged-in user
            account_name = self.logged_in_user[0]  # Assuming the account name is in the first position of user data
            self.c.execute('UPDATE Bank SET balance = ? WHERE account_name = ?', (new_balance, account_name))
            self.con.commit()
            # Update transaction table
            transaction_data = (account_name, "Deposit", deposit_amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.c.execute('INSERT INTO Transactions VALUES (?, ?, ?, ?)', transaction_data)
            self.con.commit()

            messagebox.showinfo("Success", f"Deposited {deposit_amount:.2f} successfully. New balance: {new_balance:.2f}")
        else:
            messagebox.showerror("Error", "Please enter a valid amount.")
    
    # def submit(self, amount):
    #     amount = self.Entry1.get()
    #     cleaned_deposit_amount = amount.replace(" ", "").strip()
    #     if cleaned_deposit_amount.replace(".", "", 1).isdigit() and float(cleaned_deposit_amount) > 0:
    #         amount = float(cleaned_deposit_amount)
    #         if amount <= 0:
    #             messagebox.showerror("Error", "Please enter a valid amount.")
    #             return
    #         if self.logged_in_user is None:
    #             messagebox.showerror("Error", "Please log in first.")
    #             return
    #         current_balance = self.logged_in_user[2]
    #         new_balance = current_balance + amount
    #         account_name = self.logged_in_user[0]
            
    #         self.c.execute('UPDATE Bank SET balance = ? WHERE account_name = ?', (new_balance, account_name))
    #         self.con.commit()
            
    #         transaction_data = (account_name, "Deposit", amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #         self.c.execute('INSERT INTO Transactions VALUES (?, ?, ?, ?)', transaction_data)
    #         self.con.commit()
            
    #         messagebox.showinfo("Success", f"Deposited {amount:.2f} successfully. New balance: {new_balance:.2f}")
    #     else:
    #         messagebox.showerror("Error", "Please enter a valid amount.")

        
    def back(self):
        self.master.withdraw()

class CustomMessageBox(tk.Toplevel):
    def __init__(self, parent, title, message):
        window=None
        super().__init__(parent)
        self.title(title)
        self.label = tk.Label(self, text=message, font=("Arial", 12), padx=20, pady=10)
        self.label.pack()
        self.configure(bg="#04577c")
        self.label.configure(bg="#04577c", fg="white")
        self.geometry("300x100+100+100")
        self.transient(parent)
        self.grab_set()
        self.focus_set()
        self.wait_window(self)
        
        global Label2
        
        self.Button1 = tk.Button(window, background="#d3d8dc", borderwidth="1", disabledforeground="#a3a3a3",
                                font="-family {Segoe UI} -size 9", foreground="#000000", highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0", text='''OK''', command=self.goback)
        self.Button1.place(relx=0.779, rely=0.598, height=24, width=67)
    
    def goback(self):
        self.master

class Error:
    def __init__(self, window=None):
        global master
        master = window
        window.geometry("411x117+485+248")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Error")
        window.configure(background="#f2f3f4")

        global Label2

        self.Button1 = tk.Button(window, background="#d3d8dc", borderwidth="1", disabledforeground="#a3a3a3",
                                font="-family {Segoe UI} -size 9", foreground="#000000", highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0", text='''OK''', command=self.goback)
        self.Button1.place(relx=0.779, rely=0.598, height=24, width=67)

        global _img0
        _img0 = tk.PhotoImage(file="./images/error_image.png")
        self.Label1 = tk.Label(window, background="#f2f3f4", disabledforeground="#a3a3a3", foreground="#000000",
                            image=_img0, text='''Label''')
        self.Label1.place(relx=0.024, rely=0.0, height=81, width=84)

    def setMessage(self, message_shown):
        Label2 = tk.Label(master, background="#f2f3f4", disabledforeground="#a3a3a3",
                        font="-family {Segoe UI} -size 16", foreground="#000000", highlightcolor="#646464646464",
                        text=message_shown)
        Label2.place(relx=0.210, rely=0.171, height=41, width=214)

    def goback(self):
        master.withdraw()

class createCustomerAccount:
    
    def generate_random_password(length=12):
        # Define characters to choose from
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        symbols = '!@#$%^&*()_+[]{}|;:,.<>?'
        # Combine all characters
        all_characters = lowercase_letters + uppercase_letters + digits + symbols
        # Generate a random password of length 12
        password = ''.join(r.choice(all_characters) for _ in range(12))
        return password

    def generate_account_number(self):
        return str(r.randint(10000000, 99999999))
    
    
    def __init__(self, window=None):
        self.master = window
        window.geometry("411x403+437+152")
        window.minsize(120, 1)
        window.maxsize(1370, 749)
        window.resizable(0, 0)
        window.title("Create account")
        window.configure(background="#04577c")
        window.configure(highlightbackground="#d9d9d9")
        window.configure(highlightcolor="black")
        
        self.logged_in_user = None
        self.con = sqlite3.connect("Bank.db")
        self.c = self.con.cursor()
        
        self.c.execute("""create table if not exists Bank
            (
                account_name text,
                acc_no integer,
                balance integer,
                password text,
                id_number integer UNIQUE 
            )""")
        self.c.execute("""create table if not exists Transactions
            (
                account_name text,
                transaction_type text,
                amount integer,
                date text
            )""")
        
        self.Label1 = tk.Label(window, text='''Name:''', background="#04577c", font="-family {Segoe UI} -size 12 -weight bold", foreground="#000000")
        self.Label1.place(relx=0.219, rely=0.025, height=26, width=120)

        self.Entry1 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                            insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry1.place(relx=0.511, rely=0.027, height=20, relwidth=0.302)

        self.Label2 = tk.Label(window, text='''Surname:''', background="#04577c", font="-family {Segoe UI} -size 12 -weight bold", foreground="#000000")
        self.Label2.place(relx=0.316, rely=0.099, height=27, width=75)

        self.Entry2 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                            insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry2.place(relx=0.511, rely=0.099, height=20, relwidth=0.302)

        self.Label3 = tk.Label(window, text='''ID No:''', background="#04577c", font="-family {Segoe UI} -size 12 -weight bold", foreground="#000000")
        self.Label3.place(relx=0.287, rely=0.169, height=26, width=83)

        self.Entry3 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                            insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry3.place(relx=0.511, rely=0.174, height=20, relwidth=0.302)

        self.Label4 = tk.Label(window, text='''Contacts:''', background="#04577c", font="-family {Segoe UI} -size 12 -weight bold", foreground="#000000")
        self.Label4.place(relx=0.268, rely=0.323, height=22, width=100)

        self.Entry4 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                            insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry4.place(relx=0.511, rely=0.323, height=20, relwidth=0.302)

        self.Label5 = tk.Label(window, text='''Initial amt:''', background="#04577c", font="-family {Segoe UI} -size 12 -weight bold", foreground="#000000")
        self.Label5.place(relx=0.268, rely=0.4, height=21, width=100)  

        self.Entry5 = tk.Entry(window, background="#cae4ff", disabledforeground="#a3a3a3", font="TkFixedFont",
                            foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                            insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry5.place(relx=0.511, rely=0.4, height=20, relwidth=0.302)  
        
        self.Button1 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                command=self.back)
        self.Button1.place(relx=0.243, rely=0.893, height=24, width=67)

        self.Button2 = tk.Button(window, activebackground="#ececec", activeforeground="#000000", background="#004080",
                                borderwidth="0", disabledforeground="#a3a3a3", foreground="#ffffff",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Register''',
                                command=self.create_acc)
        self.Button2.place(relx=0.633, rely=0.893, height=24, width=67)
        
        def maximize_window():
            window.attributes('-zoomed', True)  # Maximize the window

        # Create a function to minimize the window
        def minimize_window():
            window.attributes('-zoomed', False)  # Restore to normal size

        # Make the window resizable
        window.resizable(True, True)
        
        
    def back(self):
        self.master.withdraw()
        
    def create_acc(self):
        name = self.Entry1.get()
        surname = self.Entry2.get()
        id_number = self.Entry3.get()
        contact_number = self.Entry4.get()
        initial_amount = self.Entry5.get()
        password = self.generate_random_password()
        account_num = self.generate_account_number()
        
        if name.isalpha() and surname.isalpha() and len(name) > 2 and len(surname) > 2:
            full_name = name + " " + surname
            cleaned_deposit = initial_amount.replace(" ", "").strip()
            if cleaned_deposit.replace(".", "", 1).isdigit() and float(cleaned_deposit) > 0:
                initial_amount = float(cleaned_deposit)
                if id_number.isdigit() and len(id_number) == 6  and contact_number.isdigit() and len(contact_number) == 10:
                    existing_account = self.c.execute('SELECT id_number FROM Bank WHERE id_number = ?', (id_number,)).fetchone()
                    if existing_account:
                        messagebox.showerror("Error", "Account already exists!")
                        return
                    else:
                        self.c.execute('''
                            INSERT INTO Bank (account_name, acc_no, balance, password, id_number) 
                            VALUES (?, ?, ?, ?, ?)
                        ''', (full_name, account_num, initial_amount, password, id_number))
                        self.con.commit()
                        output_message = "Customer account created successfully!"
                        print(output_message)
                        
                        self.Entry1.delete(0, tk.END)
                        self.Entry2.delete(0, tk.END)
                        self.Entry3.delete(0, tk.END)
                        self.Entry4.delete(0, tk.END)
                        self.Entry5.delete(0, tk.END)
                        
                        custom_message = f"Account Number: {account_num}\nPassword: {password}\nPlease save them securely."
                        CustomMessageBox(self.master, "Registration Successful", custom_message)
                        
                        if self.notif:
                            self.notif.config(fg="green", text="Account has been created successfully")
                        else:
                            print("Notification label not initialized properly")
                else:
                    custom_message = "Please enter a valid 6-digit ID number."
                    CustomMessageBox(self.master, "Error", custom_message)
                    
            else:
                custom_message = "Please enter a valid initial deposit amount."
                CustomMessageBox(self.master, "Error", custom_message)
        else:
            custom_message = "Please use valid names."
            CustomMessageBox(self.master, "Error", custom_message)
        
root = tk.Tk()
top = welcomeScreen(root)
root.mainloop()
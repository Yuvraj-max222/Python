import tkinter as tk
from tkinter import messagebox
class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Control")
        self.root.geometry("400x350")
        self.budget = 0.0
        self.balance = 0.0
        self.total_spent = 0.0
        tk.Label(root, text="Set Total Budget ($):", font=("Arial", 10)).pack(pady=5)
        self.entry_budget = tk.Entry(root)
        self.entry_budget.pack(pady=5)
        tk.Button(root, text="Set Budget", command=self.set_budget, bg="#4CAF50", fg="white").pack(pady=5)
        tk.Label(root, text="Enter Expense Amount ($):", font=("Arial", 10)).pack(pady=5)
        self.entry_expense = tk.Entry(root)
        self.entry_expense.pack(pady=5)
        tk.Button(root, text="Add Expense", command=self.add_expense, bg="#2196F3", fg="white").pack(pady=5)
        self.label_status = tk.Label(root, text="Balance: $0.00", font=("Arial", 12, "bold"))
        self.label_status.pack(pady=20)
        self.label_message = tk.Label(root, text="", font=("Arial", 10, "italic"), fg="red")
        self.label_message.pack(pady=5)
    def set_budget(self):
        try:
            val = float(self.entry_budget.get())
            self.budget = val
            self.balance = val
            self.total_spent = 0
            self.update_display()
            messagebox.showinfo("Success", f"Budget set to ${val:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for budget.")
    def add_expense(self):
        if self.budget == 0:
            messagebox.showwarning("Warning", "Please set a budget first!")
            return
        try:
            val = float(self.entry_expense.get())
            self.balance -= val
            self.total_spent += val
            self.entry_expense.delete(0, tk.END) # Clear box
            self.update_display()
            self.check_control_message()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for expense.")
    def update_display(self):
        self.label_status.config(text=f"Budget: ${self.budget:.0f} | Left: ${self.balance:.2f}")
    def check_control_message(self):
        if self.balance < 0:
            msg = "🚨 OVERSPENT! STOP SPENDING!"
            color = "red"
        elif self.balance < (self.budget * 0.2):
            msg = "⚠️ Warning: Low funds!"
            color = "orange"
        else:
            msg = "✅ You are within budget."
            color = "green"
        self.label_message.config(text=msg, fg=color)
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
COLORS = {
    "bg_main": "#f0f2f5",       
    "bg_container": "#ffffff",  
    "text_dark": "#2c3e50",     
    "primary_btn": "#3498db",   
    "success": "#2ecc71",       
    "warning": "#f1c40f",       
    "danger": "#e74c3c",        
}
FONTS = {
    "header": ("Helvetica", 16, "bold"),
    "label": ("Helvetica", 11),
    "entry": ("Helvetica", 12),
    "balance": ("Helvetica", 22, "bold"),
    "message": ("Helvetica", 12, "bold"),
}
class BudgetAppEnhanced:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Control Pro")
        self.root.geometry("450x550")
        self.root.configure(bg=COLORS["bg_main"])
        self.budget = 0.0
        self.balance = 0.0
        self.total_spent = 0.0
        tk.Label(root, text="Personal Finance Tracker", font=FONTS["header"], 
                 bg=COLORS["bg_main"], fg=COLORS["text_dark"]).pack(pady=(30, 20))
        input_frame = tk.Frame(root, bg=COLORS["bg_container"], bd=1, relief=tk.RIDGE)
        input_frame.pack(padx=30, fill="x")
        tk.Label(input_frame, text="Set Monthly Budget ($)", font=FONTS["label"], 
                 bg=COLORS["bg_container"], fg=COLORS["text_dark"]).pack(anchor="w", padx=20, pady=(20, 5))
        self.entry_budget = tk.Entry(input_frame, font=FONTS["entry"], bg="#ecf0f1", bd=0, highlightthickness=1)
        self.entry_budget.pack(padx=20, fill="x", ipady=5)
        btn_set = tk.Button(input_frame, text="SET BUDGET", font=FONTS["label"], bg=COLORS["primary_btn"], fg="white", 
                            relief=tk.FLAT, bd=0, padx=20, pady=5, command=self.set_budget)
        btn_set.pack(pady=15)
        ttk.Separator(input_frame, orient='horizontal').pack(fill='x', padx=20, pady=10)
        tk.Label(input_frame, text="Add New Expense ($)", font=FONTS["label"], 
                 bg=COLORS["bg_container"], fg=COLORS["text_dark"]).pack(anchor="w", padx=20, pady=(10, 5))
        self.entry_expense = tk.Entry(input_frame, font=FONTS["entry"], bg="#ecf0f1", bd=0, highlightthickness=1)
        self.entry_expense.pack(padx=20, fill="x", ipady=5)
        btn_add = tk.Button(input_frame, text="+ ADD EXPENSE", font=FONTS["label"], bg=COLORS["text_dark"], fg="white", 
                            relief=tk.FLAT, bd=0, padx=20, pady=5, command=self.add_expense)
        btn_add.pack(pady=(15, 30))
        dashboard_frame = tk.Frame(root, bg=COLORS["bg_main"])
        dashboard_frame.pack(padx=30, pady=30, fill="x")
        tk.Label(dashboard_frame, text="Remaining Balance:", font=FONTS["label"], 
                 bg=COLORS["bg_main"], fg=COLORS["text_dark"]).pack()
        self.label_balance = tk.Label(dashboard_frame, text="$0.00", font=FONTS["balance"], 
                                      bg=COLORS["bg_main"], fg=COLORS["text_dark"])
        self.label_balance.pack(pady=5)
        self.status_bar = tk.Label(root, text="Please set a budget to begin.", font=FONTS["message"], 
                                   bg="#dfe6e9", fg=COLORS["text_dark"], padx=10, pady=10)
        self.status_bar.pack(fill="x", side="bottom")
    def set_budget(self):
        try:
            val = float(self.entry_budget.get())
            self.budget = val
            self.balance = val
            self.total_spent = 0
            self.update_display()
            messagebox.showinfo("Success", f"Budget set to ${val:.2f}")
        except ValueError:
             messagebox.showerror("Error", "Please enter a valid budget number.")
    def add_expense(self):
        if self.budget == 0:
             messagebox.showwarning("Warning", "Please set a budget first!")
             return
        try:
            val = float(self.entry_expense.get())
            self.balance -= val
            self.total_spent += val
            self.entry_expense.delete(0, tk.END) 
            self.update_display()
        except ValueError:
             messagebox.showerror("Error", "Please enter a valid expense number.")
    def update_display(self):
        self.label_balance.config(text=f"${self.balance:.2f}")
        
        if self.balance < 0:
            self.status_bar.config(text="🚨 ALERT: Over Budget! Stop Spending!", bg=COLORS["danger"], fg="white")
        elif self.balance < (self.budget * 0.2):
            self.status_bar.config(text="⚠️ WARNING: Low Funds.", bg=COLORS["warning"], fg=COLORS["text_dark"])
        else:
            self.status_bar.config(text="✅ STATUS: On Track.", bg=COLORS["success"], fg="white")
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetAppEnhanced(root)
    root.mainloop()
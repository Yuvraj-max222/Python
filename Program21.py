import tkinter as tk
from tkinter import messagebox
from tkinter import ttk # Import ttk for themed widgets (separators)
# --- Configuration ---
# A modern, clean color palette
COLORS = {
    "bg_main": "#f0f2f5",       # Light gray background for the window
    "bg_container": "#ffffff",  # White background for input areas
    "text_dark": "#2c3e50",     # Dark blue-gray for main text
    "primary_btn": "#3498db",   # A nice blue for main actions
    "success": "#2ecc71",       # Green
    "warning": "#f1c40f",       # Yellow/Orange
    "danger": "#e74c3c",        # Red
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
        # 1. Set window background color
        self.root.configure(bg=COLORS["bg_main"])

        # Data variables
        self.budget = 0.0
        self.balance = 0.0
        self.total_spent = 0.0

        # --- UI LAYOUT ---

        # Header Title
        tk.Label(root, text="Personal Finance Tracker", font=FONTS["header"], 
                 bg=COLORS["bg_main"], fg=COLORS["text_dark"]).pack(pady=(30, 20))

        # === MAIN INPUT CONTAINER FRAME ===
        # This creates a white box to hold the inputs, making it look cleaner.
        input_frame = tk.Frame(root, bg=COLORS["bg_container"], bd=1, relief=tk.RIDGE)
        input_frame.pack(padx=30, fill="x")

        # --- Budget Section inside the frame ---
        tk.Label(input_frame, text="Set Monthly Budget ($)", font=FONTS["label"], 
                 bg=COLORS["bg_container"], fg=COLORS["text_dark"]).pack(anchor="w", padx=20, pady=(20, 5))
        
        self.entry_budget = tk.Entry(input_frame, font=FONTS["entry"], bg="#ecf0f1", bd=0, highlightthickness=1)
        self.entry_budget.pack(padx=20, fill="x", ipady=5) # ipady adds internal padding
        
        # Styled Button
        btn_set = tk.Button(input_frame, text="SEAT BUDGET", font=FONTS["label"], bg=COLORS["primary_btn"], fg="white", 
                            relief=tk.FLAT, bd=0, padx=20, pady=5, command=self.set_budget)
        btn_set.pack(pady=15)

        # Separator line
        ttk.Separator(input_frame, orient='horizontal').pack(fill='x', padx=20, pady=10)

        # --- Expense Section inside the frame ---
        tk.Label(input_frame, text="Add New Expense ($)", font=FONTS["label"], 
                 bg=COLORS["bg_container"], fg=COLORS["text_dark"]).pack(anchor="w", padx=20, pady=(10, 5))
        
        self.entry_expense = tk.Entry(input_frame, font=FONTS["entry"], bg="#ecf0f1", bd=0, highlightthickness=1)
        self.entry_expense.pack(padx=20, fill="x", ipady=5)
        
        btn_add = tk.Button(input_frame, text="+ ADD EXPENSE", font=FONTS["label"], bg=COLORS["text_dark"], fg="white", 
                            relief=tk.FLAT, bd=0, padx=20, pady=5, command=self.add_expense)
        btn_add.pack(pady=(15, 30))

        # === DASHBOARD SECTION ===
        # A separate section at the bottom for results
        dashboard_frame = tk.Frame(root, bg=COLORS["bg_main"])
        dashboard_frame.pack(padx=30, pady=30, fill="x")

        tk.Label(dashboard_frame, text="Remaining Balance:", font=FONTS["label"], 
                 bg=COLORS["bg_main"], fg=COLORS["text_dark"]).pack()
        
        # The big balance number
        self.label_balance = tk.Label(dashboard_frame, text="$0.00", font=FONTS["balance"], 
                                      bg=COLORS["bg_main"], fg=COLORS["text_dark"])
        self.label_balance.pack(pady=5)

        # The Control Message Bar (starts hidden/empty)
        self.status_bar = tk.Label(root, text="Please set a budget to begin.", font=FONTS["message"], 
                                   bg="#dfe6e9", fg=COLORS["text_dark"], padding=10)
        self.status_bar.pack(fill="x", side="bottom")


    # --- Logic Functions (Same logic, just updating different UI elements) ---

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
            self.entry_expense.delete(0, tk.END) # Clear input box
            self.update_display()
        except ValueError:
             messagebox.showerror("Error", "Please enter a valid expense number.")

    def update_display(self):
        # Update the big balance number
        self.label_balance.config(text=f"${self.balance:.2f}")
        
        # Update the control message bar colors and text
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
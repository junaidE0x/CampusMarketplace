
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error
from decimal import Decimal, InvalidOperation

# ---------- DATABASE CONFIGURATION ----------
from config import DB_CONFIG

CATEGORIES = [
    "Books",
    "Electronics",
    "Stationery",
    "Hostel Essentials",
    "Clothing",
    "Sports",
    "Other"
]


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


class CampusMarketplace:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Marketplace")
        self.root.geometry("1050x650")
        self.root.minsize(850, 550)

        self.setup_style()
        self.create_widgets()
        self.load_listings()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            rowheight=30,
            font=("Arial", 10)
        )
        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )
        style.configure(
            "Title.TLabel",
            font=("Arial", 22, "bold")
        )

    def create_widgets(self):
        header = ttk.Frame(self.root, padding=15)
        header.pack(fill="x")

        ttk.Label(
            header,
            text="Campus Marketplace",
            style="Title.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Buy, sell and exchange items within your campus."
        ).pack(anchor="w", pady=(5, 0))

        # Listing form
        form = ttk.LabelFrame(
            self.root,
            text="Add a New Listing",
            padding=15
        )
        form.pack(fill="x", padx=15, pady=5)

        self.name_var = tk.StringVar()
        self.reg_var = tk.StringVar()
        self.item_var = tk.StringVar()
        self.category_var = tk.StringVar(value=CATEGORIES[0])
        self.price_var = tk.StringVar()

        ttk.Label(form, text="Student Name").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Entry(
            form, textvariable=self.name_var, width=28
        ).grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(form, text="Registration Number").grid(
            row=0, column=2, sticky="w", padx=5, pady=5
        )
        ttk.Entry(
            form, textvariable=self.reg_var, width=25
        ).grid(row=0, column=3, sticky="ew", padx=5, pady=5)

        ttk.Label(form, text="Item / Listing").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Entry(
            form, textvariable=self.item_var, width=28
        ).grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(form, text="Category").grid(
            row=1, column=2, sticky="w", padx=5, pady=5
        )
        ttk.Combobox(
            form,
            textvariable=self.category_var,
            values=CATEGORIES,
            state="readonly",
            width=22
        ).grid(row=1, column=3, sticky="ew", padx=5, pady=5)

        ttk.Label(form, text="Price (₹)").grid(
            row=2, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Entry(
            form, textvariable=self.price_var, width=28
        ).grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        ttk.Button(
            form,
            text="Add Listing",
            command=self.add_listing
        ).grid(row=2, column=2, padx=5, pady=8, sticky="ew")

        ttk.Button(
            form,
            text="Clear Form",
            command=self.clear_form
        ).grid(row=2, column=3, padx=5, pady=8, sticky="ew")

        for column in range(4):
            form.columnconfigure(column, weight=1)

        # Listings table
        table_frame = ttk.LabelFrame(
            self.root,
            text="Available Campus Listings",
            padding=10
        )
        table_frame.pack(
            fill="both", expand=True, padx=15, pady=10
        )

        columns = (
            "id", "student", "reg", "item",
            "category", "price", "date"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        headings = {
            "id": "ID",
            "student": "Student Name",
            "reg": "Registration No.",
            "item": "Item / Listing",
            "category": "Category",
            "price": "Price (₹)",
            "date": "Date Added"
        }

        widths = {
            "id": 45,
            "student": 130,
            "reg": 125,
            "item": 180,
            "category": 125,
            "price": 85,
            "date": 130
        }

        for column in columns:
            self.table.heading(
                column, text=headings[column]
            )
            self.table.column(
                column,
                width=widths[column],
                minwidth=40,
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(
            side="left", fill="both", expand=True
        )
        scrollbar.pack(side="right", fill="y")

        # Action buttons
        actions = ttk.Frame(self.root, padding=(15, 0, 15, 15))
        actions.pack(fill="x")

        ttk.Button(
            actions,
            text="Refresh Listings",
            command=self.load_listings
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            actions,
            text="Delete Selected Listing",
            command=self.delete_listing
        ).pack(side="left")

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(
            actions, textvariable=self.status_var
        ).pack(side="right")

    def add_listing(self):
        name = self.name_var.get().strip()
        reg = self.reg_var.get().strip()
        item = self.item_var.get().strip()
        category = self.category_var.get()

        if not all([name, reg, item, category, self.price_var.get().strip()]):
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        try:
            price = Decimal(self.price_var.get().strip())

            if not price.is_finite() or price < 0:
                raise InvalidOperation

            if price > Decimal("99999999.99"):
                raise InvalidOperation

        except InvalidOperation:
            messagebox.showerror(
                "Invalid Price",
                "Enter a valid non-negative price, such as 250 or 99.50."
            )
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

            sql = """
                INSERT INTO listings
                (student_name, registration_number,
                 item_name, category, price)
                VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(
                sql, (name, reg, item, category, price)
            )
            connection.commit()

            cursor.close()
            connection.close()

            self.clear_form()
            self.load_listings()

            messagebox.showinfo(
                "Success", "Listing added successfully!"
            )

        except Error as e:
            messagebox.showerror(
                "Database Error",
                f"Could not add listing.\n\n{e}"
            )

    def load_listings(self):
        for row in self.table.get_children():
            self.table.delete(row)

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                SELECT listing_id, student_name,
                       registration_number, item_name,
                       category, price, created_at
                FROM listings
                ORDER BY listing_id DESC
            """)

            for row in cursor.fetchall():
                listing_id, name, reg, item, category, price, date = row

                self.table.insert(
                    "",
                    "end",
                    values=(
                        listing_id,
                        name,
                        reg,
                        item,
                        category,
                        f"{price:.2f}",
                        date.strftime("%d-%m-%Y %H:%M")
                    )
                )

            cursor.close()
            connection.close()

            self.status_var.set(
                f"{len(self.table.get_children())} listing(s)"
            )

        except Error as e:
            messagebox.showerror(
                "Database Error",
                f"Could not load listings.\n\n{e}"
            )
            self.status_var.set("Database connection failed")

    def delete_listing(self):
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "No Selection",
                "Please select a listing to delete."
            )
            return

        values = self.table.item(selected[0], "values")
        listing_id = values[0]

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Delete listing ID {listing_id}?"
        )

        if not confirm:
            return

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM listings WHERE listing_id = %s",
                (listing_id,)
            )
            connection.commit()

            cursor.close()
            connection.close()

            self.load_listings()

        except Error as e:
            messagebox.showerror(
                "Database Error",
                f"Could not delete listing.\n\n{e}"
            )

    def clear_form(self):
        self.name_var.set("")
        self.reg_var.set("")
        self.item_var.set("")
        self.category_var.set(CATEGORIES[0])
        self.price_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CampusMarketplace(root)
    root.mainloop()

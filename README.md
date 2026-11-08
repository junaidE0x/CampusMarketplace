# 🛒 Campus Marketplace

A desktop-based marketplace application built using **Python, Tkinter, and MySQL**, designed to help students buy and sell items within their college campus.

Students can create listings for books, electronics, stationery, hostel essentials, clothing, sports equipment, and other items.

## ✨ Features

- **Add Listings:** Create new listings with student details and item information.
- **Student Information:** Store student name and registration number.
- **Category Selection:** Organize items into predefined categories.
- **Price Management:** Set item prices in Indian Rupees (INR).
- **View Listings:** Display all available listings in a structured table.
- **Delete Listings:** Remove selected listings from the marketplace.
- **Refresh Listings:** Retrieve the latest records from the database.
- **Persistent Storage:** Store marketplace data using MySQL.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Desktop graphical user interface |
| MySQL | Relational database |
| MySQL Connector | Python–MySQL connectivity |
| python-dotenv | Environment variable management |
| VS Code | Development environment |
| MySQL Workbench | Database management |

## 📁 Project Structure

```text
CampusMarketplace/
│
├── app/
│   ├── campus_marketplace.py
│   └── config.py
│
├── database/
│   └── schema.sql
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### Prerequisites

Make sure you have installed:

- Python 3
- MySQL Server
- MySQL Workbench
- Git

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd CampusMarketplace
```

### 2. Create a virtual environment

```bash
py -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 4. Configure the MySQL database

1. Open MySQL Workbench.
2. Connect to your local MySQL Server.
3. Open `database/schema.sql`.
4. Execute the SQL script.
5. Verify that the `campus_marketplace` database and `listings` table have been created.

### 5. Configure environment variables

Create a `.env` file in the project root directory.

Use `.env.example` as a reference:

```env
DB_HOST=localhost
DB_USER=campus_app
DB_PASSWORD=your_mysql_password
DB_NAME=campus_marketplace
```

Replace the placeholder password with your MySQL application user's password.

**Note:** Never upload your actual `.env` file or database credentials to GitHub.

### 6. Run the application

From the project root directory, execute:

```powershell
py .\app\campus_marketplace.py
```

The Campus Marketplace desktop application should now launch.

## 🗄️ Database Schema

The application uses a MySQL table named `listings`.

| Column | Data Type | Description |
|---|---|---|
| listing_id | INT | Unique listing identifier |
| student_name | VARCHAR(100) | Student's name |
| registration_number | VARCHAR(30) | Student registration number |
| item_name | VARCHAR(150) | Name of the listed item |
| category | ENUM | Item category |
| price | DECIMAL(10,2) | Item price |
| created_at | TIMESTAMP | Listing creation date and time |

## 🚀 Future Improvements

- Student authentication and registration.
- Search and filter functionality.
- Item image uploads.
- Edit and update existing listings.
- Student-to-student messaging.
- Item availability status.
- Purchase and transaction management.

## 🎯 Project Objective

The objective of this project is to develop a simple and accessible campus-based marketplace while demonstrating Python GUI development, object-oriented programming, SQL database management, and Python–MySQL integration.

## 👨‍💻 Author

**Junaid**

Developed as a Python and MySQL desktop application project.

---

*Built with Python and MySQL ❤️*
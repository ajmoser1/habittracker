import sqlite3
from datetime import datetime



DB_PATH = "habits.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            frequency TEXT NOT NULL DEFAULT 'daily',
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def create_habit(name, description=None, frequency="daily"):
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO habits (name, description, frequency, created_at) VALUES (?, ?, ?, ?)",
            (name, description, frequency, datetime.now().isoformat()),
        )
        conn.commit()
        print(f"Habit '{name}' created successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: A habit named '{name}' already exists.")
    finally:
        conn.close()

def read_habits(frequency=None):
    conn = get_connection()
    cursor = conn.cursor()
    if frequency is None:
        cursor.execute("SELECT * FROM habits")
        habits = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM habits WHERE frequency = ?", (frequency,))
        habits = cursor.fetchall()
    for habit in habits:
        print("-" * 90)
        print(f"{habit['name']} - {habit['description']} - {habit['frequency']}")
    print("-" * 90)
    conn.close()

def update_habit(name, description, frequency):
    conn = get_connection()
    fields = []
    values = []
    try:
        if description is not None: 
            fields.append("description = ?")
            values.append(description)
        if frequency is not None: 
            fields.append("frequency = ?")
            values.append(frequency)
        if not fields:
            print("No fields to update.")
            conn.close()
            return
        query = "UPDATE habits SET " + ", ".join(fields) + " WHERE name = ?"
        values.append(name)
        conn.execute(query, values)
        conn.commit()
        print(f"Habit '{name}' updated successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: A habit named '{name}' already exists.")
    except sqlite3.IntegrityError:
        print(f"Error: Habit '{name}' does not exist.")
    
    finally:
        conn.close()

def delete_habit(name):
    conn = get_connection()
    try:
        conn.execute("DELETE FROM habits WHERE name = ?", (name,))
        conn.commit()
        print(f"Habit '{name}' deleted successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Habit '{name}' does not exist.")
    finally:
        conn.close()

def wipe_habits():
    conn = get_connection()
    try: 
        conn.execute("DELETE FROM habits")
        conn.commit()
        print("All habits deleted successfully.")
    except sqlite3.IntegrityError:
        print("Error: No habits to delete.")
    finally:
        conn.close()

def main():
    init_db()
    while True:
        print("\n--- Habit Tracker ---")
        print("1. Create a habit")
        print("2. View all habits")
        print("3. Update a habit")
        print("4. Delete a habit")
        print("5. Wipe all habits")
        print("6. Quit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            name = input("Habit name: ")
            description = input("Description (or press Enter to skip): ") or None
            frequency = input("Frequency (daily/weekly/monthly): ") or "daily"
            create_habit(name, description, frequency)
        elif choice == "2":
            frequency = input("Filter by frequency (daily/weekly/monthly, or press Enter for all): ") or None
            read_habits(frequency)
        elif choice == "3":
            name = input("Name of the habit to update: ")
            description = input("New description (or press Enter to skip): ") or None
            frequency = input("New frequency (daily/weekly/monthly, or press Enter to skip): ") or None
            update_habit(name, description, frequency)
        elif choice == "4":
            name = input("Name of the habit to delete: ")
            delete_habit(name)
        elif choice == "5":
            confirm = input("Are you sure you want to delete ALL habits? (y/n): ")
            if confirm.lower() == "y":
                wipe_habits()
            else:
                print("Cancelled.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

import csv
import re

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def is_valid_email(email):
csv_file_path = "friends.csv"  # Replace with your CSV file path

try:
    with open(csv_file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)

        print("List of Friends and Their Email IDs:")
      
        for row in reader:
            if len(row) == 2:
                friend_name, friend_email = row
                if is_valid_email(friend_email):
                    print(f"Name: {friend_name}, Email: {friend_email} (Valid)")
                else:
                    print(f"Name: {friend_name}, Email: {friend_email} (Invalid)")
            else:
                print("Invalid row format:", row)
except FileNotFoundError:
    print("File not found:", csv_file_path)
except Exception as e:
    print("An error occurred:", str(e))

# app.py
# Simple backend example for admin system

def get_users():
    users = [
        {"id": 1, "name": "Admin"},
        {"id": 2, "name": "User"}
    ]
    return users

if __name__ == "__main__":
    for user in get_users():
        print(user)

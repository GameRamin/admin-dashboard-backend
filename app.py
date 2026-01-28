# app.py
# Simple backend example for admin system

def get_users():
    return [
        {"id": 1, "name": "Admin", "role": "admin"},
        {"id": 2, "name": "User", "role": "user"}
    ]

def add_user(name, role="user"):
    users = get_users()
    new_id = len(users) + 1
    users.append({"id": new_id, "name": name, "role": role})
    return users

if __name__ == "__main__":
    users = get_users()
    for u in users:
        print(u)

print("Testing table.py")

from app.table import insert_user, get_all_users

insert_user("Simran", "simran@test.com")
insert_user("ABC", "ABC@example.com")
insert_user("CBA", "CBA@example.com")

users = get_all_users()
print(users)

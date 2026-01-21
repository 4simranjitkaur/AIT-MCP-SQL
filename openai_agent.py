import requests

BASE_URL = "http://127.0.0.1:8000"

# ---------------- STEP 1: LOGIN ----------------
username = input("Enter username: ")
password = input("Enter password: ")

login_response = requests.post(
    f"{BASE_URL}/login",
    data={
        "username": username,
        "password": password
    }
)

if login_response.status_code != 200:
    print("Login failed:", login_response.text)
    exit()

token = login_response.json()["access_token"]
print("Login successful. Token received.")

# ---------------- STEP 2: CREATE USER ----------------
name = input("Enter name: ")
email = input("Enter email: ")

headers = {
    "Authorization": f"Bearer {token}"
}

create_response = requests.post(
    f"{BASE_URL}/users",
    params={
        "name": name,
        "email": email
    },
    headers=headers
)

print("Response:", create_response.json())

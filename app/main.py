from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth_file import authenticate_user, create_access_token, get_current_user, admin_only
from datetime import timedelta
from app.query import insert_user   

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Backend running successfully"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={
            "sub": user["username"],
            "role": user["role"]
        },
        expires_delta=timedelta(minutes=30)
    )

    return {"access_token": token, "token_type": "bearer"}


@app.post("/users")
def create_user(
    name: str,
    email: str,
    current_user=Depends(get_current_user)
):
    insert_user(name, email)
    return {"message": "User created successfully"}

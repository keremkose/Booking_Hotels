from app.main import app
from fastapi.testclient import TestClient

client= TestClient(app)

# def test_auth_error():
#     response= client.post("/token",data={"username":"" , "password": ""})
#     access_token=response.json().get("access_token")
#     assert access_token == None
    
def test_get_all_users():
    response= client.get("/user")
    assert response.status_code==200
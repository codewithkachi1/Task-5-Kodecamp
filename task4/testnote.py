from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes/", params={"title": "Test Note", "content": "This is a test note"})
    assert response.status_code == 200
    assert response.json() == {"message": "Note created successfully"}

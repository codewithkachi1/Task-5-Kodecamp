from fastapi import FastAPI, HTTPException
from typing import Optional
from models import Contact

app = FastAPI()

contacts = {}

@app.post("/contacts/")
def create_contact(name: str, phone: str, email: str):
    if name in contacts:
        raise HTTPException(status_code=400, detail="Contact already exists")
    contacts[name] = Contact(name, phone, email).to_dict()
    return {"message": "Contact created successfully"}

@app.get("/contacts/")
def get_contacts(name: Optional[str] = None):
    if name:
        contact = contacts.get(name)
        if contact:
            return contact
        else:
            raise HTTPException(status_code=404, detail="Contact not found")
    return list(contacts.values())

@app.post("/contacts/{name}")
def update_contact(name: str, phone: Optional[str] = None, email: Optional[str] = None):
    if name not in contacts:
        raise HTTPException(status_code=404, detail="Contact not found")
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    return {"message": "Contact updated successfully"}


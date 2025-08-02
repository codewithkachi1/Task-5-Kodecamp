from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

NOTES_DIR = "notes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

@app.post("/notes/")
async def create_note(title: str, content: str):
    try:
        with open(f"{NOTES_DIR}/{title}.txt", "w") as f:
            f.write(content)
        return {"message": "Note created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/notes/{title}")
async def read_note(title: str):
    try:
        with open(f"{NOTES_DIR}/{title}.txt", "r") as f:
            content = f.read()
        return {"title": title, "content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from job_application import JobApplication
from file_handler import save_to_json, load_from_json

app = FastAPI()

class JobApplicationRequest(BaseModel):
    name: str
    company: str
    position: str
    status: str

applications = load_from_json("applications.json")

@app.post("/applications/")
def create_application(request: JobApplicationRequest):
    try:
        application = JobApplication(request.name, request.company, request.position, request.status)
        applications.append(application)
        save_to_json(applications, "applications.json")
        return application.to_dict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/applications/")
def get_applications():
    return [application.to_dict() for application in applications]

@app.get("/applications/search")
def search_applications(status: str):
    try:
        result = [application.to_dict() for application in applications if application.status == status]
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

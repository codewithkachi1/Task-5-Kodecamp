import json
from job_application import JobApplication


def save_to_json(applications, filename):
    data = [application.to_dict() for application in applications]
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_from_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [JobApplication.from_dict(application_dict) for application_dict in data]
    except FileNotFoundError:
        return []

class JobApplication:
    def __init__(self, name, company, position, status):
        self.name = name
        self.company = company
        self.position = position
        self.status = status

    def to_dict(self):
        return {
            "name": self.name,
            "company": self.company,
            "position": self.position,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, application_dict):
        return cls(
            application_dict["name"],
            application_dict["company"],
            application_dict["position"],
            application_dict["status"]
        )

class Student:
    def __init__(self, name, subject_scores):
        self.name = name
        self.subject_scores = subject_scores
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        return sum(self.subject_scores.values()) / len(self.subject_scores)

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "subject_scores": self.subject_scores,
            "average": self.average,
            "grade": self.grade
        }

    @classmethod
    def from_dict(cls, student_dict):
        return cls(
            student_dict["name"],
            student_dict["subject_scores"]
        )



import json 
from typing import ClassVar
from pydantic import BaseModel

class Grades(BaseModel):
   
    quiz_1: float = 0
    quiz_2: float = 0
    midterm: float = 0
    project: float = 0
    final: float = 0

    file_path: ClassVar[str] = 'grades.json'

    @classmethod
    def from_json_file(cls, file_path: str = None):
        path_to_use = file_path or cls.file_path
        
        try:
            with open(path_to_use, 'r') as file:
                data = json.load(file)
            return cls.model_validate(data)
        except FileNotFoundError:
            print(f"Warning: The file '{path_to_use}' was not found.")
            return cls()

    def __str__(self) -> str:
        """
        Returns a formatted string of the grades.
        """
        grades_list = []
        if self.quiz_1 > 0:
            grades_list.append(f'Quiz 1: {self.quiz_1}')
        if self.quiz_2 > 0:
            grades_list.append(f'Quiz 2: {self.quiz_2}')
        if self.midterm > 0:
            grades_list.append(f'Midterm Exam: {self.midterm}')
        if self.project > 0:
            grades_list.append(f'Project: {self.project}')
        if self.final > 0:
            grades_list.append(f'Final Exam: {self.final}')
        
        if not grades_list:
            return 'No grades submitted yet.'
        else:
            return 'GRADES --- ' + ', '.join(grades_list)
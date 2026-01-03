import sys
import os

# Get absolute path of the project root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Add project root to Python path
sys.path.insert(0, PROJECT_ROOT)

from src.matching import rank_schools_for_student

student = {
    "name": "John Doe",
    "gpa": 3.4,
    "budget": 15000,
    "field": "Computer Science",
    "preferred_countries": ["Canada", "UK"]
}

schools = [
    {
        "name": "University of Toronto",
        "country": "Canada",
        "min_gpa": 3.2,
        "tuition": 14000,
        "fields": ["Computer Science", "Engineering"]
    },
    {
        "name": "University of Manchester",
        "country": "UK",
        "min_gpa": 3.5,
        "tuition": 16000,
        "fields": ["Computer Science", "Data Science"]
    }
]

results = rank_schools_for_student(student, schools)

for school, score in results:
    print(f"{school}: {score}")

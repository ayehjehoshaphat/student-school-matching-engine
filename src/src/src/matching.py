from src.scoring import score_student_school

def rank_schools_for_student(student, schools):
    """
    Rank schools for a given student based on compatibility score.
    """

    scored_schools = []

    for school in schools:
        score = score_student_school(student, school)
        scored_schools.append((school["name"], score))

    ranked = sorted(scored_schools, key=lambda x: x[1], reverse=True)

    return ranked

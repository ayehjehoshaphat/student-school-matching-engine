def score_student_school(student, school):
    """
    Compute a compatibility score between a student and a school.
    """

    score = 0

    # Academic fit
    if student["gpa"] >= school["min_gpa"]:
        score += 40

    # Budget fit
    if student["budget"] >= school["tuition"]:
        score += 30

    # Country preference
    if school["country"] in student["preferred_countries"]:
        score += 20

    # Field of study match
    if student["field"] in school["fields"]:
        score += 10

    return score

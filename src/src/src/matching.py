from typing import Dict, List, Tuple


def score_school(student: Dict, school: Dict) -> Tuple[int, Dict]:
    """
    Compute a compatibility score between a student and a school.
    Returns both the score and an explanation dictionary.
    """

    score = 0
    explanation = {}

    # GPA compatibility
    if student["gpa"] >= school["min_gpa"]:
        score += 40
        explanation["gpa"] = "meets requirement"
    else:
        explanation["gpa"] = "below requirement"

    # Budget compatibility
    if student["budget"] >= school["tuition"]:
        score += 30
        explanation["budget"] = "within budget"
    else:
        explanation["budget"] = "exceeds budget"

    # Field match
    if student["field"] in school["fields"]:
        score += 20
        explanation["field"] = "field supported"
    else:
        explanation["field"] = "field not supported"

    # Country preference
    if school["country"] in student["preferred_countries"]:
        score += 10
        explanation["country"] = "preferred country"
    else:
        explanation["country"] = "non-preferred country"

    return score, explanation


def rank_schools_for_student(
    student: Dict, schools: List[Dict]
) -> List[Tuple[str, int, Dict]]:
    """
    Rank schools by compatibility score.
    """

    ranked = []

    for school in schools:
        score, explanation = score_school(student, school)
        ranked.append((school["name"], score, explanation))

    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked

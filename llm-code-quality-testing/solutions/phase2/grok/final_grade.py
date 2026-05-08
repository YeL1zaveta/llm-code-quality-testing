def calculate_final_grade(points, attendance):
    if not isinstance(points, (int, float)) or not isinstance(attendance, (int, float)):
        return False
    if points < 0 or points > 100 or attendance < 0 or attendance > 100:
        return False
    if attendance < 50:
        return 2
    if points >= 90:
        return 5
    elif points >= 75:
        return 4
    elif points >= 60:
        return 3
    else:
        return 2
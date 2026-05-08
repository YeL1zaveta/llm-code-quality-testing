def calculate_final_grade(points, attendance):
    if not isinstance(points, (int, float)) or not isinstance(attendance, (int, float)):
        return None

    if not (0 <= points <= 100) or not (0 <= attendance <= 100):
        return None

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
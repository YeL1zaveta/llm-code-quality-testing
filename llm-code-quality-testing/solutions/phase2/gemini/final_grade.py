def calculate_final_grade(points, attendance):
    # Check for valid types (None check is covered by isinstance)
    if not isinstance(points, (int, float)) or not isinstance(attendance, (int, float)):
        return False

    # Check for valid ranges
    if not (0 <= points <= 100) or not (0 <= attendance <= 100):
        return False

    # Attendance threshold check
    if attendance < 50:
        return 2

    # Grading logic based on points
    if 90 <= points <= 100:
        return 5
    elif 75 <= points < 90:
        return 4
    elif 60 <= points < 75:
        return 3
    else:
        return 2
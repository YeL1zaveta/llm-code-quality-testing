def calculate_final_grade(points, attendance):
    # Validate inputs
    if not isinstance(points, (int, float)) or not isinstance(attendance, (int, float)):
        raise ValueError("Both points and attendance must be numbers")

    if points < 0 or points > 100:
        raise ValueError("Points must be between 0 and 100 inclusive")

    if attendance < 0 or attendance > 100:
        raise ValueError("Attendance must be between 0 and 100 inclusive")

    # Check attendance requirement
    if attendance < 50:
        return 2

    # Calculate grade based on points
    if 90 <= points <= 100:
        return 5
    elif 75 <= points <= 89:
        return 4
    elif 60 <= points <= 74:
        return 3
    else:
        return 2
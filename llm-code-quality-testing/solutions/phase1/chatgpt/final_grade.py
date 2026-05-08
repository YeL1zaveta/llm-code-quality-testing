def calculate_final_grade(points, attendance):
    try:
        # Validate types
        if not isinstance(points, (int, float)) or not isinstance(attendance, (int, float)):
            raise ValueError("Points and attendance must be numeric.")

        # Validate ranges
        if not (0 <= points <= 100) or not (0 <= attendance <= 100):
            raise ValueError("Points and attendance must be between 0 and 100.")

        # Attendance rule
        if attendance < 50:
            return 2

        # Grade assignment
        if 90 <= points <= 100:
            return 5
        elif 75 <= points < 90:
            return 4
        elif 60 <= points < 75:
            return 3
        else:
            return 2

    except Exception:
        return None
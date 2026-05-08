import math

def calculate_final_grade(points, attendance):
    # Validate types (reject bool explicitly)
    if not (isinstance(points, (int, float)) and not isinstance(points, bool)):
        return False
    if not (isinstance(attendance, (int, float)) and not isinstance(attendance, bool)):
        return False

    # Check for NaN
    if math.isnan(points) or math.isnan(attendance):
        return False

    # Validate ranges
    if not (0 <= points <= 100 and 0 <= attendance <= 100):
        return False

    # Attendance rule
    if attendance < 50:
        return 2

    # Grade based on points
    if 90 <= points <= 100:
        return 5
    elif 75 <= points <= 89:
        return 4
    elif 60 <= points <= 74:
        return 3
    else:
        return 2
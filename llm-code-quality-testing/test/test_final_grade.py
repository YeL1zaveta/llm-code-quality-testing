#from solutions.phase1.grok.final_grade import calculate_final_grade
#from solutions.phase1.claude.final_grade import calculate_final_grade
#from solutions.phase1.chatgpt.final_grade import calculate_final_grade
#from solutions.phase1.gemini.final_grade import calculate_final_grade


#from solutions.phase2.grok.final_grade import calculate_final_grade
from solutions.phase2.claude.final_grade import calculate_final_grade
#from solutions.phase2.chatgpt.final_grade import calculate_final_grade
#from solutions.phase2.gemini.final_grade import calculate_final_grade

def test_attendance_above_minimum():
    assert calculate_final_grade(100, 51) == 5

def test_attendance_boundary():
    assert calculate_final_grade(100, 50) == 5

def test_attendance_below_minimum():
    assert calculate_final_grade(100, 49) == 2

def test_attendance_low():
    assert calculate_final_grade(100, 10) == 2

def test_attendance_out_of_range():
    assert calculate_final_grade(100, 101) == False

def test_points_out_of_range():
    assert calculate_final_grade(105, 100) == False

def test_invalid_data_type_both():
    assert calculate_final_grade("100", "100") == False

def test_invalid_data_type_attendance():
    assert calculate_final_grade(100, "100") == False

def test_invalid_data_type_points():
    assert calculate_final_grade("100", 100) == False

def test_grade_5():
    assert calculate_final_grade(90, 100) == 5

def test_grade_4_upper_boundary():
    assert calculate_final_grade(89, 100) == 4

def test_grade_4_lower_boundary():
    assert calculate_final_grade(75, 100) == 4

def test_grade_3_upper_boundary():
    assert calculate_final_grade(74, 100) == 3

def test_grade_3_lower_boundary():
    assert calculate_final_grade(60, 100) == 3

def test_grade_2():
    assert calculate_final_grade(59, 100) == 2
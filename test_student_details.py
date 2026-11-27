from student_details import student_details

def test_student():
    result = student_details(
        "Ravi",
        "01FE25BCA001",
        "ABC College",
        "Bangalore",
        "ravi@gmail.com"
    )

    assert result["name"] == "Ravi"
    assert result["usn"] == "01FE25BCA001"
    assert result["college"] == "ABC College"
    assert result["city"] == "Bangalore"
    assert result["email"] == "ravi@gmail.com"
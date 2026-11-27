from student import student_details

def test_student():
    result = student_details(
        "Ravi",
        "01FE25BCA001",
        "ABC College",
        "Bangalore"
    )

    assert result["name"] == "Ravi"
    assert result["usn"] == "01FE25BCA001"
    assert result["college"] == "ABC College"
    assert result["city"] == "Bangalore"
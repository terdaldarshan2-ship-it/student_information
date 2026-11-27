def student_details(name, usn, college, city):
    return {
        "name": name,
        "usn": usn,
        "college": college,
        "city": city
    }

if __name__ == "__main__":
    result = student_details(
        "Ravi",
        "01FE25BCA001",
        "ABC College",
        "Bangalore"
    )

    print(result)

    def student_details(name,usn,college,city,email):
    return {
        "name":name,
        "usn":usn,
        "college":college,
        "city":city,
        "email":email
    }

if __name__ == "__main__":
    print(student_details("Ravi", "01FE25BCA001", "ABC College", "Bangalore", "ravi@gmail.com"))
   
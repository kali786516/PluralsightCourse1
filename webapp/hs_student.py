from webapp.student import Student

class HighSchoolStudent(Student):

    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a High school student"

    def get_name_captilize(self):
        original_value = super().get_name_captilize()
        return original_value + "-HS"
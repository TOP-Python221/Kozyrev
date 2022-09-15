from enum import Enum


class Gender(Enum):
    MALE = 'man'
    FEMALE = 'woman'


class Degree(Enum):
    BACHELOR = 'Bac'
    MASTER = 'Mas'
    DOCTOR = 'Doc'


class Person:
    def __init__(self, name: str,
                 birthdate: str,
                 gender: Gender):
        self.gender = gender
        self.birthdate = birthdate
        self.__name = name

    @property
    def name(self):
        return self.__name


class Employee(Person):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 gender: Gender,
                 position: str,
                 salary: int):
        super().__init__(name, birthdate, gender)
        self.position = position
        self.salary = salary


class Administrator(Employee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 gender: Gender,
                 position: str,
                 salary: int,
                 supervisor: None,
                 subordinates=None):
        super().__init__(name, birthdate, gender, position, salary)
        self.supervisor = supervisor
        if subordinates is None:
            subordinates = []
        self.subordinates = subordinates


class ProfessionalEmployee(Employee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 gender: Gender,
                 position: str,
                 salary: int,
                 degree: Degree.BACHELOR,
                 experience: int = 0):
        super().__init__(name, birthdate, gender, position, salary)
        self.degree = degree
        self.experience = experience


class Teacher(ProfessionalEmployee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 gender: Gender,
                 position: str,
                 salary: int,
                 degree: Degree = Degree.MASTER,
                 professorship: bool = False,
                 experience: int = 0,
                 course=None):
        super().__init__(name, birthdate, gender, position, salary, experience)
        if course is None:
            course = []
        self.__course = course
        self.professorship = professorship
        self.degree = degree

    def add_course(self, course: str):
        self.__course.append(course)
        # self.__rem_course.remove(course)


class Researcher(ProfessionalEmployee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 gender: Gender,
                 position: str,
                 salary: int,
                 experience: int = 0,
                 degree: Degree = Degree.MASTER):
        super().__init__(name, birthdate, gender, position, salary, experience)
        self.degree = degree


class GeneralPersonnel(Employee):
    pass


class SecurityPersonnel(Employee):
    pass


class EducationForms(Enum):
    INTRAMURAL = 'Intra'
    EXTRAMURAL = 'Extra'
    REMOTE = 'Rem'


class Student(Person):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 gender: Gender,
                 form: EducationForms.INTRAMURAL,
                 year: int = 1,
                 average_grade: float = -1):
        super().__init__(name, birthdate, gender)
        self.average_grade = average_grade
        self.year = year
        self.form = form

    def __str__(self):
        pass

    def year_increment(self):
        pass


class OrganizationLevel:
    def __init__(self,
                 name: str,
                 head: Administrator,
                 employees: list[Employee],
                 address: str
                 # budget
                 ):
        self.address = address
        self.__employees = employees
        self.__head = head
        self.name = name

    def __str__(self):
        pass

    def change_head(self, Administrator):
        pass

    def hire_employee(self, Employee):
        pass

    def fire_employee(self, Employee):
        pass

    def set_annual_budget(self, amount: int):
        pass





class Department:
    def __init__(self,
                 groups: dict[str, Group]):
        self.groups = groups


class Institute:
    def __init__(self,
                 departments: dict[str, Department]):
        self.departments = departments


class University:
    def __init__(self,
                 institutes: dict[str, Institute]):
        self.institutes = institutes

    def __str__(self):
        pass


class Group:
    def __init__(self,
                 number_group: str,
                 specialty: str):
        self.number_group = number_group
        self.specialty = specialty

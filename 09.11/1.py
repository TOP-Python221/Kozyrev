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
        # ОТВЕТИТЬ: это очень хорошо! а вы понимаете, что сделали с этим атрибутом?
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
                 # ИСПРАВИТЬ: здесь вы указали None в качестве аннотации типа, а не значения по умолчанию
                 # ИСПОЛЬЗОВАТЬ: когда нам нужно аннотировать создаваемый класс, то мы можем взять имя этого класса в кавычки, чтобы избежать ошибок
                 supervisor: 'Administrator' = None,
                 subordinates: list[Employee] = None):
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
                 degree: Degree = Degree.BACHELOR,
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
                 courses: list[str] = None):
        # ИСПОЛЬЗОВАТЬ: лучше отправить полученный аргумент degree в конструктор надкласса, чем переопределять поле — так вы и ошибок при вызове родительского конструктора избежите, и значение по умолчанию переопределите
        super().__init__(name, birthdate, gender, position, salary, degree, experience)
        if courses is None:
            courses = []
        # ИСПОЛЬЗОВАТЬ: квадрат — это частный (private) атрибут — мы намекаем, что не стоит к этому полю обращаться напрямую, но если очень надо...
        self._course = courses
        self.professorship = professorship
        # УДАЛИТЬ: это поле определяется в конструкторе надкласса, здесь не нужно его переопределять
        self.degree = degree

    def add_course(self, course: str):
        self._course.append(course)
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
        # ИСПРАВИТЬ: вы передаете аргумент experience в параметр degree родительского конструктора
        super().__init__(name, birthdate, gender, position, salary, experience)
        # УДАЛИТЬ: это поле определяется в конструкторе надкласса, здесь не нужно его переопределять
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
                 address: str,
                 budget: int
                 ):
        self.address = address
        self._employees = employees
        self._head = head
        self.name = name
        # ИСПОЛЬЗОВАТЬ: а ромб — это защищённый (protected) атрибут — для него включается механизм искажения имён
        self.__budget = budget

    def __str__(self):
        pass

    # ИСПРАВИТЬ: в этом и двух следующих методах: имена классов у вас использованы в качестве параметров, придумайте другие имена параметров, а имена классов используйте для аннотаций
    def change_head(self, Administrator):
        pass

    def hire_employee(self, Employee):
        pass

    def fire_employee(self, Employee):
        pass

    def set_annual_budget(self, amount: int):
        pass


class Group:
    def __init__(self,
                 number_group: str,
                 specialty: str):
        self.number_group = number_group
        self.specialty = specialty


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


# ДОБАВИТЬ: все описанные методы (свои тоже предлагать не возбраняется); добавить код тех, для которых это возможно


# ИТОГ: хорошо, но мало — 8/12


# СДЕЛАТЬ: ждём вторую часть задания!

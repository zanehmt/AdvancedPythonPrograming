


class Nematode:
    def __init__(self, bodyLength: float, gender: str, age: int) -> None:
        self.bodyLength = bodyLength
        self.gender = gender
        self.age = age

    def __str__(self):
        return "Nematode details:\nbody length : {}\ngender : {}\nage :{}".format(self.bodyLength, self.gender,
                                                                                  self.age)

    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__, self.bodyLength, self.gender, self.age)


class Member:
    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__, self.name, self.address, self.email)


class Faculty(Member):
    def __init__(self, name: str, address: str, email: str,
                 faculty_num: str) -> None:
        super().__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []

    def __repr__(self):
        return "{0}({1},{2},{3},{4},{5})".format(self.__class__.__name__, self.name, self.address, self.email,
                                                 self.faculty_number, self.courses_teaching)


class Student(Member):
    def __init__(self, name: str, address: str, email: str,
                 student_num: str) -> None:
        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = ['Python','Java']
        self.courses_taking = ['Python']

    def __str__(self):
        return "Name of the student : {0} \nAddress : {1} \nemail : {2} \nStudent number : {3} \nCourses_taken : {4} \nCourses_taking : {5} \n".format(
            self.name, self.address, self.email, self.student_number, self.courses_taken, self.courses_taking)

    def __repr__(self):
        return "{0}({1},{2},{3},{4},{5},{6})".format(self.__class__.__name__, self.name, self.address, self.email,
                                                     self.student_number, self.courses_taken, self.courses_taking)

class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        if isinstance(other, Country):
            return self.area > other.area
        else:
            print("Both objects need to be from class Country")
            return -1

    def population_density(self):
        return (self.population / self.area)

    def __str__(self):
        return ("{0} has a population of {1} and its area is {2} square kilometers.".format(self.name, self.population,
                                                                                            self.area))

    def __repr__(self):
        return "Country('{0}', {1}, {2})".format(self.name, self.population, self.area)



class Continent:
    def __init__(self,name,countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        sum = 0
        for country in self.countries:
            sum += country.population
        return sum

    def __str__(self):
        string = self.name + '\n'
        for country in self.countries:
            string += '{} has a population of {} and is {} square km.'.format(country.name, country.population, country.area) + '\n'
        return string







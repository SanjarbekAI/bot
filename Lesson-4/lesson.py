from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name'])

persons = []


person1 = Person('Sanjar', 'Tursunov')
persons.append(person1)


from datetime import datetime

print(datetime.year)
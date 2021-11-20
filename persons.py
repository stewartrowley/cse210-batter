class Person:
    def __init__(self) -> None:
        self._first_name = ''
        self._last_name = ''
    
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def make_concat_string(self):
        name = f'{self._first_name} {self._last_name}'
        return name

def main():
    
    person = Person()
    person.set_first_name('John')
    person.set_last_name('Williams')

    person2 = Person()
    person2.set_first_name('Tyler')
    person2.set_last_name('Jackson')

    person3 = Person()
    person3.set_first_name('Riley')
    person3.set_last_name('Grant')

    person_list = []

    person_list.append(person.make_concat_string())
    person_list.append(person2.make_concat_string())
    person_list.append(person3.make_concat_string())

    for i in person_list:
        print(i)




if __name__ == "__main__":
    main()


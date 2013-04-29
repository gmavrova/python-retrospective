class Person:

    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        self.father = father
        self.list_of_children = []
        for parent in [self.father, self.mother]:
            if parent:
                parent.list_of_children.append(self)

    def children(self, gender=None):
        if gender:
            return list(filter(lambda child: child.gender == gender,
                               self.list_of_children))
        else:
            return self.list_of_children

    def get_siblings(self, gender):
        siblings = set(self.mother.children(gender)
                       + self.father.children(gender))
        return list(siblings - {self})

    def get_brothers(self):
        return self.get_siblings('M')

    def get_sisters(self):
        return self.get_siblings('F')

    def is_direct_successor(self, other_person):
        return other_person in self.list_of_children

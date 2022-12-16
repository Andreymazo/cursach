class TeamIterator:
    def __init__(self, team):
        self.team = team
        self._index = 0

    def __next__(self):
        if self._index < (len(self.team._juniorMembers+self.team._seniorMembers)):
            if self._index < (len(self.team._juniorMembers)):
                    result = (self.team._juniorMembers[self._index], 'junior')
            else:
                    result = (self.team._seniorMembers[self._index - len(self.team._juniorMembers)], 'senior')
            self._index += 1
            return result
        raise StopIteration


class Team:
    """
    Хранит список джунов и синьоров, а также переопределяет метод __iter__().
    """

    def __init__(self):
        self._juniorMembers = list()
        self._seniorMembers = list()

    def add_junior_members(self, members):
        self._juniorMembers += members

    def add_senior_members(self, members):
        self._seniorMembers += members

    def __iter__(self):
        """ Возвращает объект-итератор """
        return TeamIterator(self)


def main():
    # создаем команду
    team = Team()
    # добавляем имена джунов
    team.add_junior_members(['Ivan', 'Mary', 'Nikita'])
    # добавляем имена синьоров
    team.add_senior_members(['Rita', 'Roma', 'Ramil'])

    print('*** Итерируемся по команде в цикле for ***')
    for member in team:
        print(member)

    print('*** Итерируемся по команде в цикле while ***')
    # Получаем итератор из итерируемого объекта - экземпляра класса Team
    iterator = iter(team)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break


if __name__ == '__main__':
    main()

# *** Итерируемся по команде в цикле for ***
#('Ivan', 'junior')
# ('Mary', 'junior')
# ('Nikita', 'junior')
# ('Rita', 'senior')
# ('Roma', 'senior')
# ('Ramil', 'senior')
# # *** Итерируемся по команде в цикле while ***
# ('Ivan', 'junior')
# ('Mary', 'junior')
# ('Nikita', 'junior')
# ('Rita', 'senior')
# ('Roma', 'senior')
# ('Ramil', 'senior')
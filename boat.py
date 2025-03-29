from oar import Oar
from anchor import Anchor
from typing import Literal

class Boat:
    """Класс, представляющий вёсельную лодку"""

    def __init__(self):
        self.oars = [Oar(), Oar()]  # Два весла
        self.anchor = Anchor()
        self.occupied_seats = 0  # Количество занятых мест
        self.in_water = False  # Лодка в воде или нет

    def row(self, direction: Literal["вперед", "назад", "влево", "вправо"]):
        """Гребля в заданном направлении"""
        if self.anchor.dropped:
            return "Невозможно грести: якорь опущен"

        return self.oars[0].row(direction)

    def drop_anchor(self):
        """Опустить якорь"""
        return self.anchor.drop()

    def lift_anchor(self):
        """Поднять якорь"""
        return self.anchor.lift()

    def apply_rope_tension(self, tension: int):
        """Применить нагрузку к веревке якоря"""
        return self.anchor.apply_rope_tension(tension)

    def throw_anchor(self, confirm=False):
        """Выбросить якорь с возможным подтверждением"""
        return self.anchor.throw_anchor(confirm)

    def sit(self, people: int):
        """Рассадить людей в лодке"""
        if people < 1 or people > 3:
            return "В лодке может быть от 1 до 3 человек"
        self.occupied_seats = people
        return f"В лодке {people} человек"

    def check_stability(self):
        """Проверка устойчивости лодки"""
        return "Лодка устойчива" if self.occupied_seats <= 3 else "Лодка перегружена!"

    def check_buoyancy(self):
        """Проверка плавучести лодки"""
        if not self.in_water:
            return "Лодка не в воде"
        if self.occupied_seats == 0:
            return "Лодка на плаву"
        elif self.occupied_seats > 3:
            return "Лодка перегружена и может утонуть"
        return "Лодка на плаву"

    def place_in_water(self):
        """Поместить лодку в воду"""
        self.in_water = True
        return "Лодка помещена в воду"

    def remove_from_water(self):
        """Удалить лодку из воды"""
        self.in_water = False
        return "Лодка убрана из воды"
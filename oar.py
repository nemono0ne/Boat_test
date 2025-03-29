from typing import Literal


class Oar:
    """Класс, представляющий весло"""

    def __init__(self):
        self.is_attached = True  # Весло вставлено в уключину

    def row(self, direction: Literal["вперед", "назад", "влево", "вправо"]):
        """Имитация гребли в указанном направлении"""
        if not self.is_attached:
            raise ValueError("Весло не закреплено в уключине")

        if direction in ["влево", "вправо"]:
            return f"Лодка поворачивает {direction}"
        return f"Лодка движется {direction}"
class Anchor:
    """Класс, представляющий якорь с веревкой"""
    def __init__(self):
        self.dropped = False  # Якорь изначально поднят
        self.rope_broken = False  # Изначально веревка не порвана
        self.anchored = False  # Лодка может быть закреплена якорем

    def drop(self):
        """Опустить якорь в воду"""
        if self.rope_broken:
            return "Невозможно опустить якорь: веревка порвана"
        if self.dropped:
            return "Якорь уже опущен"
        self.dropped = True
        self.anchored = True  # Лодка закреплена якорем
        return "Якорь опущен, лодка зафиксирована"

    def lift(self):
        """Поднять якорь из воды"""
        if self.rope_broken:
            return "Невозможно поднять якорь: веревка порвана"
        if not self.dropped:
            return "Якорь уже поднят"
        self.dropped = False
        self.anchored = False  # Лодка больше не закреплена
        return "Якорь поднят, лодка может двигаться"

    def apply_rope_tension(self, tension: int):
        """Применение нагрузки к веревке якоря"""
        if tension > 5:
            self.rope_broken = True
            return "Веревка порвалась!"
        return "Веревка натянута под умеренной нагрузкой"

    def check_rope(self):
        """Проверка состояния веревки якоря"""
        if self.rope_broken:
            return "Веревка порвалась!"
        return "Веревка в хорошем состоянии"

    def throw_anchor(self, confirm=False):
        """Выбросить якорь, если веревка порвана"""
        if self.rope_broken:
            if self.dropped:
                # Якорь уже опущен, веревка порвана, с ним нельзя взаимодействовать
                return "Веревка порвана, якорь утерян, с ним нельзя взаимодействовать."
            else:
                # Якорь в лодке, веревка порвана — можно выбросить якорь только с подтверждением
                if not confirm:
                    return "Веревка порвана, якорь в лодке. Вы хотите выбросить якорь навсегда? Подтвердите, чтобы выбросить."
                else:
                    # Якорь выбрасывается, лодка не закрепляется
                    self.dropped = False  # Якорь выбрасывается, снимаем его с лодки
                    self.anchored = False
                    return "Веревка порвана, якорь выброшен, лодка больше не закреплена."
        else:
            # Если веревка не порвана, вызываем drop для опускания якоря
            if self.dropped:
                return "Якорь уже опущен, лодка зафиксирована."
            else:
                # Якорь выбрасывается, если веревка цела и якорь в лодке
                return self.drop()  # Вызов функции drop_anchor для опускания якоря

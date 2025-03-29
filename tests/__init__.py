import pytest
from boat import Boat
from anchor import Anchor
from oar import Oar

@pytest.fixture
def boat():
    return Boat()

@pytest.fixture
def anchor_with_broken_rope():
    anchor = Anchor()
    anchor.apply_rope_tension(6)  # Порвать веревку
    return anchor

@pytest.fixture
def oar():
    return Oar()

# Тест для метода row, когда якорь опущен
def test_row_with_dropped_anchor(boat):
    boat.drop_anchor()  # Опускаем якорь
    result = boat.row("forward")
    assert result == "Невозможно грести: якорь опущен"

def test_row_without_dropped_anchor(boat):
    result = boat.row("forward")
    assert result == "Лодка движется forward"

def test_turn_left(boat):
    result = boat.row("turn_left")
    assert result == "Лодка поворачивает влево за счет правого весла"

def test_turn_right(boat):
    result = boat.row("turn_right")
    assert result == "Лодка поворачивает вправо за счет левого весла"

# Тесты для метода drop_anchor
def test_drop_anchor(boat):
    result = boat.drop_anchor()
    assert result == "Якорь опущен, лодка зафиксирована"

def test_drop_anchor_when_dropped(boat):
    boat.drop_anchor()
    result = boat.drop_anchor()
    assert result == "Якорь уже опущен"

# Тесты для метода lift_anchor
def test_lift_anchor(boat):
    boat.drop_anchor()
    result = boat.lift_anchor()
    assert result == "Якорь поднят, лодка может двигаться"

def test_lift_anchor_when_not_dropped(boat):
    result = boat.lift_anchor()
    assert result == "Якорь уже поднят"

def test_lift_anchor_when_rope_broken(boat, anchor_with_broken_rope):
    boat.anchor = anchor_with_broken_rope
    boat.drop_anchor()
    result = boat.lift_anchor()
    assert result == "Невозможно поднять якорь: веревка порвана"

# Тесты для метода apply_rope_tension
def test_apply_rope_tension(boat):
    result = boat.apply_rope_tension(3)
    assert result == "Веревка натянута под умеренной нагрузкой"

def test_apply_rope_tension_with_high_tension(boat):
    result = boat.apply_rope_tension(6)
    assert result == "Веревка порвалась!"

# Тесты для метода throw_anchor
def test_throw_anchor_when_rope_broken(boat, anchor_with_broken_rope):
    boat.anchor = anchor_with_broken_rope
    result = boat.throw_anchor()
    assert result == "Веревка порвана, якорь утерян, с ним нельзя взаимодействовать."

def test_throw_anchor_when_not_broken_rope(boat):
    result = boat.throw_anchor(confirm=True)
    assert result == "Якорь опущен, лодка зафиксирована"

def test_throw_anchor_when_not_broken_rope_without_confirm(boat):
    result = boat.throw_anchor()
    assert result == "Веревка порвана, якорь в лодке. Вы хотите выбросить якорь навсегда? Подтвердите, чтобы выбросить."

# Тесты для метода sit
def test_sit_with_valid_people_count(boat):
    result = boat.sit(2)
    assert result == "В лодке 2 человек"

def test_sit_with_invalid_people_count_low(boat):
    result = boat.sit(0)
    assert result == "В лодке может быть от 1 до 3 человек"

def test_sit_with_invalid_people_count_high(boat):
    result = boat.sit(4)
    assert result == "В лодке может быть от 1 до 3 человек"

# Тесты для метода check_stability
def test_check_stability_with_valid_occupancy(boat):
    boat.sit(2)
    result = boat.check_stability()
    assert result == "Лодка устойчива"

def test_check_stability_with_overload(boat):
    boat.sit(4)
    result = boat.check_stability()
    assert result == "Лодка перегружена!"

# Тесты для метода check_buoyancy
def test_check_buoyancy_when_not_in_water(boat):
    result = boat.check_buoyancy()
    assert result == "Лодка не в воде"

def test_check_buoyancy_when_in_water_and_empty(boat):
    boat.place_in_water()
    result = boat.check_buoyancy()
    assert result == "Лодка на плаву"

def test_check_buoyancy_when_in_water_and_overloaded(boat):
    boat.place_in_water()
    boat.sit(4)
    result = boat.check_buoyancy()
    assert result == "Лодка перегружена и может утонуть"

def test_check_buoyancy_when_in_water_and_stable(boat):
    boat.place_in_water()
    boat.sit(2)
    result = boat.check_buoyancy()
    assert result == "Лодка на плаву"

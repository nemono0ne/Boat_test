import pytest
from boat import Boat

@pytest.fixture
def boat():
    """Фикстура для создания лодки без якоря"""
    return Boat()

@pytest.fixture
def anchored_boat():
    """Фикстура для создания лодки с опущенным якорем"""
    boat = Boat()
    boat.drop_anchor()
    return boat

@pytest.fixture
def broken_rope_boat():
    """Фикстура для создания лодки с порванной веревкой якоря"""
    boat = Boat()
    boat.apply_rope_tension(6)
    return boat

def test_row_free(boat):
    """Проверка гребли вперед, когда якорь не опущен"""
    result = boat.row("вперед")
    assert result == "Лодка движется вперед"

def test_row_free(boat):
    """Проверка гребли назад, когда якорь не опущен"""
    result = boat.row("назад")
    assert result == "Лодка движется назад"

def test_row_anchored(anchored_boat):
    """Проверка гребли при опущенном якоре"""
    result = anchored_boat.row("вперед")
    assert result == "Невозможно грести: якорь опущен"

def test_turn_left_anchored(anchored_boat):
    """Проверка поворота влево при опущенном якоре"""
    result = anchored_boat.row("влево")
    assert result == "Невозможно грести: якорь опущен"

def test_turn_right_anchored(anchored_boat):
    """Проверка поворота вправо при опущенном якоре"""
    result = anchored_boat.row("вправо")
    assert result == "Невозможно грести: якорь опущен"

def test_drop_anchor_success(boat):
    """Проверка успешного опускания якоря"""
    result = boat.drop_anchor()
    assert result == "Якорь опущен, лодка зафиксирована"

def test_drop_anchor_already_dropped(anchored_boat):
    """Проверка попытки повторного опускания якоря"""
    result = anchored_boat.drop_anchor()
    assert result == "Якорь уже опущен"

def test_lift_anchor(anchored_boat):
    """Проверка успешного поднятия якоря после того, как он был опущен"""
    anchored_boat.drop_anchor()
    result = anchored_boat.lift_anchor()
    assert result == "Якорь поднят, лодка может двигаться"

def test_row_with_broken_rope(broken_rope_boat):
    """Проверка гребли при порванной веревке якоря"""
    result = broken_rope_boat.row("вперед")
    assert result == "Лодка движется вперед"

def test_lift_anchor_after_throw(broken_rope_boat):
    """Проверка подъема якоря после того, как он был выброшен"""
    broken_rope_boat.throw_anchor(confirm=True)
    result = broken_rope_boat.lift_anchor()
    assert result == "Невозможно поднять якорь: веревка порвана"

def test_throw_no_confirm(broken_rope_boat):
    """Проверка выброса якоря без подтверждения при порванной веревке"""
    result = broken_rope_boat.throw_anchor(confirm=False)
    assert result == "Веревка порвана, якорь в лодке. Вы хотите выбросить якорь навсегда? Подтвердите, чтобы выбросить."

def test_throw_confirm(broken_rope_boat):
    """Проверка выброса якоря с подтверждением при порванной веревке"""
    result = broken_rope_boat.throw_anchor(confirm=True)
    assert result == "Веревка порвана, якорь выброшен, лодка больше не закреплена."

def test_move_after_throw(broken_rope_boat):
    """Проверка движения лодки после выброса якоря"""
    broken_rope_boat.throw_anchor(confirm=True)
    result = broken_rope_boat.row("вперед")
    assert result == "Лодка движется вперед"

def test_turn_left_after(broken_rope_boat):
    """Проверка поворота влево после выброса якоря"""
    broken_rope_boat.throw_anchor(confirm=True)
    result = broken_rope_boat.row("влево")
    assert result == "Лодка поворачивает влево"

def test_turn_right_after(broken_rope_boat):
    """Проверка поворота вправо после выброса якоря"""
    broken_rope_boat.throw_anchor(confirm=True)
    result = broken_rope_boat.row("вправо")
    assert result == "Лодка поворачивает вправо"

def test_drop_anchor_after_throw(broken_rope_boat):
    """Проверка, что невозможно отпустить якорь, если он выброшен"""
    broken_rope_boat.throw_anchor(confirm=True)
    result = broken_rope_boat.drop_anchor()
    assert result == "Невозможно опустить якорь: веревка порвана"

def test_sit_in_boat(boat):
    """Проверка рассадки людей в лодке"""
    result = boat.sit(2)
    assert result == "В лодке 2 человек"

def test_sit_in_boat_invalid(boat):
    """Проверка рассадки людей в лодке, когда число людей неверное"""
    result = boat.sit(5)
    assert result == "В лодке может быть от 1 до 3 человек"

def test_check_stability(boat):
    """Проверка устойчивости лодки"""
    boat.sit(3)
    result = boat.check_stability()
    assert result == "Лодка устойчива"

def test_check_buoyancy(boat):
    """Проверка плавучести лодки"""
    boat.place_in_water()
    boat.sit(3)
    result = boat.check_buoyancy()
    assert result == "Лодка на плаву"

def test_buoyancy_dry(boat):
    """Проверка плавучести лодки, когда она не в воде"""
    result = boat.check_buoyancy()
    assert result == "Лодка не в воде"

def test_place_in_water(boat):
    """Проверка помещения лодки в воду"""
    result = boat.place_in_water()
    assert result == "Лодка помещена в воду"

def test_remove_from_water(boat):
    """Проверка удаления лодки из воды"""
    boat.place_in_water()
    result = boat.remove_from_water()
    assert result == "Лодка убрана из воды"

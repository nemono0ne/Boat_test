
# Тестовое задание на позицию QA Automation

## Решение

В рамках данного задания были выполнены следующие шаги:

### 1. Создание тест-кейсов

Разработаны тест-кейсы на трёх уровнях:
- **Системные**: Проверка плавучести, вместимости и устойчивости лодки.
- **Интеграционные**: Взаимодействие лодки с якорем, веревкой и вёслами.
- **Функциональные**: Проверка работы функций гребли, управления якорем и проверки состояния веревки.

Тест-кейсы представлены в документе: `Тест_кейсы.docx`.

### 2. Реализация модели лодки

Реализована модель лодки на Python 3.10, включающая следующие компоненты:
- `Boat` — класс лодки с методами:
  - `row(direction)` — гребля в заданном направлении.
  - `drop_anchor()` — опускание якоря.
  - `lift_anchor()` — подъем якоря.
  - `check_buoyancy()` — проверка плавучести лодки.
  - `check_stability()` — проверка устойчивости лодки.
  - `place_in_water()` — помещение лодки в воду.
  - `remove_from_water()` — удаление лодки из воды.
- `Oar` — класс вёсел, позволяющий управлять направлением движения.
- `Anchor` — класс якоря, включающий логику работы с веревкой:
  - `apply_rope_tension(tension)` — проверка натяжения веревки с возможностью её обрыва.
  - `check_rope()` — проверка состояния веревки.
  - `throw_anchor(confirm)` — выброс якоря, если веревка порвана.

### 3. Автоматизированные тесты

- Автотесты написаны с использованием фреймворка `pytest`.
- Покрыл все автоматизированными тест-кейсами. Некоторые тест-кейсы можно использовать для ручного тестирования.
- Тесты покрывают функциональные, интеграционные и системные сценарии.

### Запуск тестов

1. Убедитесь, что у вас установлен `pytest`:
   ```sh
   pip install pytest
   ```

2. Перейдите в корневой каталог проекта и выполните команду:
   ```sh
   pytest
   ```
   Эта команда автоматически найдёт и выполнит все тесты из файлов, имя которых соответствует шаблону:
   - `test_*.py`
   - `*_test.py`
   
   расположенных в каталоге проекта и его подкаталогах.

3. Если тесты находятся в специальной директории (например, `test`), выполните команду:
   ```sh
   pytest test/
   ```

4. Чтобы получить более подробную информацию о результатах тестов, используйте флаг `-v` (verbose):
   ```sh
   pytest -v
   ```

### Скриншот результатов тестов
![test_boat_result](https://github.com/user-attachments/assets/be4d7e46-0413-473f-acda-f97fa5db8cac)

Проект выполнен с использованием системы контроля версий Git.



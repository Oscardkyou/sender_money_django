# Проект Django для отправки денег

[![Django](https://img.shields.io/badge/Django-3.2-092E20.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.9-3776AB.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Этот проект на Django представляет собой систему для отправки денег с использованием веб-интерфейса.

## Описание

Проект включает две основные модели: UserProfile и Transaction. Модель UserProfile содержит информацию о пользователях системы, включая их персональные данные и баланс счета. Модель Transaction используется для записи и отслеживания денежных операций между пользователями.

Административный интерфейс для этих моделей был настроен для удобного управления данными.

## Особенности

- Регистрация и аутентификация пользователей.
- Возможность просмотра и редактирования профилей пользователей.
- Отправка денежных переводов между пользователями.
- Отображение истории транзакций.

## Запуск проекта

Чтобы запустить проект локально, следуйте инструкциям:

1. Клонируйте репозиторий на свой локальный компьютер.
2. Установите необходимые зависимости, выполнив команду: `pip install -r requirements.txt`.
3. Примените миграции с помощью команды: `python manage.py migrate`.
4. Запустите сервер разработки: `python manage.py runserver`.
5. Откройте веб-браузер и перейдите по адресу `http://localhost:8000` для доступа к приложению.

## Вклад

Вы можете внести свой вклад в проект, создавая запросы на извлечение (pull requests) с предложенными изменениями. Убедитесь, что тщательно описываете ваши изменения и следуете соглашениям о стиле кодирования.

## Лицензия

Этот проект лицензирован под MIT License. Подробности см. в файле [LICENSE](LICENSE).

---

Обратите внимание, что вам может потребоваться обновить пути, инструкции и другие детали, чтобы они соответствовали вашему конкретному проекту.

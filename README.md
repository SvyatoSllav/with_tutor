## With tutor
#### Сайт проект для вуза для обучения английскому языку. Через админ панель можно загружать темы-подтемы-материалы. На сайте есть возможность связи через телеграмм бота https://github.com/evencatt/with_tutor_bot.

### **Стек**
![python version](https://img.shields.io/badge/Python-3.7-green)
![django version](https://img.shields.io/badge/Django-4.0.3-green)
![pillow version](https://img.shields.io/badge/Pillow-8.3-green)
![pytest version](https://img.shields.io/badge/pytest-6.2-green)
![requests version](https://img.shields.io/badge/requests-2.26-green)
![sorl-thumbnail version](https://img.shields.io/badge/thumbnail-12.7-green)

# Планы:
 * Адаптивная вёрстка.
 * Возможность добавлять HTML теги напрямую в текст записей.

# Запуск:
  * Установка зависимостей:
    * `pip install -r requirements.txt`
  * Применение миграций:
    * `python manage.py makemigrations`
    * `python manage.py migrate`
  * Создание администратора:
    * `python manage.py createsuperuser`
  * Запуск приложения:
    * `python manage.py runserver`

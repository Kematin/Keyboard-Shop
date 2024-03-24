# Keyboards Shop

Типы пользователей на сайте:
- Гость (покупатель)

frontend:
figma + html;css + react + vite

backend:
- django rest framework
- admin panel
- redis
- elastic
- postgres
- flake8; github actions
- pytest; coverage
- poetry
- docker; nginx

**Этапы разработки**:
- [ ] BACKEND
    - [X] Создание схематических моделей базы данных
    - [X] Растановка окружения API
    - [ ] Настройка drf
        - [x] Подключение middleware
        - [x] Подключение cors
        - [x] Подключение логирования
        - [x] Подключение админки
        - [x] Подключение инструментов тестирования 
    - [ ] Подключение БД
        - [ ] Подключение postgres
        - [ ] Подключение redis
        - [ ] Подключение elastic
    - [ ] Добавление моделей в API
    - [ ] Написанание routers заглушек
        - [ ] Keyboards
        - [ ] Tools
        - [ ] Accessories
        - [ ] Brands
    - [ ] Написание сериализаторов под моделей
    - [ ] Подключение ci/cd с github action + flake8
    - [ ] Написание логики
        - [ ] Keyboards
        - [ ] Tools
        - [ ] Accessories
        - [ ] Brands
        - [ ] Логика по покупке товара
    - [ ] Конечное тестирование + coverage
- [ ] FRONTEND
    - [ ] Верстка страницы на figma
    - [ ] Перенос страницы в react
    - [ ] Состыковка с бэкендом
- [ ] DEPLOY
    - [ ] Создание docker образов для backend и frontend
    - [ ] Настройка nginx на сервере
    - [ ] Деплой

## pages
- main page
- keyboards
    - custom
    - brands
        - varmilo
        - ...
    - wireless
    - MAC
    - low profile
    - size
        - 90-100%
        - ...
- accessories
    - mat
    - cable
    - brands
        - geekboards
        - ...
- tools
    - tools
    - switches
    - stabilizers
    - plates
    - PCB
    - body
    - noise insulation
    - consumables
- brands
    - varmilo
    - geekboards
    - ...
- about
- search
- error page
- order page

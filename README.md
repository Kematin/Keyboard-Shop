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
- poetry; loguru
- docker; nginx

Этапы разработки:
- [ ] BACKEND
    - [X] Создание схематических моделей базы данных
    - [ ] Растановка окружения API
    - [ ] Настройка drf
        - [ ] Подключение middleware
        - [ ] Подключение cors
        - [ ] Подключение логирования
        - [ ] Подключение админки
        - [ ] Подключение ci/cd с github action + flake8
        - [ ] Подключение pytest + coverage
    - [ ] Подключение БД
        - [ ] Подключение postgres
        - [ ] Подключение redis
        - [ ] Подключение elastic
    - [ ] Добавление моделей в API
    - [ ] Создание routers 
- [ ] FRONTEND
    - [ ] Верстка страницы на figma
    - [ ] Перенос страницы в react
    - [ ] Состыковка с бэкендом
- [ ] DEPLOY
    - [ ] Создание docker образов для backend и frontend
    - [ ] Настройка nginx на сервере
    - [ ] Деплой

pages
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

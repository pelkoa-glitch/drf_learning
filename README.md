# drf_learning


![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-4.2.6%2B-brightgreen)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16%2B-orange)

Учебный проект, разрабатывается с целью изучения бэкенда веб-приложений с использованием Python и Django Rest Framework. Приложение предоставляет RESTful API для управления информацией о гитарах и категориях. Оно также включает в себя аутентификацию с использованием JWT токенов для обеспечения безопасности API.

## Особенности

- Создание, чтение, обновление и удаление записей о гитарах и категориях с помощью API.
- Использование PostgreSQL в качестве базы данных для хранения информации о гитарах и категориях.
- Поддержка Docker для удобного развертывания приложения на удаленных серверах.

## Технологии

- Python 3.10
- Django Rest Framework 4.2.6
- PostgreSQL 16
- Docker

## Установка и Запуск

Для установки и запуска приложения, выполните следующие шаги:

1. Склонируйте репозиторий на ваш локальный компьютер.

2. Установите Docker, если он еще не установлен.

3. В корневом каталоге проекта выполните следующие команды:

   ```bash
   docker-compose build
   docker-compose up
   ```

4. Приложение будет доступно по адресу `http://localhost:8000/`.

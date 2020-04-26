# Установка:
На вашем локальном компьютере клонируйте это репозиторий
 - git clone https://github.com/haferf1ocken/DjangoProject.git
# Запуск:
Чтобы запустить проект перейдите в директорию, в которой он содержится и запустите командой docker-compose up
 - cd DjangoProject
 + docker-compose up
 # Работа с сервисом:
 + После запуска проекта открываем страницу с адресом [localhost:8000](http://localhost:8000) или [127.0.0.1:8000](http://127.0.0.1:8000)
 - При загрузке странице отправляется GET запрос и выводится список клиентов, если в БД проекта есть данные
 + На главной странице клинкнув по кнопке «Обзор» выбираем файл
 - Кнопка «Загрузить» отправляет POST запрос с выбранным файлом
 + По ссылке http://localhost:8000/api/v1/testapp/deals/ доступен список всех сделок в формате json
 - По ссылке http://localhost:8000/api/v1/testapp/deal/create доступна форма для создания объекта модели Deal(модель сделки)
 + По ссылке http://localhost:8000/api/v1/testapp/deal/detail/<int:pk> доступна информация о конкретной сделке в формате json
 

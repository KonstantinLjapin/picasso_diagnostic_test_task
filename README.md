# picasso_diagnostic_test_task
# **Basic Features**
1. Проект и приложение на Django Rest Framework >= 3.12 (Django > =3.2).
2. Модель File, которая будет представлять загруженные файлы.
3. эндпоинт upload/ POST-запросы для загрузки файлов. При загрузке файла создаёт объект модели File,
   запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку 
   файла возвращает статус 201 и сериализованные данные файла.
4. эндпоинт files/ возвращает список всех файлов с их данными, включая статус обработки.
# **Quick Start**
### Linux(Debian), docker compose (version v2.21.0)
#### Клонируете ветку мастер проекта локально, по образцу .env.dist(введены переменные для примера) создаётся .env . 
#### Проект готов к запуску.

**Выполните эти команды для запуска** 
- $ sudo chmod +x test_start.sh
- $ ./test_start.sh
- автоматически применяются миграции создаётся супер юзер и запускается сервер Django.
###  Open endpoint in browser or Postman.
#### -http://localhost:8000/admin/ - стандартная "админка"
#### -http://localhost:8000/api/upload/ - принимает POST- запросы модели File, Celery задачу, включая статус ответа
#### -http://localhost:8000/api/files/ - возвращает список всех файлов с их данными, включая статус обработки.
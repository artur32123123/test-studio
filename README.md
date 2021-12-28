# Опросник


## Инструкция по запуску

- активировать venv
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

## API

### Авторизация

Данные супер пользователя:
- username: admin
- password: admin

Для авторизации нужно воспользоваться: POST `api/v1/login`.
Пример:

```curl
curl --location --request POST 'http://127.0.0.1:8000/api/v1/login' \
--header 'Authorization: Token b09e2263a9618e53e62c89a881012778b3bc3cf7' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=wSAU0ot9cp8AiooiUWbfE51KDegzg6PqObCInCMfX0OFoknM1rNQ9Q028zMBtr5L' \
--data-raw '{
    "username": "admin",
    "password":"admin"
}'
```
### Опрос

- Получить все опросы: GET `api/v1/questionnaires`
- Получить опрос по ID: GET `api/v1/questionnaires`
- Создание опрос: POST `api/v1/questionnaires`
- Редактировать опрос: PUT `api/v1/questionnaires`
- Удалить опрос : DELETE `api/v1/questionnaires`
- Получить активные опросы: GET `/api/v1/questionnaires/active`

Структура модели:
- name - название
- description - описание
- date_start - дата и время начала
- date_end - дата и время конца опроса

### Вопросы для ответа

- Получить все опросы: GET `api/v1/questionnaires`
- Получить опрос по ID: GET `api/v1/questionnaires`
- Создание опрос: POST `api/v1/questionnaires`
- Редактировать опрос: PUT `api/v1/questionnaires`
- Удалить опрос : DELETE `api/v1/questionnaires`

Структура модели:

- text - Орисание
- type - Тип 
- questionnaire - Варинты ответа

### Варианты выбора для вопроса

- Получить все опросы: GET `api/v1/questionnaires`
- Получить опрос по ID: GET `api/v1/questionnaires`
- Создание опрос: POST `api/v1/questionnaires`
- Редактировать опрос: PUT `api/v1/questionnaires`
- Удалить опрос : DELETE `api/v1/questionnaires`

Структура модели:

- questionnaire - Опросник
- user - Пользователь

### Прохождение тестирования

- Получить результаты по user_id: GET `api/v1/pass?user_id=...`
- Пройти тестирование: POST `api/v1/pass`
```json
{
  "questionnaire": 1,
  "answers":[
    {
        "answer": "Артур",
        "question": 1
    }
  ]
}
```

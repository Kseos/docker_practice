__В данном проекте два микросервиса: один для сохранения книг, второй для сохранения рецензий.__


Запуск Docker Compose

`docker-compose up --build`

#### Book service:
__Используется flask, BeautifulSoup, requests (для парсинга книг с openlibrary)__

Получение списка все книг

`curl http://localhost:5000/books`

Получение информации о книге 

`curl http://localhost:5000/books/title/The%20Silmarillion`


#### Review service:
__Используется flask__

Чтение всех рецензий 

`curl http://localhost:5001/reviews`

Добавление рецензии  

`curl -X POST http://localhost:5001/reviews/add -H "Content-Type: application/json" -d "{\"book_title\": \"The Silmarillion\", \"reviewer\": \"Alice\", \"comment\": \"Amazing book!\"}"`

Получение рецензии по книге  

`curl http://localhost:5001/reviews/The%20Silmarillion`


#### Проверка работы микросервисов

Для сервиса книг: http://localhost:5000/books

Для сервиса рецензий: http://localhost:5001/reviews

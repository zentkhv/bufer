from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return "GET Request Received!"

@app.route('/', methods=['POST'])
def handle_post():
    # Получаем данные о запросе
    method = request.method
    url = request.url
    headers = dict(request.headers)
    data = request.data

    # Выводим информацию о запросе
    print(f"Метод: {method}")
    print(f"URL: {url}")
    print("Заголовки:")
    for key, value in headers.items():
        print(f"  {key}: {value}")
    print(f"Тело запроса: {data}")

    return "POST Request Received!"

if __name__ == '__main__':
    app.run()

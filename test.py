import openai

import credentials

openai.api_key = credentials.token


def generate_answer(prompt):
    response = openai.Completion.create(
        engine="davinci",  # модель, которую мы используем для генерации ответов
        prompt=prompt,
        temperature=0.2,  # устанавливаем температуру для контроля генерации текста
        max_tokens=60,  # устанавливаем максимальное количество генерируемых токенов
        n=1,  # количество ответов, которые мы хотим получить
        stop=None,
        # остановка генерации текста, если мы не хотим, чтобы текст заканчивался на какую-то определенную фразу
        timeout=15,  # устанавливаем тайм-аут на 15 секунд для получения ответа от модели
    )
    if response.choices[0].text.strip():  # проверяем, что ответ получен
        return response.choices[0].text.strip()
    else:
        return "К сожалению, я не смог найти ответ на ваш вопрос."


# входим в цикл диалога с пользователем
while True:
    prompt = input("Введите ваш вопрос: ")
    answer = generate_answer(prompt)
    print("Ответ: ", answer)

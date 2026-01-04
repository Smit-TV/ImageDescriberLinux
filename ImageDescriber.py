import pyscreenshot as ImageGrab
import base64
import json
import requests
import os
import configController
import ResponseDialog

SCREENSHOT_SAVE_DIR = "./fullscreen_schreenshot.png"

def describe():
    screenshot = ImageGrab.grab()
    screenshot.save(SCREENSHOT_SAVE_DIR)
    result = describe_image_with_groq(
        SCREENSHOT_SAVE_DIR,
        configController.get_api_key(),
        configController.get_selected_model(),
        configController.get_instructions()
    )
    ResponseDialog.ResponseDialog(result).create()



def describe_image_with_groq(
    image_path: str,
    api_key: str,
    model: str = "meta-llama/llama-4-scout-17b-16e-instruct",
    prompt: str = "Опиши это изображение подробно и ясно.",
    max_tokens: int = 1024,
) -> str:
    """
    Отправляет изображение в Groq API и возвращает его текстовое описание.

    :param image_path: Путь к изображению
    :param api_key: Groq API ключ
    :param model: Модель Groq
    :param prompt: Инструкция для описания
    :param max_tokens: Максимальное число токенов в ответе
    :return: Текстовое описание изображения
    """

    image_path = os.path.expanduser(image_path)

    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Файл не найден: {image_path}")

    # Читаем и кодируем изображение
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        },
                    },
                ],
            }
        ],
        "max_tokens": max_tokens,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise RuntimeError(
            f"Groq API error {response.status_code}: {response.text}"
        )

    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        raise RuntimeError(f"Некорректный ответ Groq API: {data}")
import requests

def send_telegram_message(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)
    return response

def fetch_data():
    # Здесь ваш код для получения данных через API
    return "Информация получена через API"

if __name__ == "__main__":
    bot_token = 'ВАШ_ТОКЕН_БОТА'
    chat_id = 'ВАШ_CHAT_ID'
    message = fetch_data()
    send_telegram_message(bot_token, chat_id, message)

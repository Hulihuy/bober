"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import requests
from aiogram import Bot, Dispatcher, executor, types

OPENWEATHER_API_KEY = "c28b8f13af900c5c45364126a91d34ae"

API_TOKEN = '7522501900:AAGgD8U6A0YXdpRlnvxJJ9ZVU3EvYZUOB38'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_weather_samara():
    city = "Самара"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru";
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_desc = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        city_name = data['name']
        country = data['sys']['country']
        return (
f"🌤 Погода в {city_name}, {country}:\n"
f"Температура: {temp}°C (ощущается как {feels_like}°C)\n"
f"Описание: {weather_desc}\n"
f"Влажность: {humidity}%\n"
f"Скорость ветра: {wind_speed} м/с"
)
    else:
        return '❌ Не удалось получить данные о погоде.'


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\nЯ - бот погоды в Самаре!\nПриятного пользования!")

@dp.message_handler(commands=['weather'])
async def send_weather(message: types.Message):
    weather_info = get_weather_samara()
    await message.reply(weather_info)



@dp.message_handler()
async def echo(message: types.Message):


    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
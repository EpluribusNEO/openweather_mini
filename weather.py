import dotenv
from os import environ
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

def wind_deg_to_direction(deg: float) -> str:
	# winddirections = ("северный", "северо-восточный", "восточный", "юго-восточный", "южный", "юго-западный", "западный", "северо-западный")
	winddirections = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
	_winddirections = ('N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW')
	direction = int((deg + 22.5) // 45 % 8)
	_direction = int((deg + 22.5)// 22.5 % 16)
	return _winddirections[_direction]


def get_weather_from_dict_to_str_ru(w_dict) -> str:
	ans = f"Город: {w_dict['location']['name']}, {w_dict['location']['country']}\n" \
	      f"Погода: {w_dict['weather']['detailed_status']}\n" \
	      f"Температура: {round((float(w_dict['weather']['temperature']['temp'])-273.15),2)} °C\n" \
	      f"Ощущается как: {round((float(w_dict['weather']['temperature']['feels_like'])-273.15), 2)} °C\n" \
	      f"Влажность: {w_dict['weather']['humidity']}%\n" \
	      f"Ветер: {w_dict['weather']['wind']['speed']} m/s {wind_deg_to_direction(float(w_dict['weather']['wind']['deg']))}\n" \
	      f"Давление: {round((w_dict['weather']['pressure']['press']) * 7.50062*pow(10, -1),2)} мм рт.ст.\n" \
	      f"Уровень облачности: {w_dict['weather']['clouds']}%\n" \
	      f"Видимость: {w_dict['weather']['visibility_distance']} м"
	return ans

def get_weather_from_dict_to_str_en(w_dict) -> str:
	ans = f"City: {w_dict['location']['name']}, {w_dict['location']['country']}\n" \
	      f"Weather: {w_dict['weather']['detailed_status']}\n" \
	      f"Temperature: {round((float(w_dict['weather']['temperature']['temp'])-273.15),2)} °C\n" \
	      f"Feels like: {round((float(w_dict['weather']['temperature']['feels_like'])-273.15), 2)} °C\n" \
	      f"Humidity: {w_dict['weather']['humidity']}%\n" \
	      f"Wind: {w_dict['weather']['wind']['speed']} m/s {wind_deg_to_direction(float(w_dict['weather']['wind']['deg']))}\n" \
	      f"Pressure: {round((w_dict['weather']['pressure']['press']) * 7.50062*pow(10, -1),2)} mm \n" \
	      f"Clouds: {w_dict['weather']['clouds']}%\n" \
	      f"Visibility distance: {w_dict['weather']['visibility_distance']} m"
	return ans

def get_weather_by_cityname(city: str) -> str:
	observation = mgr.weather_at_place(city)
	# w = observation.weather
	return get_weather_from_dict_to_str_ru(observation.to_dict())


config_dict = get_default_config()
config_dict['language'] = 'ru'

dotenv.load_dotenv('.env') # Загрузка переменных окружения из файлу
KEY = environ['owm_api_key'] # взять переменную, API-OpenWeathergit
owm = OWM(KEY, config_dict)
mgr = owm.weather_manager()


city = input("Введите название города:>")

try:
	answer = get_weather_by_cityname(city)
except:
	answer = "!_[ОШИБКА] Возможно некоректно указано название города!"
finally:
	print(answer)



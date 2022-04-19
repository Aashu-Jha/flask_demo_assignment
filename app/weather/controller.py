from msilib.schema import Error
import requests

def get_current_weather():

    url = 'https://api.openweathermap.org/data/2.5/weather?lat=28.619738&lon=77.011955&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    r = requests.get(url).json()

    weather = {
        'temperature': r['main']['temp'],
        'description' : r['weather'][0]['description']
    }

    return weather,200
    



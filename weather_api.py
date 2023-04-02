import requests
import time
import datetime
import json
import credentials


current_time = datetime.datetime.now()


def weather_request():
  
  print('Hello! Please select your location via longitude and latitude and the desired time for your report.')
  target_hour = input('Time: Please input the hour (1-24): ')
  target_minute = input('Time: Please input the minute (1-60): ')
  lat = input('Please enter your latitude: ')
  lon = input('Please enter your longitude: ')

  while True:
    current_time = datetime.datetime.now()
    if current_time.hour == target_hour and current_time.minute == target_minute:
      url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={credentials.api_key}'
      response = requests.get(url)
      if response.status_code == 200:
        data = response.json()
        
        #save required data from json
        clouds = data['weather'][0]['main']
        clouds_descr = data['weather'][0]['description']
        temp = round(data['main']['temp'] - 273.15)
        temp_feel = round(data['main']['feels_like'] - 273.15)
        temp_min = round(data['main']['temp_min'] - 273.15)
        temp_max = round(data['main']['temp_max'] - 273.15)
        humidity = data['main']['humidity']
        location = data['name']

        # print the weather data depending on the situation
        print(f"Hello, here's the weather for {location}.")
        if clouds == 'Clouds':
          print("Today it is cloudy.")
        print(f"The average temperature today is {temp}°C.") 
        if  temp != temp_feel:
          print(f"It feels like {temp_feel}°C.")
        print(f"The maximum temperature for today is {temp_max}, minimum is {temp_min} °C.")

      #in case site is not available print error message
      else:
        print("Couldn't to connect to page.")

    time.sleep(55)
 
weather_request()
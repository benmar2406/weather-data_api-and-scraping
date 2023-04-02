import requests
import time
import datetime
import json
import smtplib
import credentials

#location
lat = 50.104890
lon = 8.61349670

#define time for daily request
target_hour = 10
target_minute = 50
#get current time
current_time = datetime.datetime.now()

name = "user"

def weather_request():

  while True:
    current_time = datetime.datetime.now()
    if current_time.hour == target_hour and current_time.minute == target_minute:
      url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={credentials.api_key}'
      response = requests.get(url)
      if response.status_code == 200:
        data = response.json()
        
        #save required data from json, change the temperature values from Kelvin to °C
        clouds = data['weather'][0]['main']
        clouds_descr = data['weather'][0]['description']
        temp = round(data['main']['temp'] - 273.15)
        temp_feel = round(data['main']['feels_like'] - 273.15)
        temp_min = round(data['main']['temp_min'] - 273.15)
        temp_max = round(data['main']['temp_max'] - 273.15)
        humidity = data['main']['humidity']
        location = data['name']

        #send email with the weather data
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(credentials.sender, credentials.password)
        from_address = credentials.sender
        to_address = credentials.receiver
        subject = f"Weather report for today."
        message = f"Hello {name},\nhere is your daily weather report for {location}.\nTemperature: {temp}C.\nFelt temperature: {temp_feel}C\nMax. temperature: {temp_max}C\nMin. temperature: {temp_min}C\nMax. temperature: {temp_max}C\nHumidity: {humidity}{chr(37)}"
        email_text = f'From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{message}'
        server.sendmail(from_address, to_address, email_text)
        server.quit()



      #in case site is not available print error message
      else:
        print("Couldn't to connect to page.")

    time.sleep(55)
 
weather_request()
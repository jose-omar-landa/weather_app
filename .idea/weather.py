import time
import tkinter as tk
from tkinter import messagebox
import requests

messagebox.showinfo("Weather App", "Please type your city name in the text box, then press 'ENTER' on your keyboard!")


# Function to convert temp from kelvin to fahrenheit:
def f_temp(k_temp):
    celcius = int(k_temp) - int(273.15)
    fahrenheit = celcius * (9 / 5) + 32
    return round(fahrenheit)


# Function to pull weather data using OpenWeather API:
def pull_weather_info(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9db00a166be88aa415f63706801886a9"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = f_temp(int(json_data["main"]["temp"]))
    min_temp = f_temp(int(json_data["main"]["temp_min"]))
    max_temp = f_temp(int(json_data["main"]["temp_max"]))
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = round(json_data["wind"]["speed"] * 2.237)
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data["sys"]["sunrise"] - 21600))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data["sys"]["sunset"] - 21600))

    final_info = condition + "\n" + str(temp) + "° F"
    final_data = "\n" + "High Temp: " + str(max_temp) + "\n" + "Low Temp: " + str(min_temp) + "\n" + "Pressure: " \
                 + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + " MPH" \
                 + "\n" + "Sunrise: " + sunrise + " AM" + "\n" + "Sunset: " + sunset + " PM"
    label1.config(text=final_info)
    label2.config(text=final_data)


# Tkinter Data:
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>", pull_weather_info)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()

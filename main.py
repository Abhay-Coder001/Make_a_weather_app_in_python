import tkinter as tk
import requests
import time

#create a def function

def getWeather(canvas):
    city = textField.get() #take city name from the textfield

    #copy the api from openwheathermap.org
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

    #now we call jason data using requests
    json_data = requests.get(api).json()
    #now these are all types of data which we see in output display of wheather app
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    #now define strings to carry all our data
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("900x600") #geometry of canvas
canvas.title("Weather App") #give the name to the canvas
#for giving the fonts
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

#define a textfield here to get the city name form the user
textField = tk.Entry(canvas, justify='left', width=20, font=t)
textField.pack(pady=20) #pack these entries
textField.focus() #for remain focus so user can enter city name directly without moving the cursor
textField.bind('<Return>', getWeather)
#Creating labels to show the data
label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()
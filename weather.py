import requests
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import io

# API details
API_KEY = "643af57dc24221ad9429565f97368481"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Function to get weather data
def get_weather_data(city_name, unit='metric'):
    try:
        complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units={unit}"
        response = requests.get(complete_url)
        data = response.json()
        if data['cod'] != '404':
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'weather': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
            }
            return weather_data
        else:
            messagebox.showerror("Error", "City not found!")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Unable to get weather data: {e}")
        return None

# Function to display weather data in the GUI
def display_weather():
    city_name = city_entry.get()
    unit = 'metric' if var.get() == 1 else 'imperial'
    weather_data = get_weather_data(city_name, unit)
    
    if weather_data:
        city_label.config(text=weather_data['city'])
        temp_label.config(text=f"Temperature: {weather_data['temperature']}°")
        weather_label.config(text=f"Weather: {weather_data['weather']}")
        wind_label.config(text=f"Wind Speed: {weather_data['wind_speed']} m/s")
 
# Function to center the window on the screen
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Initialize the GUI
root = tk.Tk()
root.title("Weather App")
center_window(root, 430, 420)  # Set window size and center it

# Set a background color for better appearance
root.configure(bg='#d9e3f0')

# Frame for content
frame = tk.Frame(root, bg='#f0f4f7', padx=20, pady=20)
frame.pack(pady=20)

# User input field for city name
city_label = tk.Label(frame, text="Enter City Name:", font=("Arial", 12), bg='#f0f4f7')
city_label.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
city_entry = tk.Entry(frame, width=20, font=("Arial", 12))
city_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

# Labels to display weather information
city_label = tk.Label(frame, text="", font=("Arial", 20, 'bold'), bg='#f0f4f7')
city_label.grid(row=1, column=0, columnspan=2, pady=10, sticky='nsew')

temp_label = tk.Label(frame, text="", font=("Arial", 14), bg='#f0f4f7')
temp_label.grid(row=2, column=0, columnspan=2, pady=10, sticky='nsew')

weather_label = tk.Label(frame, text="", font=("Arial", 14), bg='#f0f4f7')
weather_label.grid(row=3, column=0, columnspan=2, pady=10, sticky='nsew')

wind_label = tk.Label(frame, text="", font=("Arial", 14), bg='#f0f4f7')
wind_label.grid(row=4, column=0, columnspan=2, pady=10, sticky='nsew')

# Unit selection for Celsius/Fahrenheit
var = tk.IntVar()
var.set(1)  # Default is Celsius
celsius_radio = tk.Radiobutton(frame, text="Celsius", variable=var, value=1, font=("Arial", 12), bg='#f0f4f7')
fahrenheit_radio = tk.Radiobutton(frame, text="Fahrenheit", variable=var, value=2, font=("Arial", 12), bg='#f0f4f7')
celsius_radio.grid(row=5, column=0, pady=10, sticky='ew')
fahrenheit_radio.grid(row=5, column=1, pady=10, sticky='ew')

# Button to fetch weather
fetch_button = tk.Button(frame, text="Get Weather", command=display_weather, font=("Arial", 12), bg='#87CEEB', fg='white')
fetch_button.grid(row=6, column=0, columnspan=2, pady=20, sticky='nsew')

root.mainloop()

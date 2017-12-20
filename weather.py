import pyowm

owm = pyowm.OWM('d6c1adeac7d7008ab74147f5a68f20be')  
observation = owm.weather_at_place("waco, us")  
w = observation.get_weather()  
wind = w.get_wind()  
temperature = w.get_temperature('fahrenheit')
tomorrow = pyowm.timeutils.tomorrow()  


print(w)  
print(wind) 
print(temperature)
print(tomorrow)

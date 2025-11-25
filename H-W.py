temp=int(input("Enter temperature in Celsius: "))

if temp>=22:
    print("It is appropriate to wear light clothes right now.")
else:
    print("It is better to wear warm clothes right now.")

humidity=int(input("Enter the humidity percentage: "))
if humidity>=60:
    print("It is advisable to carry an umbrella.")
else:
    print("No need to carry an umbrella.")

wind_speed=int(input("Enter the wind speed in km/h: "))
if wind_speed>=30:
    print("It is recommended to stay indoors due to high wind speed.")
else:
    print("It is safe to go outside.")
rainfall=int(input("Enter the rainfall in mm: "))
if rainfall>=20:
    print("Heavy rain expected, take necessary precautions.")
else:
    print("Light or no rain expected.")

if temp<=0 and humidity>=80:
    print("Extreme cold and high humidity detected, stay warm and dry.")
elif temp>=35 and humidity>=70:
    print("Extreme heat and high humidity detected, stay hydrated and cool.")
else:
    print("Weather conditions are normal.")
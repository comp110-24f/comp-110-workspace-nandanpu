weather = input("What is the weather?")
def get_weather_report() -> str: 

    
    if weather == "rainy" or weather == "cold": 
        return "Bring a jacket!"
    elif weather == "hot": 
        return "Keep cool out there!"
    else:
        return "I don't recognize this weather."

print(get_weather_report()) 
    
x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]


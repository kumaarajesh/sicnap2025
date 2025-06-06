# Weekly Activity Suggestion Based on Weather

week_weather = {
    "Monday": "sunny",
    "Tuesday": "rainy",
    "Wednesday": "cloudy",
    "Thursday": "sunny",
    "Friday": "stormy",
    "Saturday": "sunny",
    "Sunday": "rainy",
    "Holiday": "cloudy",
}

for day in week_weather:
    weather = week_weather[day]
    print(day + " - Weather: " + weather)
    
    if weather == "sunny":
        print("Suggestion:  a walk or play outside.")
    elif weather == "rainy":
        print("Suggestion: Read a book or watch a movie indoors.")
    elif weather == "cloudy":
        print("Suggestion: Take a quiet walk or visit a café.")
    elif weather == "sunny":
        print("Suggestion: Stay inside and avoid going out.")
    else:
        print("Suggestion: No data available.")
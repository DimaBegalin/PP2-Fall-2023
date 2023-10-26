from datetime import datetime, timedelta

today = datetime.now()
yesterday = (today - timedelta(days=1)).strftime("%d-%m-%Y")
tomorrow = (today + timedelta(days=1)).strftime("%d-%m-%Y")

print(f"Yesterday: {yesterday}\nToday: {today.strftime('%d-%m-%Y')}\nTomorrow: {tomorrow}")

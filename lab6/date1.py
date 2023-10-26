from datetime import datetime, timedelta

c_date = datetime.now()
f_date = c_date - timedelta(days=5)

print(f_date.strftime("%Y-%m-%d"))
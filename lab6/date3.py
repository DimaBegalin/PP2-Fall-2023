from datetime import datetime

c_date = datetime.now()
c_date = c_date.replace(microsecond=0)

print(c_date.strftime("%Y-%m-%d %H:%M:%S"))

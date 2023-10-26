from datetime import datetime

date1 = datetime(2023, 10, 20)
date2 = datetime(2023, 10, 25)

t_difference = (date2 - date1).total_seconds()

print(t_difference)

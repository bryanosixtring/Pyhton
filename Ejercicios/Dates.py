#Dates

from datetime import datetime
from datetime import date
from datetime import time

fecha_hora_sistema = datetime.now()



def print_date(date): 
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)

print_date(fecha_hora_sistema)

year_2023 = datetime(2023,1,1)
print(year_2023)

current_time = time(21,6,0)
print(current_time)
print(current_time.hour)

current_data = date.today()
print(current_data)

#Operaciones con fecha

diff = year_2023 - fecha_hora_sistema
print(diff)

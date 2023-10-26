from auto.models import Auto, Make
from datetime import datetime
from time import sleep
from csv import reader


def run():
    fhand = open("auto/auto.csv")
    freader = reader(fhand)
    next(freader)

    for row in freader:
        now = datetime.now()

        m,c = Make.objects.get_or_create(name=row[0])
        
        if row[4] == '':
            rep78 = None
        else:
            rep78 = row[4]

        auto = Auto.objects.create(make=m, name=row[1], price=row[2], mpg=row[3], rep78=rep78, headroom=row[5], trunk=row[6], weight=row[7], length=row[8], turn=row[9], displacement=row[10], gear_ratio=row[11], foreign=row[12])

        print(f"{m}, {auto}")
        
import calendar


def getCalendar(yy: int, mm: int) -> str:
    days_of_month = calendar.month(yy, mm)
    print(days_of_month)


getCalendar(2022, 4)
getCalendar(1997, 7)

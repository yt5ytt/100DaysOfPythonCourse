import datetime


class DateTimeConversion:

    def __init__(self, raw_date):
        data = raw_date.split("T")
        time_off = data[1].split(".")
        self.today = datetime.date.today()
        self.timeOff = time_off[0]
        self.dateOff = self.convert_date(data[0])

    def convert_date(self, raw_date):
        data = raw_date.split("-")
        year = data[0]
        month = data[1]
        day = data[2]
        return f"{day}.{month}.{year}."

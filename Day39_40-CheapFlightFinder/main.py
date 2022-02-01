from classes.lowestPrices import LowestPrices
from classes.kiwiPartners import KiwiFlights
from classes.dateTimeConversion import DateTimeConversion
from classes.twilioSMS import TwilioSMS
from classes.kiwiLocations import KiwiLocations

cities = LowestPrices()
for city in cities.data:
    if city["iataCode"] == "":
        locations = KiwiLocations(city["city"])
        code = locations.code
        cities.import_codes(city["id"], code)

prices = LowestPrices()

for city in prices.data:
    flight = KiwiFlights(city["iataCode"])
    lowestFlight = False
    for data in flight.data:
        if city["lowestPrice"] >= data["price"] and not lowestFlight and data["availability"]["seats"] != "null":
            timeConvert = DateTimeConversion(data["local_departure"])
            message = f"There is unbelievable opportunity for you to fly to {data['cityTo']} for only " \
                      f"{data['price']} EUR on {timeConvert.dateOff} at {timeConvert.timeOff} local time. " \
                      f"You will sleep {data['nightsInDest']} nights there."
            sendSMS = TwilioSMS()
            sendSMS.sms(message)
            lowestFlight = True

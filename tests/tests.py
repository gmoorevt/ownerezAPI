import datetime
import os 
import dotenv

from ownerrezapi import Ownerrezapi




dotenv.load_dotenv()


username = os.getenv("USERNAME")
token = os.getenv("TOKEN")


# props = api.getproperties()
# for prop in props:
#     print(prop.id)
#     print(prop.name)
#     print(prop.thumbnail_url_large)


api = Ownerrezapi(username, token)

print(api.isunitbooked(357991))

# bookings = api.getbookings(property_id=357991, since_utc="2024-01-01")
# today = datetime.datetime.today()
# for booking in bookings:
#     arrival = datetime.datetime.strptime(booking.arrival, "%Y-%m-%d")
#     departure = datetime.datetime.strptime(booking.departure, "%Y-%m-%d")
    
#     if arrival <= today and departure >= today:
#         print("Unit is booked today")
#         print(booking.id)
#         print(booking.title)
#         continue

#booking = api.getbooking(booking_id=9732833)



#print(booking.guest.last_name)



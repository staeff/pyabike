#!/usr/bin/python
from pyabike import PyABike

cab = PyABike()

# Broken (with unpatched suds library?)
# product_info = cab.list_product_info()
# print product_info

# Initiate SMS with recovery password.
# cab.request_new_password('YOUR_PHONE_NUMBER')

# # List free bikes
# free_bikes = cab.list_free_bikes(
#     maxRes=100, 
#     radius=500, 
#     longitude=9.98963,
#     latitude=53.5602
# )
# print(free_bikes)

# list return stations
return_locations = cab.list_return_locations(
    maxRes=100, 
    radius=500,
    bike='3351',
    longitude=9.98963,
    latitude=53.5602
)
print(return_locations)

# get bike info
# print(cab.get_bike_info('3351'))

# redeem bonus code
# bonus_code_result = cab.redeem_bonus_code(
#     bonusCode = 'ABCDEF',
#     user = 'YOUR_USERNAME_OR_PHONENUMBER',
#     passwd = 'YOUR_PASSWD'
# )
# print(bonus_code_result)

# # List completed trips
# completed_trips = cab.list_completed_trips(
#     user = 'YOUR_USERNAME_OR_PHONENUMBER',
#     passwd = 'YOUR_PASSWD'
# )
# print(completed_trips)

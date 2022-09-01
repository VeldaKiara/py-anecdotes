import phonenumbers

#import geocoder, Geocoding allows you to take your customers' information and create a map of their locations.
from phonenumbers import geocoder

user_input = input("Enter the phone number: ")
phone_number = phonenumbers.parse(user_input)

print(geocoder.description_for_number(phone_number, 'en'))
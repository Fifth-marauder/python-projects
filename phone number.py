import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
while (True):
    code=input("enter country code")
    num=input("enter the phone number")
    print("+"+code+num)
    if len(num)<1 or len(code)<1:
        break
    ph_number=phonenumbers.parse("+"+code+num)
    print(carrier.name_for_number(ph_number,'en'))
    print(geocoder.description_for_number(ph_number,'en'))   

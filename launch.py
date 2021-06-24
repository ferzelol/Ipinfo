import requests
import sys
import os


ip = input("IP: ")

os.system("clear")
r = requests.get(f"http://ip-api.com/json/{ip}").json()
print(f"Cоuntry code: {r[str('countryCode')]}\nCountry: {r[str('country')]}\nCity: {r[str('city')]}\nTimezone: {r[str('timezone')]}\nISP: {r[str('isp')]}")

import sys
import requests
import json
import os

#Constant variables
DRAW_LINE = "-"*50

URL = "http://api.openweathermap.org/data/2.5/weather?q="

os.system('cls')

RESPONSE_OK = 200

def getCommandLineArguments(*args):
	api_key = args[0][1]
	city_name = args[0][2]
	buildWeatherUrl(api_key, city_name)

def buildWeatherUrl(api_key, city_name):
	global URL
	URL = URL + city_name +"&appid="+api_key
	callWeatherAPI(URL)
	
def callWeatherAPI(url):
	response_str = requests.get(url)
	if(response_str.status_code == RESPONSE_OK):
		json_str = json.loads(response_str.content)
		print("City Name: "+json_str['name'])
		print("Weather Condition: "+json_str['weather'][0]['description'])
	else:
		print("Oops, something is messed up")


print("""\
API Usage: Enter command in the following format:
get_weather_report.py <API key> <city name>

Note: This program will clear the screen using MS-DOS cls command
      before showing the results
""")

print(DRAW_LINE)
print("\n")

#Get the commnad line arguments into variable
commandLineArgs = sys.argv
getCommandLineArguments(commandLineArgs)

"""
It is expected that the command line arguments are in the format
get_weather_report.py <api key> <city_name>
"""

print("\n")
print(DRAW_LINE)

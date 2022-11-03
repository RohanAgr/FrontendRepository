import requests

url = "https://nfl-schedule.p.rapidapi.com/v1/schedules"

headers = {
	"X-RapidAPI-Key": "b558955759msh32134753facfdd1p133021jsncf26cd31822e",
	"X-RapidAPI-Host": "nfl-schedule.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

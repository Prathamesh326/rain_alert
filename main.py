import requests
import smtplib

my_email = "" # enter your own email
password = "" # enter your own generated password

api_key = "" #generate your own api key and paste it here
my_lat = 19.075983
my_long = 72.877655

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "cnt": 4,
    "appid": api_key,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response.status_code)
data = response.json()
print(data)

will_rain = False
for i in data['list']:
    weather_id = i['weather'][0]['id']
    if weather_id < 700:
        will_rain=True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg="Subject:Rain Alert\n\nIt's going to rain today. Remember to bring an umbrella."
                            )

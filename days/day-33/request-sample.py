import requests
from datetime import datetime
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# """
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# elif response.status_code == 404:
#     raise Exception("That resource does not exist.")
# """

response.raise_for_status()
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://api.open-notify.org/is-now.json
# 404
# 에러가 있으면 코드와 메세지 raise, 아니면 실행

# <Response [200]>
# 1XX : Hold on
# 2XX : request success
# 3XX : permission denied
# 4XX : target Not found
# 5XX : something about server went wrong

data = response.json()
print(data) #{'message': 'success', 'iss_position': {'latitude': '14.1240', 'longitude': '-157.2921'}, 'timestamp': 1773627782}

# 딕셔너리처럼 키 접근
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_position = (latitude, longitude)
print(iss_position)

# ============= request with parameters ================== #

parameters = {
    "lat" : 37.456257,
    "lng" : 126.705208,
    "formatted" : 0,
    "tzid" : "Asia/Hong_Kong"
}

another_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
another_response.raise_for_status()
sunrise = another_response.json()['results']['sunrise'] # 2026-03-16T05:41:44+08:00
sunset = another_response.json()['results']['sunset']

sunrise_time = sunrise.split("T")[1].split(":")[0]
sunset_time = sunset.split("T")[1].split(":")[0]
print(datetime.now()) # 2026-03-16 12:00:05.874668

print(sunrise_time)
print(sunset_time)
print(datetime.now().hour)


import requests

# NUTRITIONIX
APP_ID = ""
API_KEY = ""

GENDER = "male"
WEIGHT_KG = "68"
HEIGHT_CM = "176"
AGE = "39"

exercise_query = input("What exercise you did? ")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
nutritionix_request_body = {
 "query": exercise_query,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=nutritionix_request_body, headers=nutritionix_headers)
result = response.json()
print(result)

# # SHEETY
# post_endpoint = "https://api.sheety.co/45acc41c42404d01472bceb2dd5ac605/pythonMyWorkouts/workouts"
# sheety_headers = {
#     "Authorization": "XXX",
# }
# sheety_request_body = {
#     "workout": {
#         "date": "24/02/2022",
#         "time": "15:00:00",
#         "exercise": "Running",
#         "duration": 30,
#         "calories": 79.33,
#         "new": "something",  # REMOVE TODO 1
#     }
# }
# response = requests.post(url=post_endpoint, json=sheety_request_body, headers=sheety_headers)
# result = response.text
# print(result)

import requests


def weather():

    city= input("Please Enter Your Location : ")

    Api_Add= 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=9598da4e9a5c13241990c282e2c5ad48'.format(city)
    jData=requests.get(Api_Add).json()

    print(jData)


weather()


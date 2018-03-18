import pyowm


owm = pyowm.OWM('b4a90387458cb975bafe21c7c9ea0737')
fc = owm.three_hours_forecast('Lviv, ua')

time = pyowm.timeutils.next_three_hours()


while True:
    try:
        if int(str(time)[11:13]) > 8 and int(str(time)[11:13]) < 22:
            print(fc.get_weather_at(time).get_humidity(), time)
        time = pyowm.timeutils.next_three_hours(time)
    except:
        break

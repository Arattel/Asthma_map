import pyowm


owm = pyowm.OWM('b4a90387458cb975bafe21c7c9ea0737')
fc = owm.three_hours_forecast('Lviv, ua')

time = pyowm.timeutils.next_three_hours()
while True:
    try:
        print(fc.get_weather_at(time).get_humidity())
        time = pyowm.timeutils.next_three_hours(time)
    except:
        break

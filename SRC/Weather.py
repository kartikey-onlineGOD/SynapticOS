import python_weather
import asyncio
w = []

async def getweather():
    global w
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find("Bangalore")

    # returns the current day's forecast temperature (int)
    w.append(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        w.append(str(forecast.date)+" "+str(forecast.sky_text)+" "+str(forecast.temperature))

    # close the wrapper once done
    await client.close()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
    return w


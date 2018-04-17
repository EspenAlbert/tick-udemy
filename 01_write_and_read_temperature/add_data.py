import random
import requests
import time


def total_ms_now():
    return int(time.time() * 1000)


seconds_in_a_day = 3600 * 24


def get_payload(point_count, start_temperature=25.5, time_delta_ms=30000):
    start_ms = total_ms_now() - seconds_in_a_day * 1000
    temperature = start_temperature
    data_points = []
    for point_number in range(point_count):
        unix_time = start_ms + time_delta_ms * point_number
        delta_temp = random.random() #Number between 0-1
        if random.random() > 0.5: #Add or subtract delta temperature
            delta_temp *= -1
        temperature = temperature + delta_temp
        rounded_temperature = round(temperature, 1)
        payload_line = f"sensors,sensor_id=climax_1531,user_location=greenhouse is_fahrenheit=false,temperature={rounded_temperature} {unix_time}"
        data_points.append(payload_line)
    payload = "\n".join(data_points)
    return payload


if __name__ == '__main__':
    point_interval_in_seconds = 30
    points_in_a_day = int((seconds_in_a_day) / point_interval_in_seconds)  # 2880
    payload = get_payload(points_in_a_day)
    url = "http://localhost:8086/write"
    querystring = {"db": "tick_udemy", 'precision': 'ms'}
    response = requests.request("POST", url, data=payload, params=querystring)

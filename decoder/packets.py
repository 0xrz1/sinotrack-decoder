def decode_gps(data: bytes) -> dict:
    # SinoTrack GPS packet format (common)
    # [date(6)][gps info][lat(4)][lon(4)][speed][course(2)]

    year = 2000 + data[0]
    month = data[1]
    day = data[2]
    hour = data[3]
    minute = data[4]
    second = data[5]

    lat_raw = int.from_bytes(data[7:11], 'big')
    lon_raw = int.from_bytes(data[11:15], 'big')

    latitude = lat_raw / 30000 / 60
    longitude = lon_raw / 30000 / 60

    speed = data[15]
    course = int.from_bytes(data[16:18], 'big')

    return {
        "time": f"{year}-{month:02}-{day:02} {hour:02}:{minute:02}:{second:02}",
        "latitude": latitude,
        "longitude": longitude,
        "speed_kmh": speed,
        "course": course
    }

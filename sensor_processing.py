def calculate_average():

    values = [72, 55, 101, 90]
    average = sum(values) / len(values)
    print("Average value:", average)

calculate_average()

stations = [
    ['A1', 62],
    ['B5', 97],
    ['C3', 155]
]

for station in stations:
    print(f"{station[0]} → {station[1]}")

def report_status(stations, threshold):
    for station in stations:
        id, pm25 = station
        if pm25 < threshold:
            print(f"id {id} pm25 (safe)")
        else:
            print(f"id {id} pm25 (danger!)")
stations = [
    [1, 50],
    [2, 120],
    [3, 90],
    [4, 150],
]
report_status(stations, 100)


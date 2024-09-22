import random

def get_sensor_data():
    vehicles_on_road = random.randint(5, 50)
    avg_speed = random.uniform(20, 80) 
    return {
        "vehicle_count": vehicles_on_road,
        "average_speed": avg_speed
    }

if __name__ == "__main__":
    sensor_data = get_sensor_data()
    print(f"Sensor Data: {sensor_data}")

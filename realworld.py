import random
import time
import matplotlib.pyplot as plt

class TrafficSensor:
    def __init__(self, location):
        self.location = location

    def get_traffic_data(self):
        # Simulate traffic data: vehicles per minute
        return random.randint(50, 200)

class TrafficManagementSystem:
    def __init__(self):
        self.sensors = []
        self.data_history = {}

    def add_sensor(self, sensor):
        self.sensors.append(sensor)
        self.data_history[sensor.location] = []

    def collect_data(self):
        data = {}
        for sensor in self.sensors:
            traffic_data = sensor.get_traffic_data()
            data[sensor.location] = traffic_data
            self.data_history[sensor.location].append(traffic_data)
        return data

    def analyze_data(self, data):
        total_vehicles = sum(data.values())
        average_vehicles = total_vehicles / len(data)
        return total_vehicles, average_vehicles

    def check_alerts(self, data, threshold=150):
        alerts = []
        for location, count in data.items():
            if count > threshold:
                alerts.append(f"High traffic alert at {location}: {count} vehicles")
        return alerts

    def plot_data(self):
        plt.figure(figsize=(10, 5))
        for location, history in self.data_history.items():
            plt.plot(history, label=location)
        plt.xlabel('Time (minutes)')
        plt.ylabel('Vehicles per minute')
        plt.title('Traffic Data Over Time')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    tms = TrafficManagementSystem()
    tms.add_sensor(TrafficSensor("Location A"))
    tms.add_sensor(TrafficSensor("Location B"))
    tms.add_sensor(TrafficSensor("Location C"))

    for _ in range(10):  # Collect data for 10 minutes
        data = tms.collect_data()
        total, average = tms.analyze_data(data)
        alerts = tms.check_alerts(data)
        print(f"Total vehicles: {total}, Average vehicles per location: {average:.2f}")
        for alert in alerts:
            print(alert)
        time.sleep(60)  # Collect data every minute

    tms.plot_data()

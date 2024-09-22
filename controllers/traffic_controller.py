from models.traffic_rl_model import TrafficRLModel
from data.sensors_data import get_sensor_data

class TrafficController:
    def __init__(self):
        self.model = TrafficRLModel(state_size=5, action_size=3)

    def adjust_traffic_signals(self):
        sensor_data = get_sensor_data()
        state = sensor_data['vehicle_count'] // 10 
        action = self.model.choose_action(state)
        print(f"Adjusting traffic signals with action {action}")

if __name__ == "__main__":
    controller = TrafficController()
    controller.adjust_traffic_signals()

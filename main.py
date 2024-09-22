from controllers.traffic_controller import TrafficController

def main():
    controller = TrafficController()
    while True:
        controller.adjust_traffic_signals()

if __name__ == "__main__":
    main()

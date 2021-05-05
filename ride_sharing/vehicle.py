class Vehicle:
    VEHICLE_DB = {}
    def __init__(self, driver_name, vehicle_name, vehicle_number):
        self.driver_name = driver_name
        self.vehicle_name = vehicle_name
        self.vehicle_number = vehicle_number
        self.VEHICLE_DB[vehicle_number] = self


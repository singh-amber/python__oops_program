from user import User
from vehicle import Vehicle
from rides import Ride


class Query:
    def __init__(self):
        pass

    def add_user(self, name, gender, age):
        if name in User.User_DB:
            print("This user already exists")
        else:
            User(name, gender, age)
            print("User added")

    def add_vehicle(self, driver_name, vehicle_name, vehicle_number):
        if vehicle_number in Vehicle.VEHICLE_DB:
            print("Vehicle already present in database")
        else:
            Vehicle(driver_name, vehicle_name, vehicle_number)
            print("Vehicle added")

    def offer_ride(self, driver_name, origin, available_seats, vehicle_name, vehicle_number, destination):
        if (driver_name, vehicle_number) in Ride.RIDES_DB:
            print("This driver is already offering a ride with this vehicle")
        else:
            Ride(driver_name, origin, available_seats, vehicle_name, vehicle_number, destination)
            User.User_DB[driver_name].rides_offered += 1
            Ride.ENGAGED_AS_DRIVER[driver_name] += 1
            print("ride added")

    def select_ride(self, passenger_name, origin, destination, seats, strategy):
        if strategy == "Most Vacant":
            result = Ride.get_a_suitable_vacant_ride(passenger_name, origin, destination, seats)
            # if not result:
            #     print("Cannot select from available rides")
        else:
            result = Ride.get_a_suitable_vehicle(passenger_name, origin, destination, seats, strategy)
            # if not result:
            #     print("Cannot select from available rides")

    def end_ride(self, driver_name, origin, available_seats, vehicle_name, vehicle_number, destination):
        if (driver_name, vehicle_number) in Ride.RIDES_DB:
            Ride.ENGAGED_AS_DRIVER[driver_name] -= 1
            del Ride.RIDES_DB[(driver_name, vehicle_number)]
            print("Ride ended")
            return
        else:
            print("No such ride exist that can be ended")
            return

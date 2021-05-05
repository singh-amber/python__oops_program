from user import User

from collections import defaultdict


class Ride:
    # RIDES_DB is static variable
    RIDES_DB = {}
    ENGAGED_AS_DRIVER = defaultdict(int)
    ENGAGED_AS_PASSENGER = set()

    def __init__(self, driver_name, origin, available_seats, vehicle_name, vehicle_number, destination):
        self.driver_name = driver_name
        self.origin = origin
        self.available_seats = available_seats
        self.vehicle_name = vehicle_name
        self.vehicle_number = vehicle_number
        self.destination = destination
        self.RIDES_DB[(driver_name, vehicle_number)] = self

    @staticmethod
    def get_a_suitable_vacant_ride(passenger_name, origin, destination, seats):
        if passenger_name in Ride.ENGAGED_AS_PASSENGER:
            print("This passenger is already travelling in another cab")
            return False

        if Ride.ENGAGED_AS_DRIVER[passenger_name] > 0:
            print("This passenger is a driver and offering a ride, Ask him to first end all rides")
            return False

        maxVacant = 0
        ride_obj = None

        keys = list(Ride.RIDES_DB.keys())
        for key in keys:
            if Ride.RIDES_DB[key].origin == origin and \
                    Ride.RIDES_DB[key].destination == destination and \
                    Ride.RIDES_DB[key].available_seats >= seats and \
                    not (Ride.RIDES_DB[key].driver_name == passenger_name) and \
                    Ride.RIDES_DB[key].available_seats > maxVacant:
                maxVacant = Ride.RIDES_DB[key].available_seats
                ride_obj = Ride.RIDES_DB[key]

        if ride_obj is not None:
            Ride.ENGAGED_AS_PASSENGER.add(passenger_name)
            User.User_DB[passenger_name].rides_taken += 1
            ride_obj.available_seats -= 1
            print(passenger_name, "will be travelling with driver", ride_obj.driver_name, "in vehicle", ride_obj.vehicle_name, "-", ride_obj.vehicle_number)
            return True

        if passenger_name in Ride.ENGAGED_AS_PASSENGER:
            print("This passenger is already travelling with another driver")
        else:
            print("No rides found")
        return False

    @staticmethod
    def get_a_suitable_vehicle(passenger_name, origin, destination, seats, strategy):
        if passenger_name in Ride.ENGAGED_AS_PASSENGER:
            print("This passenger is already travelling in another cab")
            return False

        if Ride.ENGAGED_AS_DRIVER[passenger_name] > 0:
            print("This passenger is a driver and offering a ride, Ask him to cancel all rides")
            return False

        keys = list(Ride.RIDES_DB.keys())
        for key in keys:
            if Ride.RIDES_DB[key].origin == origin and \
                    Ride.RIDES_DB[key].destination == destination and \
                    Ride.RIDES_DB[key].available_seats >= seats and \
                    Ride.RIDES_DB[key].vehicle_name == strategy and \
                    not (Ride.RIDES_DB[key].driver_name == passenger_name):
                Ride.ENGAGED_AS_PASSENGER.add(passenger_name)
                User.User_DB[passenger_name].rides_taken += 1
                Ride.RIDES_DB[key].available_seats -= 1
                print(passenger_name, "will be travelling with driver ", Ride.RIDES_DB[key].driver_name, "in vehicle", Ride.RIDES_DB[key].vehicle_name, "-", Ride.RIDES_DB[key].vehicle_number)
                return True
        return False

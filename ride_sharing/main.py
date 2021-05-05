from query import Query
from user import User
from vehicle import Vehicle

if __name__ == "__main__":
    query_obj = Query()
    query_obj.add_user("Rohan", "M", "36")
    query_obj.add_vehicle("Rohan", "Swift", "KA-01-12345")

    query_obj.add_user("Shashank", "M", "26")
    query_obj.add_vehicle("Shashank", "Baleno", "TS-05-62395")

    query_obj.add_user("Nandani", "F", "29")

    query_obj.add_user("Shipra", "F", "27")
    query_obj.add_vehicle("Shipra", "Polo", "KA-05-41491")
    query_obj.add_vehicle("Shipra", "Activa", " KA-12-12332")

    query_obj.add_user("Gaurav", "M", "29")

    query_obj.add_user("Rahul", "M", "35")
    query_obj.add_vehicle("Rahul", "XUV", "KA-05-1234")

    print("\noffering ride")
    query_obj.offer_ride("Rohan", "Hyderabad", 1, "Swift", "KA-01-12345", "Bangalore")
    query_obj.offer_ride("Shipra", "Bangalore", 1, "Activa", "KA-12-12332", "Mysore")
    query_obj.offer_ride("Shipra", "Bangalore", 2, "Polo", "KA-05-41491", "Mysore")
    query_obj.offer_ride("Shashank", "Hyderabad", 2, "Baleno", "TS-05-62395", "Bangalore")
    query_obj.offer_ride("Rahul", "Hyderabad", 5, "XUV", "KA-05-1234", "Bangalore")
    query_obj.offer_ride("Rohan", "Bangalore", 1, "Swift", "KA-01-12345", "Pune")

    # print("\nselecting ride")
    # query_obj.select_ride("Nandani", "Bangalore", "Mysore", 1, "Most Vacant")
    # query_obj.select_ride("Gaurav", "Bangalore", "Mysore", 1, "Activa")
    # query_obj.select_ride("Shashank", "Mumbai", "Bangalore", 1, "Most Vacant")
    # query_obj.select_ride("Rohan", "Hyderabad", "Bangalore", 1, "Baleno")
    # query_obj.select_ride("Shashank", "Hyderabad", "Bangalore", 1, "Polo")

    print("\nselecting ride")
    query_obj.select_ride("Nandani", "Bangalore", "Mysore", 1, "Most Vacant")
    query_obj.select_ride("Gaurav", "Bangalore", "Mysore", 1, "Activa")

    query_obj.end_ride("Shashank", "Hyderabad", 2, "Baleno", "TS-05-62395", "Bangalore")
    query_obj.select_ride("Shashank", "Mumbai", "Bangalore", 1, "Most Vacant")
    query_obj.offer_ride("Shashank", "Hyderabad", 2, "Baleno", "TS-05-62395", "Bangalore")

    query_obj.end_ride("Rohan", "Bangalore", 1, "Swift", "KA-01-12345", "Pune")
    query_obj.select_ride("Rohan", "Hyderabad", "Bangalore", 1, "Baleno")

    query_obj.select_ride("Shashank", "Hyderabad", "Bangalore", 1, "Polo")

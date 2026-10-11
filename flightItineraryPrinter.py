flight_route = {
    ("New York", "London"),
    ("Athens", "Chicago"),
    ("Madrid", "Rome"),
    ("Venice", "Miami")
}

def print_itinerary(route_list):
    for departure, arrival in route_list:
        print(f"Flight from {departure} to {arrival}")

print_itinerary(flight_route)
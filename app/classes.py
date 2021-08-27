import datetime
from datetime import datetime



class Timetable:
    """
    Class representing timetable, with routes, trips and stops.
    """

    def __init__(self):
        self.routes = {}
        self.stops = {}
        self.stop_names = []

    def create_route(self, route_raptor_id):
        new_route = Route(route_raptor_id)
        new_route.index_routes = self.number_routes
        self.routes[route_raptor_id] = new_route
        return new_route

    def get_route(self, route_raptor_id):
        route = self.routes[route_raptor_id]
        return route

    def create_trip(self, trip_id, route_raptor_id):
        route = self.get_route(route_raptor_id)
        new_trip = Trip(trip_id, route)
        route = self.get_route(route_raptor_id)
        route.trip_ids.append(new_trip)
        return new_trip

    def create_stop(self, stop_name):
        new_stop = Stop(stop_name)
        self.stops[stop_name] = new_stop
        self.stop_names.append(stop_name)
        return new_stop

    def get_route(self, route_raptor_id):
        return self.routes[route_raptor_id]

    def get_stop(self, stop_name):
        return self.stops[stop_name]


class Trip:
    def __init__(self, trip_id, route):
        self.trip_id = trip_id
        self.number_stops = 0
        self.route = route
        self.stop_times = []

    def get_stop_index(self, stop):
        index = self.route.get_stop_index(stop)
        return index

    def get_arr_index(self, stop):
        index = self.get_stop_index(stop) * 2
        return index

    def get_arr(self, stop):
        arr = self.stop_times[self.get_arr_index(stop)]
        return arr

    def get_dep_index(self, stop):
        index = self.get_arr_index(stop) + 1
        return index

    def get_dep(self, stop):
        dep = self.stop_times[self.get_dep_index(stop)]
        return dep


class Route:
    """
    Class representing routes
    """
    def __init__(self, route_raptor_id):
        self.route_raptor_id = route_raptor_id
        self.name = None
        self.number_stops = 0
        self.number_trips = 0
        self.stop_names = []
        self.trip_ids = []
        # stops - nazvy zastavek

    def get_stop_index(self, stop):
        index = self.stop_names.index(stop.stop_name)
        return index

    def get_stop_sequence(self, stop):
        sequence = self.get_stop_index(stop.stop_name) + 1
        return sequence

    def create_departure_list(self, stop, arr_depp_list):
        stop_sequence = self.get_stop_sequence(stop.stop_name)
        index_first_arrival = 2 * (stop_sequence - 1)
        index_first_departure = index_first_arrival + 1
        departures = []
        for trip in range(self.number_trips):
            index = index_first_departure + trip * self.number_stops * 2
            departures.append(arr_depp_list[index])
        return departures

    def find_arrival_time(self, stop, trip_sequence, arr_depp):
        stop_sequence = self.get_stop_sequence(stop)
        arrival_index = 2 * (stop_sequence - 1) + \
                        (trip_sequence - 1) * (self.number_stops)
        arrival_time = arr_depp[arrival_index]
        return arrival_time

    def get_rest_stops(self, stop):
        stop_index = self.stop_names.index(stop.stop_name)
        rest_stops = self.stop_names[(stop_index + 1):]
        return rest_stops





class Stop:
    """Class representing Stops"""
    def __init__(self, stop_name):
        self.stop_name = stop_name
        self.routes = []
        self.best_arrival_time = datetime.strptime('23:59:59', '%H:%M:%S')
        self.departure_time = time1
        self.marked = False
        self.previous = None

    def get_path(self):
        path = [(self.stop_name,self.best_arrival_time,None,None)]
        stop=self
        while stop.previous:
            #(stop_name, arrival time, departure_time, line)
            path.append((stop.previous[0].stop_name,
                         stop.previous[0].best_arrival_time,
                         stop.previous[1],
                         stop.previous[2]))
            stop = stop.previous[0]
        path.reverse()
        return path

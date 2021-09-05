from helpers import *
from classes import *
from raptor import raptor
source = "myraptor/data/timetable_metro_tram_bus.csv"

def main():
    tb = read_timetable(source)
    start_stop_name = load_start_stop(tb)
    target_stop_name = load_target_stop(tb)
    start_time = load_start_time()
    transfers = load_transfers()
    raptor(tb,start_stop_name,target_stop_name,start_time,transfers)



if __name__ == '__main__':
    main()



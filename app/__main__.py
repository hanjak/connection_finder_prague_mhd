from helpers import *
from classes import *
from raptor import raptor
source = "timetable.csv"

def main():
    print ("main")
    tb = read_timetable(source)
    start_stop_name = load_start_stop(tb)
    target_stop_name = load_target_stop(tb)
    start_time = load_start_time()
    transfers = load_transfers()
    result = raptor(tb,start_stop_name,target_stop_name,start_time,transfers)



if __name__ == '__main__':
    main()



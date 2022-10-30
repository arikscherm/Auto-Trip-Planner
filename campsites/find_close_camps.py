import math


#will be passed from send camps
given_coordinates = {"latitude":37.2753,"longitude":-107.8801}


#Need to format message and refactor but should work other than that.
#Create dictionary of with Coordinates : Camp Information pairs
def read_camps_text():
    camp_list = ['']
    camps_by_gps = {}
    #gps_key = ''
    #f = open('results.txt','r')
    f = open('campsites/results.txt', 'r')
    for line in f:
        camp_list[len(camp_list)-1] += line.replace('\n','  ')

        if(line[0:4] == 'GPS:'):
            coordinates_from_text = line[5:].replace('\n','')
            gps_key = coordinates_from_text

        elif('*' in line):
            camps_by_gps[gps_key] = camp_list[len(camp_list)-1]
            gps_key = ''
            camp_list.append(line)

    f.close()

    return camps_by_gps

#Create dicitonary of Coordinates : Distance from given coordinates - pairs
def find_camp_distances(coordinates,camps_by_gps):
    camp_distances_by_gps = {}
    list_of_all_camp_coordinates = camps_by_gps.keys()
    for camp_coordinates in list_of_all_camp_coordinates:
        #should just use list comprehension
        camp_coordinates_as_list = camp_coordinates.split(',')
        camp_coordinates_object = {"latitude":float(camp_coordinates_as_list[0]),"longitude":float(camp_coordinates_as_list[1])}
        
        camp_distances_by_gps[camp_coordinates] = math.dist([camp_coordinates_object["latitude"],camp_coordinates_object["longitude"]],[coordinates["latitude"],coordinates["longitude"]])
    return camp_distances_by_gps

#get 5 closest camp's gps
def find_closest_camps(camp_distances_by_gps):

    sorted_camps_distances = sorted(camp_distances_by_gps.items(),reverse=True)
    close_camps = sorted_camps_distances[:3]
    return close_camps


def get_close_camp_info(close_camps,camps_by_gps):
    close_camps_info = []
    close_camps_string = ""
    for i in close_camps:
        close_camps_info.append(camps_by_gps[i[0]])

    for i in close_camps_info:
        close_camps_string += i + '\n' + '\n'
    return close_camps_string



def prepare_message(coordinates):
    camps_by_gps = read_camps_text()
    camp_distances_by_gps = find_camp_distances(coordinates,camps_by_gps)
    close_camps = find_closest_camps(camp_distances_by_gps)
    closest_camps_info = get_close_camp_info(close_camps,camps_by_gps)
    
    #print(closest_camps_info)
    closest_camps_info =   closest_camps_info.replace('"',"'")
    return closest_camps_info


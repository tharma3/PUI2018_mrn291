# Author: Martha Norrick, NYU, September 2018
##################################
# Code written to demonstrate understanding of how to interact with API data

from __future__ import print_function
import pylab as pl
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if len(sys.argv) != 3:
    print("Invalid number of arguments. Run script as python get_bus_info_mrn291.py <BUS_LINE> <BUS_LINE>.csv. Note bus lines are case sensitive.")

#get the data from mta
url_base = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='
vehicle_base = "&VehicleMonitoringDetailLevel=calls&LineRef="
mta_key = os.getenv("MTAKEY")
bus_name = sys.argv[1]

url_compiled = url_base + mta_key + vehicle_base + bus_name

#load data from url
response = urllib.urlopen(url_compiled)
data = response.read().decode("utf-8")
data = json.loads(data)

#calculate the number of buses
number_of_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

#set up the file to write to
file = open(sys.argv[2], "w")
file.write(("Latitude, Longitude, Stop Name, Stop Status")+"\n")

for i in range(number_of_buses):
    stop_name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    stop_status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][i]['Extensions']['Distances']['PresentableDistance']
    latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if stop_name is None:
        stop_name = "N/A"
    else:
        stop_name
    
    if stop_status is None:
        stop_status = "N/A"
    else:
        stop_status
    
    if latitude is None:
        latitutde = "N/A"
    else:
        latitude
    
    if longitude is None:
        longitude = "N/A"
    else:
        longitude
    
    line = "%f, %f, %s, %s"%(latitude, longitude, stop_name, stop_status)
    file.write(line+"\n")
    
    
    
    
    

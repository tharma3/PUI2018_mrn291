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
    print("Invalid number of arguments. Run script as python Assignment_3.py <MTA_KEY> <BUS_LINE>. Note bus lines are case sensitive.")

#get the data from mta
url_base = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='
vehicle_base = "&VehicleMonitoringDetailLevel=calls&LineRef="
mta_key = sys.argv[1]
bus_name = sys.argv[2]

url_compiled = url_base + mta_key + vehicle_base + bus_name

#load data from url
response = urllib.urlopen(url_compiled)
data = response.read().decode("utf-8")
data = json.loads(data)

bus_line_name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']
number_of_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print("Bus Line :", bus_line_name)
print("Number of Active Buses: ", number_of_buses)

for i in range(number_of_buses):
    latitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    longitude = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus %s is at latitude %s and longitude %s." %(i+1, latitude, longitude))
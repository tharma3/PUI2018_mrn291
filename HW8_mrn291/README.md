# Homework Assignment 8 for PUI2018 Evening Session

#### Assignment 1
For this assignment, we were asked to make a plot of whatever data we wanted of urban relevance and upload [the code that generates the plot](https://github.com/tharma3/PUI2018_mrn291/blob/master/HW8_mrn291/Assignment_1.ipynb) into this repo.

The dataset I used for this assignment is an anonymized list of citizens in New York City who may be vulnerable (i.e. have difficulty evacuating) in the event of a coastal storm. I have access to this list through my job but it is not publicly released. To preprocess this data, I used a spatial join of this client list against the [Sandy Inundation Zone](https://data.cityofnewyork.us/Environment/Sandy-Inundation-Zone/uyj8-7rv5) from New York City Open Data to filter the list to just clients in the Sandy Inundation Zone, and then joined the [PLUTO Data](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page) to get the type of building (building class) from the PLUTO dataset.

Here is the plot:

![womp womp](https://github.com/tharma3/PUI2018_mrn291/blob/master/HW8_mrn291/distribution_by_borough.png)

Figure showing the distribution of the 4 major housing types in each borough for clients who are potentially vulnerable in the event of a coastal storm.
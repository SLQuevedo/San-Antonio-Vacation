# San Antonio Airport Vacation Dashboard

## Project Proposal

Our webpage explores and visualizes 105 possible vacation destinations to visit by flight from San Antonio, Texas. 39 locations are available through direct flights and 46 are available through flights with a layover. Information collected about each possible destination city includes the weather there, the choice of several hotels nearby, and several different possible activities to engage in while vacationing this fall.

 In addition, an international map is included that marks each destination city. Further interaction with the marker in each city displays additional information.
 
We used the following original data sources for this project: https://transtats.bts.gov/AIRFARES/
https://aviation-edge.com/developers/
https://openweathermap.org/api
https://flysanantonio.com/home/flights/nonstop-destinations/
https://maps.googleapis.com/maps/api/place/nearbysearch/json

##Table of Contents
•	[Extract](#extract)
•	[Transform](#transform)
• [Load](#load)
•	[Credits](#credits)
•	[Results](#rsults)



##Extract

The data used from [Aviation edge API]( https://aviation-edge.com/developers/) are all CSV files, while the data used from Flight Destinations is a scraped website.

We selected the [Aviation edge API]( https://aviation-edge.com/developers/) dataset because it was the only data, we found that contained all the airport codes and flight destinations. 

A secondary dataset was utilized from [Flight Destinations](https://flysanantonio.com/home/flights/nonstop-destinations/) to determine what indirect and direct flights came out of San Antonio. A [Jupyter Notebook](https://github.com/SLQuevedo/project-3/blob/main/data/airports.ipynb) was implemented to scrape flights location for the destinations. 

##Transform

With the Flight Destinations data, we scraped the website to set flight destinations and converted data into a Jason format.  

To transform the public data and use it in our analysis, we executed the following:
•	Leveraged Pandas functions in Jupyter Notebook to load all several CSV files
•	Inspected the files and converted them into data frames
•	Created different data frames and queries to extract information for San Antonio Airport destinations. We then created a Jason file to levarge for JS and HTML files. 
We transformed our datasets with the above information to be able to get the most succinct results possible. 

##Load
The final database we used to obtain Best rated Hotel and Restaurants. 

We chose a relational database because our datasets because of it easy to use functionalities. 

##Results
Temperature Gauge by City

 

Best Restaurants and Hotels
 
 
Average Ticket Price  

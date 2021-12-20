# sqlalchemy-challenge- Surfs Up!

### Background
Using sqlalchemy to performed climate analysis of Honolulu, Hawaii! 
## Climate Analysis and Exploration

 All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Used pandas for data exploration.

* Used SQLAlchemy `create_engine` to connect to your sqlite database.

* Used SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

* Linked Python to the database by creating an SQLAlchemy session.


### Precipitation Analysis

* Started by finding the most recent date in the data set.

* Retrived the last 12 months of precipitation data by querying the 12 preceding months of data. 

* Only `date` and `prcp` values were selected.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* DataFrame values was sorted by `date`.


  ![precipitation](Images/precipitation.png)

* Used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Designed a query to calculate the total number of stations in the dataset.

* Designed a query to find the most active stations (i.e. which stations have the most rows?).

  * To list the stations and observation counts in descending order.

  * Which station id has the highest number of observations?

  * Using the most active station id, calculate the lowest, highest, and average temperature.


* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Query the last 12 months of temperature observation data for this station.

  * Plot the results as a histogram with `bins=12`.

    ![station-histogram](Images/station-histogram.png)

* Closed the session.

- - -

## Step 2 - Climate App

After completing  initial analysis, I also designed a Flask API based on the above queries 

* Used Flask to create  routes.

### Routes

* `/`

  * Home page.

  * To list all routes that are available.

* `/api/v1.0/precipitation`

  * To convert the query results to a dictionary using `date` as the key and `prcp` as the value and return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * To return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * To query the dates and temperature observations of the most active station for the last year of data.

  * To return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * To return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


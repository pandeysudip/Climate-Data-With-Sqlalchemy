from flask import Flask, jsonify
import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, and_
import numpy as np
import pandas as pd

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn=engine.connect()

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the climate app API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2017-08-15 and /api/v1.0/2017-08-15/2017-08-23"
    )
@app.route("/api/v1.0/precipation")
def precipation():
    #create  a session from python to DB
    session=Session(engine)
    #query date and prcp
    results=session.query(Measurement.date, Measurement.prcp)\
                        .group_by(Measurement.date).all()
    session.close()
    #create a dictionary
    date_dict={}
    for date, prcp, in results:
        date_dict[date]=prcp

    return jsonify(date_dict)

@app.route('/api/v1.0/stations')
def stations():
    session=Session(engine)
    results=session.query(Station.station).all()
    session.close()
    all_names=list(np.ravel(results))
    return jsonify(all_names)

@app.route('/api/v1.0/tobs')
def tobs():
    session=Session(engine)
    results=session.query( Measurement.date, Measurement.tobs)\
                    .filter(Measurement.station == 'USC00519281')\
                    .filter(Measurement.date > '2016-08-23').all()
    session.close()
    all_dates=[]
    for date, temp in results:
        date_dict={}
        date_dict['date']=date
        date_dict['temp']=temp
        all_dates.append(date_dict)
    
    return jsonify(all_dates)

@app.route("/api/v1.0/<start>")
def temp_range(start):
    session=Session(engine)
    results=session.query(func.min(Measurement.prcp),
                        func.avg(Measurement.prcp),
                        func.max(Measurement.prcp) )\
                        .filter(Measurement.date >= start)\
                        .filter(Measurement.date <= '2017-08-23').all()
    
    session.close()
    all_temp=list(np.ravel(results))
    return jsonify(all_temp)

@app.route("/api/v1.0/<start>/<end>")
def temprange1(start, end):
    session=Session(engine)
    results=session.query(func.min(Measurement.prcp),
                        func.avg(Measurement.prcp),
                        func.max(Measurement.prcp) )\
                        .filter(Measurement.date >= start)\
                        .filter(Measurement.date <= end).all()
    
    session.close()
    all_temp=list(np.ravel(results))
    return jsonify(all_temp)

if __name__ == "__main__":
    app.run(debug=True)



import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Save reference to the table

engine = create_engine('sqlite:///my_data2.db')


# Flask Setup
#################################################
app = Flask(__name__)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

table = Base.classes.users2
# Flask Routes- Welcome Page

@app.route("/")
def welcome():
    return (
        f"Please Choose a Route to Explore Restaurants for your Vacation:<br/>"
        
        f"/api/v1.0/City_Code<br/>"
        
        f"/api/v1.0/High_Rating<br/>"
        
        f"/api/v1.0/All_Restaurants<br/>"
    )


# City_Code Route

@app.route("/api/v1.0/<City_Code>")
def City_Code(City_Code):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
    results = session.query(table.Restaurant_Name, table.Address).filter(table.City_Code == City_Code).all()

    session.close()

    # # Convert list of tuples into normal list
    all_codes = list(np.ravel(results))

    return jsonify(all_codes)


# Rating Route

@app.route("/api/v1.0/High_Rating")
def Rating():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
    results = session.query(table.Restaurant_Name,table.Rating,table.Address).filter(table.Rating >= 3.5).all()

    session.close()

    # Convert list of tuples into normal list
    ratings = list(np.ravel(results))

    return jsonify(ratings)


# Restaurant_Name

@app.route("/api/v1.0/All_Restaurants")
def Restaurant_Name():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all Restaurant_Names
    results3 = session.query(table.Restaurant_Name,table.Rating,table.Address).all()

    session.close()

    # Convert list of tuples into normal list
    all_Restaurants = list(np.ravel(results3))

    return jsonify(all_Restaurants)


if __name__ == '__main__':
    app.run(debug=True)
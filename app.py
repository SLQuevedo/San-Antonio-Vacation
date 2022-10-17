import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


# Database Setup

engine = create_engine("sqlite:///data/my_data.db")

#reflect an existing database into a new mocel
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

#Save references to the tables
Users = Base.classes.users

# Flask Setup

app = Flask(__name__)
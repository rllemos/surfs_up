# Import dependencies
from flask import Flask

app = Flask(__name__)

# engine=create_engine("sqlite:///hawaii.sqlite")

# Base =automap_base()

# Base.prepare(engine , reflect =True)

# Measurement =Base.classes.measurement
# Station =Base.classes.station

# session =Session(engine)


# @app.route('/')
# def welcome ():
#     return(

    # )
@app.route('/')
def hello_world():
    return 'Hello world'
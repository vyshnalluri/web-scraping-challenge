from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_data_dict = mongo.db.mars_data_dict.find_one()

    # Return template and data
    return render_template("index.html", mars_data_dict=mars_data_dict)

@app.route("/scrape")
def scrape():
    mars_data_dict =  mongo.db.mars_data_dict

    mars_dict = scrape_mars.scrape_all()

    mongo.db.mars_data_dict.update({}, mars_dict, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)

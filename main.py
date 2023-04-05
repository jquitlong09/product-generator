from flask import Flask
from flask_cors import CORS

from v1.blueprints.ads import ads as ads_blueprint

app = Flask(__name__)
CORS(app)

# Blueprint registration
app.register_blueprint(ads_blueprint)

# Entry point of the application
app.run(debug=True, port=8010)

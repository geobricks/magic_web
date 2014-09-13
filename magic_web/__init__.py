from flask import Flask
from flask.ext.cors import CORS
from importlib import import_module
from pgeo.error.custom_exceptions import PGeoException
from flask import jsonify
from flask import render_template
from config.settings import modules


# Initialize the Flask app
app = Flask(__name__)


# Initialize CORS filters
cors = CORS(app, resources={r'/*': {'origins': '*'}})


# Custom error handling
@app.errorhandler(PGeoException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Root REST
@app.route('/')
def root():
    return 'Welcome to MagicWeb!'


# Dynamic import of modules specified in config.settings.py
for module in modules:

    # Load module
    mod = import_module(module['module_name'])

    # Load Blueprint
    rest = getattr(mod, module['rest_name'])

    # Register Blueprint
    app.register_blueprint(rest, url_prefix=module['url_prefix'])


# Start Flask server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True, threaded=True)
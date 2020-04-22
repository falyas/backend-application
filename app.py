from flask import  Flask

# Create an application that gets named after the name of our file
app = Flask(__name__)

# Set up a route to listen to our homepage, the route handler is index
@app.route('/')
def index():
    # return a template html file to render an
    # html file for the user whenever the user visits this route
    # by default, Flask looks for template files in a file called templates
    # inside the project directory, so index.html is inside the templates folder
    render_template('index.html')

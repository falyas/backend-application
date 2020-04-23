from flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create an application that gets named after the name of our file
app = Flask(__name__)

# configure flask application to connect to a particular database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:_fullstack_@localhost:5432/todo'

# define a db object to link SQLAlchemy to flask app
db = SQLAlchemy(app)

# create a table for the Todo-list model
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)

    # Printing method for debugging
    def __repr__(self):
        return f'<Todo {self.id}> {self.description}>'

# for each model class, this call create table if a table doesn't already exist
# otherwise this call, does nothing
db.create_all()

# Set up a route to listen to our homepage, the route handler is index
@app.route('/')

# This method acts as the controller. It routes commands to models and views
# return a template html file to render an
# html file for the user whenever the user visits this route
def index():
    # by default, Flask looks for template files in a file called templates
    # inside the project directory, so index.html is inside the templates folder
    # Pass data to render_template with list of items to render in our todo list
    return render_template('index.html', data=Todo.query.all())

if __name__ == '__main__':
    app.run(debug=True)

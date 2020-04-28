from flask import  Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create an application that gets named after the name of our file
app = Flask(__name__)

# configure flask application to connect to a particular database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:_fullstack_@localhost:5432/tododb'

# disable warnings about import python files that use SQLAlchemy in the python interpreter
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# define a db object to link SQLAlchemy to flask app
db = SQLAlchemy(app)

# link flask app and database instance together to set up migrations
# The Migrate function allows us to use  the migratation commands to initiate migrations files, upgrade and downgrade our database
migrate = Migrate(app, db)

# create a table for the Todo-list model
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    # Printing method for debugging
    def __repr__(self):
        return f'<Todo {self.id}> {self.description}>'

# for each model class, this call create table if a table doesn't already exist
# otherwise this call, does nothing
# db.create_all()

# Set up a route endpoint to handle user form input
@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        # The request.get_json() method fetches the json body that was sent to it
        # in our case, the json body contains the keyword description
        # the json body is given as a dictionary
        # use [] to get the description field inside the json body
        # add record to database
        todo_description = request.get_json()['description']
        todo_item = Todo(description=todo_description)
        db.session.add(todo_item)
        db.session.commit()
        # update the json object
        body['description'] = todo_item.description
    except:
         error = True
         db.session.rollback()
         print(sys.exc_info())
    finally:
         db.session.close()
    if error:
         abort(400)
    else:
         return jsonify(body)

# Set up a route endpoint to listen to our homepage, the route handler is index
@app.route('/')
# This method acts as the controller. It routes commands to models and views
# return a template html file to render an
# html file for the user whenever the user visits this route
def index():
    # by default, Flask looks for template files in a file called templates
    # inside the project directory, so index.html is inside the templates folder
    # Pass data to render_template with list of items to render in our todo list
    return render_template('view.html', data=Todo.query.all())

# run the flask app from the command
#if __name__ == '__main__':
#    app.run(debug=True)

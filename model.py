from flask import  Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create an application that gets named after the name of our file
app = Flask(__name__)

# configure flask application to connect to a particular database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/todo'

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

# Set up a route endpoint to handle user form input
@app.route('/todos/create', methods=['POST'])
def create_todo():
    todo_description = request.form.get('description', '')
    if todo_description == '':
        skip
    else:
        # add record to database
        todo_item = Todo(description=todo_description)
        db.session.add(todo_item)
        db.session.commit()
        # refresh records and redirect user to the index endpoint
        return redirect(url_for('index'))

# Set up a route endpoint to listen to our homepage, the route handler is index
@app.route('/')
# This method acts as the controller. It routes commands to models and views
# return a template html file to render an
# html file for the user when222222ever the user visits this route
def index():
    # by default, Flask looks for template files in a file called templates
    # inside the project directory, so index.html is inside the templates folder
    # Pass data to render_template with list of items to render in our todo list
    return render_template('view.html', data=Todo.query.all())

if __name__ == '__main__':
    app.run(debug=True)

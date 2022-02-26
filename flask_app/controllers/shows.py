from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.show import TV_Shows
from flask_app.models.user import User

# New Tv Show 
@app.route('/new/show')
def new_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : session['user_id']
    }
    return render_template('new.html', user = User.get_by_id(data))

# Create New TV Show
@app.route('/create/show', methods = ['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not TV_Shows.validate_show(request.form):
        return redirect('/new/show')
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    TV_Shows.save(data)
    return redirect('/dashboard')

# Edit The Tv Show
@app.route('/edit/show/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    user_data = {
        "id" : session['user_id']
    }
    return render_template("edit_show.html", edit = TV_Shows.get_one(data), user = User.get_by_id(user_data))

# Update The Tv Show
@app.route('/update/show', methods = ['POST'])
def update_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not TV_Shows.validate_show(request.form):
        return redirect('/new/show')
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": (request.form["description"]),
        "id": request.form['id']
    }
    TV_Shows.update(data)
    return redirect('/dashboard')

# Show the specific Tv Show from a specific user
@app.route('/show/<int:id>')
def display_tv_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    user_data = {
        "id" : session['user_id']
    }
    return render_template("show.html", show = TV_Shows.get_one(data), user = User.get_by_id(user_data))

# Delete The Recipe 
@app.route('/destroy/show/<int:id>')
def destroy_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    TV_Shows.destroy(data)
    return redirect('/dashboard')
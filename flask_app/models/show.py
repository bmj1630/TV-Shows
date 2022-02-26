from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class TV_Shows:
    db = 'tv-shows'
    def __init__(self, db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.network = db_data['network']
        self.release_date = db_data['release_date']
        self.description = db_data['description']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']

#Create TV Show
    @classmethod
    def save(cls, data):
        query = "INSERT INTO shows (title, network, release_date, description, user_id) VALUES (%(title)s,%(network)s,%(release_date)s,%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

#Select All TV Shows
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_shows = []
        for row in results:
            all_shows.append( cls(row) )
        return all_shows

#Select All Tv Shows By ID
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls( results[0] )

# Update Tv Shows
    @classmethod
    def update(cls, data):
        query = "UPDATE shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

# Delete Tv Shows
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

# Validate Tv Shows
    @staticmethod
    def validate_show(show):
        is_valid = True
        if len(show['title']) < 3:
            is_valid = False
            flash("The Title must be at least 3 characters","show")
        if len(show['network']) < 3:
            is_valid = False
            flash("The Network must be at least 3 characters","show")
        if len(show['description']) < 3:
            is_valid = False
            flash("The Description must be at least 3 characters","show")
        if show['release_date'] == "":
            is_valid = False
            flash("Please enter a date","show")
        return is_valid
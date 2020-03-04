
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


Class Tribe(db.Model):
	"""Indigeneous peoples in North America"""

	__tablename__ = "tribe"

	tribe_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	name = db.Column(db.String(), nullable=False, unique=True)
	common_name = db.Column(db.String(), nullable=True)
	earliest_location = db.relationship("Location", backref=) #Finish backref link
	current_location = db.relationship("Location", backref=) #Finish backref link
	language = db.Column(db.String(), nullable=True)
	language_family = db.Column(db.String(), nullable=True)

	def __repr__(self):

		return f"<Tribe id = {tribe_id}, name = {name}>"


Class Location(db.Model):
	"""Location in latitude and longitude"""

	__tablename__ = "location"

	location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	latitude = db.Column(db.Integer, nullable=False)
	longitude = db.Column(db.Integer, nullable=False)
	region = db.Column(db.String(), nullable=True)

	def __repr__(self):

		return f"<Location id = {location_id} region = {region}>"



def connect_to_db(app):

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tribes'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.app = app
	db.init_app(app)


if __name__ == "__main__":

	from server import app
	connect_to_db(app)
	print("Connected to database.")
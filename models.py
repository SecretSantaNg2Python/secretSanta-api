from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	full_name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	password = db.Column(db.String, nullable=False)

	def __init__(self, full_name, email, password):
		self.full_name = full_name
		self.email = email
		self.password = password

	def __repr__(self):
		return '<id {}>'.format(self.id)
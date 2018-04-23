from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Home(Resource):
	def get(self):
		return {'message': 'Your API is runing....'}




api.add_resource(Home, '/')
app.run(port=5000)

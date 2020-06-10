from BackEnd import flaskAppInstance
from BackEnd import app
from BackEnd import models
from BackEnd import db, migrate
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow
from flask import request


#Marshmallow instance used to send data in a json format
ma = Marshmallow(flaskAppInstance)

class EmployeeModelSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "phone")

post_schema = EmployeeModelSchema()
posts_schema = EmployeeModelSchema(many=True)





#Class to get/post entire list of entries.
class PostListResource(Resource):
    def get(self):
        posts = models.EmployeeModel.query.all()
        return posts_schema.dump(posts)
    def post(self):
        new_post = models.EmployeeModel(
            name=request.json['name'],
            email=request.json['email'],
            phone=request.json['phone']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)    




#Class to call a celery task.
class CeleryTest(Resource):
    def post(self):
        #Actual celery task
        app.celery_insert.delay()

        #Dummy table entry to be returned from api.
        new_post = models.EmployeeModel(
            name="Dummy",
            email="Dummy@gmail.com",
            phone=000
        )
        return post_schema.dump(new_post)




#Class to get single table resource by id
class PostResource(Resource):
    def get(self, post_id):
        post = models.EmployeeModel.query.get_or_404(post_id)
        return post_schema.dump(post)

    def patch(self, post_id):
        post = models.EmployeeModel.query.get_or_404(post_id)

        if 'name' in request.json:
            post.name = request.json['name']
        if 'email' in request.json:
            post.email = request.json['email']
        if 'phone' in request.json:
            post.phone = request.json['phone']    

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, post_id):
        post = models.EmployeeModel.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204    

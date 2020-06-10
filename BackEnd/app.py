from BackEnd import flaskAppInstance
from BackEnd import models
from BackEnd import db
from flask_restful import Api, Resource
from BackEnd import tasks
from BackEnd.ApiRoute import PostListResource, PostResource, CeleryTest
from BackEnd import celery


#Flask-Restful API definition
api = Api(flaskAppInstance)

#PostGRES Table Initialization
db.init_app(flaskAppInstance)
db.create_all()


#API Routes Definitions
api.add_resource(PostListResource, '/posts')
api.add_resource(PostResource, '/posts/<int:post_id>')
api.add_resource(CeleryTest, '/tester')



#####CELERY TASK#####

@celery.task(name="celery_example.insert")
def celery_insert():
            new_post = models.EmployeeModel(
                name="CeleryTester",
                email="CeleryTester@gmail.com",
                phone=000
            )
            db.session.add(new_post)
            db.session.commit()
            return "Done"


#####################

@flaskAppInstance.route('/')
@flaskAppInstance.route('/index')
def index():
    return "SERVER IS LIVE"




if __name__ == '__main__':
    flaskAppInstance.run(debug=True,use_reloader=True)
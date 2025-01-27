from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views} likes = {likes})"

# db.create_all()  # This is done only once as we dont want to rewrite the db everytime we run the code

video_put_args = reqparse.RequestParser() # Parses the request and makes sure the=at its passing the guidelines that is defined
video_put_args.add_argument("name", type=str, help="Name of the video is needed", required=True)
video_put_args.add_argument("likes", type=int, help="No of likes of the video")
video_put_args.add_argument("views", type=int, help="No of views of the video")

'''
def abort_if_video_id_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video_id doesn't exists")

def abort_if_video_id_exist(video_id):
    if video_id in videos:
        abort(409, message="Video already exits")
'''

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        results = VideoModel.query.get(id=video_id)
        return results
    '''
    def put(self, video_id):
        abort_if_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201  # that is status code (200 is representing ok)
    def delete(self, video_id):
        abort_if_video_id_not_exist(video_id)
        del videos[video_id]
        return "", 204
    '''


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
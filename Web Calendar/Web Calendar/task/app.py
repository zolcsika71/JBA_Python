from flask import Flask
from flask_restful import Api, Resource, reqparse, inputs, marshal_with, fields, abort
from flask_sqlalchemy import SQLAlchemy
from os import path
import sys
import datetime

DB_NAME = 'events.db'

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


def create_database(app_):
    if not path.exists(DB_NAME):
        db.create_all(app=app_)
        print('Database created!')


create_database(app)

post_resource_fields = {
    'message': fields.String,
    'event': fields.String,
    'date': fields.DateTime(dt_format='iso8601')
}

get_resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.DateTime(dt_format='iso8601')
}

delete_resource_fields = {
    'message': fields.String
}


@api.resource('/event')
class GetEvent(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'start_time',
        type=inputs.date,
        help='',
        required=False
    )

    parser.add_argument(
        'end_time',
        type=inputs.date,
        help='',
        required=False
    )

    @marshal_with(get_resource_fields)
    def get(self):

        args = self.parser.parse_args()

        # get event by date range
        if args['start_time'] and args['end_time']:

            result = Events.query.filter(Events.date.between(args['start_time'], args['end_time'])).all()

            if not result:
                abort(404, message='There are no events for this date range!')

            return result, 200

        else:
            # get all events
            result = Events.query.all()

            if not result:
                abort(404, message='There are no events in database!')

            return result, 200


@api.resource('/event/<int:event_id>')
class GetEventByID(Resource):

    @marshal_with(get_resource_fields)
    def get(self, event_id):

        result = Events.query.filter_by(id=event_id).first()

        if not result:
            abort(404, message="The event doesn't exist!")

        return result, 200

    @marshal_with(delete_resource_fields)
    def delete(self, event_id):

        result = Events.query.filter_by(id=event_id).first()

        if not result:
            abort(404, message="The event doesn't exist!")

        db.session.delete(result)
        db.session.commit()

        result.message = 'The event has been deleted!'

        return result, 200


@api.resource('/event/today')
class GetTodayEvent(Resource):

    @marshal_with(get_resource_fields)
    def get(self):
        today = datetime.datetime.today().date()

        result = Events.query.filter_by(date=today).all()

        if not result:
            abort(404, message='There are no events for today!')

        return result, 200


@api.resource('/event')
class PostEvent(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'event',
        type=str,
        help="The event name is required!",
        required=True
    )

    parser.add_argument(
        'date',
        type=inputs.date,
        help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
        required=True
    )

    @marshal_with(post_resource_fields)
    def post(self):
        args = self.parser.parse_args()

        result = Events(event=args['event'], date=args['date'])
        db.session.add(result)
        db.session.commit()

        result.message = 'The event has been added!'

        return result, 200


# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()

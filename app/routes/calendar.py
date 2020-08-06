from app.models.models import db, Calendar
from flask_restx import Resource, Namespace, fields
import datetime

api = Namespace('calendar', description='Calendar operations')

# expected information
model = api.model("Calendar",
                {
                    "start_date": fields.Date(required=True, description="Calendar start date"),
                    "end_date": fields.Date(required=True, description="Calendar end date"),
                    "location_id": fields.Integer(required=True, description="Calendar location"),
                    "user_id": fields.Integer(required=True, description="Calendar user"),
                }
)

@api.route("/")
class Calendars(Resource):
    '''Get all Scheduled Calendar Ranges'''
    def get(self, location_id):
        '''Get all Calendar Bookings'''
        dates = Calendar.query.filter_by(location_id=location_id).all()

        data = [day.to_dictionary() for day in dates]
        return {"dates": data}

    @api.expect(model)
    def post(self, location_id):
        '''Create a new calendar booking with the provided date range'''
        data = api.payload
        print(data)
        dates = Calendar.query.filter_by(location_id=location_id).all()
        print(dates)
        if bool(dates) == False:
            calendar = Calendar(**data)
            db.session.add(calendar)
            db.session.commit()

            return {"Message": "Successfully scheduled!"}
        else:
            return {"Message": "TODO"}

        # get the calendar for the location

        # if nothing found, safe to post
        # else need to check if the dates are available if true we can post


    #     calendar_data={
    #         "start_date":data["start_date"],
    #         "end_date":data["end_date"],
    #     }
    #     # get the dates in a range
    #     calendar_array = []
    #     # get the first date
    #     new_date = data["start_date"]
    #     while (new_date <= data["end_date"]):
    #         # store and format the date
    #         temp_date = new_date
    #         # increment the date
    #         new_date =
    #         # push the date to the date array

    #     # check if the days selected are available, (are not already in another calendar range)

    #     scheduled_dates = Calendar.query.filter_by(
    #         start_date = calendar_data["start_date"],
    #         end_date = calendar_data["end_date"]
    #     )

    #     # if the date exists in the calendar range,

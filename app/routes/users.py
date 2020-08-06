from app.models.models import db, User
from flask_restx import Resource, Namespace, fields

api = Namespace('users', description='Create and update user operations')

model = api.model("User", {
                            "firstName": fields.String( description="User first name."),
                            "lastName": fields.String( description="User last name."),
                            "userInfo": fields.String( description="User information."),
                            "domicileType": fields.String( description="User domicile type."),
                            "phoneNumber": fields.String( description="User phone number."),
                            "password": fields.String( description="User Password."),
                            })

@api.route("/<int:id>")
@api.response(404, 'User not found')
@api.param('id', 'The user identifier')
class GetUser(Resource):
    @api.response(200, 'User found')
    @api.doc('get_user')
    def get(self, id):
        '''Get user by user id'''
        user = User.query.get(int(id))
        if user == None:
            return {"message": "no user found for the requested id"}, 404

        return {"user":user.to_dictionary()}
    @api.doc('update_user')
    @api.response(201, 'User record updated')
    @api.expect(model)
    def put(self, id):
        '''Update user record by user id'''
        user = User.query.get(int(id))
        if user == None:
            return {"message": "no user found for the requested id"}

        user.image_url = api.payload["image_url"]
        user.password = api.payload["password"]
        user.phone_number = api.payload["phoneNumber"]
        user.user_Info = api.payload["userInfo"]
        user.domicile_type = api.payload["domicileType"]
        user.first_name = api.payload["firstName"]
        user.last_name = api.payload["lastName"]
        db.session.commit()

        return {"message":"User record updated successfully."}

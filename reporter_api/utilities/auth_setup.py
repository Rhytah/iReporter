# import jwt
# def encode_auth_token(self, user_id):
#     """
#     Generates the Auth Token
#     :return: string
#     """
#     try:
#         payload = {
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
#             'iat': datetime.datetime.utcnow(),
#             'sub': user_id
#         }
#         return jwt.encode(
#             payload,
#             app.config.get('SECRET_KEY'),
#             algorithm='HS256'
#         )
#     except Exception as e:
#         return e

from functools import wraps
from flask import jsonify, request
import jwt



def jwt_required(func):
    ''' Decorator for endpoint functions '''
    @wraps(func)
    def authorize(*args, **kwargs):
        ''' Check for the user's authentication token in header '''

        if 'Authorization' not in request.headers:
            response = jsonify({
                "message": "Missing Authorization header"
            })
            response.status_code = 401
            return response

        jwt_token = request.headers['Authorization']

        try:
            identity = jwt.decode(jwt_token, 'secret')['sub']
            print(identity)
            return func(identity, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            response = jsonify({
                "message": "Your token has expired. Please log in to continue"
            })
            response.status_code = 401
            return response

        except jwt.InvalidTokenError:
            response = jsonify({
                    "message": "Invalid token. Please log in or sign up to continue"
            })
            response.status_code = 401
            return response

        return authorize
def user_identity():
    """Get a user identity from token.
    """
    auth = request.headers['Authorization']
    token = auth.lstrip('Bearer').strip(' ')
    return jwt.decode(token, 'secret')


def admin_route(my_route):
    @wraps(my_route)
    def only_admin(*args, **kwargs):
        is_admin = user_identity().get("is_admin")
        if is_admin is False:
            return jsonify({
                'error': "Forbidden! This is an Admin ONLY route, and sadly you are not Admin.",
                'status': 403
            }), 403
        return my_route(*args, **kwargs)
    return only_admin
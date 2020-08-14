# flask_token_auth_blueprint

## A re-usable flask blueprint for jwt token authorization
This blueprint adds an endpoint for Registration and Login. It also exports a `login_required` decorator that authenticates routes and populates flask's `g` object with the current user payload.


## Installation
1. Download files to your local directory
2. Add as git submodule.
     Run ```git add submodule git@github.com:dogoyaro/flask_token_auth_blueprint.git <preferred-path>```


## Usage
#### Pre-requisites: 

For this to work, you need:
*important* this routes accept json data

1. An auth class that implements `create_user`, `authenticate` and `get_token_payload` static methods.
2. Add the authentication class the `USER_MODEL` config object
3. [POST] `/token-register` is used for sign ups and returns a jwt token.
4. [POST] `/token-login` is used for login and also returns a jwt token.



```
from flask import Flask

`./models.py`

class User:
  @staticmethod
  def create_user(user):
    # creates user
    return user

  @staticmethod
  def authenticate(user_details):
    # authenticates user using the data passed in the request
    return user_details

  @staticmethod
  def get_token_payload(user):
    # returns the payload to store in the token
      return { 'id': user['id'] }


`./__init__.py`

def create_app():
  app = Flask(__name__)
  app.config['USER_MODEL'] = User

  # token_auth being the module holding the blueprint
  from .token_auth import auth_blueprint as token_auth_blueprint
  app.register_blueprint(token_auth_blueprint)

  return app


`./api.py`
from .token_auth import login_required
@app.route('/')
@login_required
def index():
  return 'an authenticated route'

```



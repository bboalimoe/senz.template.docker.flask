from flask import Flask
import rollbar
import os
import rollbar.contrib.flask

ACCESS_TOKEN = "ca7f0172c3d44f54a17c75367116bd2a"
ENVIRONMENT = "production"
rollbar.init(ACCESS_TOKEN,ENVIRONMENT)
app = Flask(__name__)

from flask import got_request_exception


@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(

        ACCESS_TOKEN,
        # environment name
        ENVIRONMENT,
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


@app.route('/')
def hello_world():

#try: if catch the exception.
    raise Exception("what is the fukc");
#except:
    print "there is an exception!"

    return 'Hello World!'


if __name__ == '__main__':
    #report one message
    rollbar.report_message("get one message","error");

    app.run(port=9001)

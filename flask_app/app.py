import rollbar
import os
import rollbar.contrib.flask
from flask import jsonify
#####new relic demo
####
#### Reference:
#### https://docs.newrelic.com/docs/agents/python-agent/getting-started/python-agent-quick-start
#
# import newrelic.agent
cur_path = os.path.abspath(".")
#newrelic.agent.initialize(cur_path + "/newrelic.ini","staging")



from flask import Flask

app = Flask(__name__)

##### rollbar demo
##### Reference
##### https://rollbar.com/docs/notifier/pyrollbar/

# ACCESS_TOKEN = "ca7f0172c3d44f54a17c75367116bd2a"
# ENVIRONMENT = "production"
# rollbar.init(ACCESS_TOKEN,ENVIRONMENT)
# from flask import got_request_exception
#
#
# @app.before_first_request
# def init_rollbar():
#     """init rollbar module"""
#     rollbar.init(
#
#         ACCESS_TOKEN,
#         # environment name
#         ENVIRONMENT,
#         # server root directory, makes tracebacks prettier
#         root=os.path.dirname(os.path.realpath(__file__)),
#         # flask already sets up logging
#         allow_logging_basic_config=False)
#
#     # send exceptions from `app` to rollbar, using flask's signal system.
#     got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


@app.route("/json/")
def json_response():

    return jsonify(success=True,args={"code":1,"status":"OK"})



@app.route('/')
def hello_world():

    return 'Hello World!'



@app.route("/roll_exception/")
def rollbar_exception():

#try:
    raise Exception("what is the fukc");
#except:
    print "there is an exception!"
    return "rollbar test"

if __name__ == '__main__':
    #report one message
    #rollbar.report_message("get one message","error");
    app.debug = True;
    app.run(port=9001)

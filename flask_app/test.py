from flask.ext.testing import TestCase
from flask.ext.testing import LiveServerTestCase
from app import app as FlaskApp
from flask import Flask
import urllib2

# to conduct the tests,
# first install nose: pip install nose
# just cd to the dir containing the test.py,and run command "nosetests"

class IsLiveTest(LiveServerTestCase):

    def create_app(self):

        FlaskApp.config["TESTING"] = True
        FlaskApp.config["LIVESERVER_PORT"] = 8943
        #return FlaskApp
        return FlaskApp

    def test_server_is_up_and_running(self):

        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code,200)




class JsonAndOtherTest(TestCase):

    def create_app(self):

        FlaskApp.config["TESTING"] = True
        FlaskApp.config["LIVESERVER_PORT"] = 8943
        #return FlaskApp
        return FlaskApp


    def test_json_get(self):
        response = self.client.get("/json_get/")
        print response.json
        self.assertEqual(
            response.json,
            dict(
                success=True,
                args={"code":1,"status":"OK"}
                )
        )

    def test_json_post(self):
        params = {"a":"b"}
        from flask import jsonify
        from flask import json
        json_str = json.dumps(params)
        response = self.client.post("/json_post/",data = json_str)
        self.assertEqual(response.json,dict(
            post_params=params,
            success=True
        )
        )


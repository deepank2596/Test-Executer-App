from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
#from flaskwebgui import FlaskUI

from test_executer.utils.DriverManager import getDriver
from test_executer.config import BOOTSTRAP_CLASSNAME
from time import sleep
import json
#from test_executer.config import TEST_FILE_PATH

def get_class( kls ):
    parts = kls.split('.')
    module = ".".join(parts[:-1])
    print(module)
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)            
    return m

def read_Testfile(test_filePath):
    with open(test_filePath,"r") as test_file:
        testCases = json.loads(test_file.read())
        return testCases

def run_test(test):
    driver= getDriver()
    login_page= get_class(BOOTSTRAP_CLASSNAME)(driver)    #LP(driver)
    print(test['name'])
    print("Total Steps: {}".format(len(test["steps"])))
    for step in test['steps']:
        if step.get("args") is not None:
            getattr(login_page,step["action"])(**step["args"])
        else:
            getattr(login_page,step["action"])()


def execute_tests(testCases):
    #testCases=read_Testfile(test_filePath)
    for test in testCases:
        if test.get("execute").lower() == "yes":
            run_test(test)

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#ui= FlaskUI(app,port=8000,browser_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

parser=reqparse.RequestParser()
parser.add_argument('filepath')
parser.add_argument('test_cases')

class GetTestCases(Resource): 
    def post(self): 
        args=parser.parse_args()
        print("#"*10)
        testCases=read_Testfile(args.get('filepath',''))
        return testCases

class ExecuteTests(Resource): 
    def post(self): 
        args=parser.parse_args()
        print("#"*10)
        print(args.get('test_cases',''))
        execute_tests(json.loads(args.get('test_cases','')))
        return jsonify({'message': "all tests completed successfully"}) 

api.add_resource(GetTestCases, '/api/getTestCases')
api.add_resource(ExecuteTests, '/api/execute')

if __name__ == '__main__':
   #ui.run() 
   app.run(debug=True,port=8000)
                


import traceback
from flask import Flask,request, jsonify,json
import sys
from flask import Response
import json

#Flask instance
app = Flask('stocker')

#region
#adding header to allow access for websites
@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "X-Requested-With,content-type, authorization"
    return response

@app.route('/python-api/analyser',methods=['POST'])
def ai_analysis():
    '''
    input to the API: {"input-text":"hello"}
    output from the API: {"input-text":"hello"}
    '''
    try:
        json_input = request.json
        input_string = json_input['input-text']
        # You can call any function here and use the input passed to the API as params to the function and then respond with the function result
        output_string = reverse_string(input_string)

        return json.dumps({"output-text":output_string})
    except:
        return jsonify({'trace': traceback.format_exc()})


def reverse_string(text):
  return text[::-1]

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # This is for a command-line input
    except:
        port = 8889
    app.run(port=port,host="localhost")

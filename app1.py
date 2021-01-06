from flask import Flask, render_template,request
import json
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/equation', methods=['GET','POST'])
def equation():
   response = {}
   jsonData = request.get_json()
   print(jsonData)

   denoted_data = jsonData['denoted']
   power_data = jsonData['power']
   if None not in denoted_data and None not in power_data and len(denoted_data) > 0 and len(power_data) > 0 :
      response['message'] = 'Successfully Added.'
      response['code'] = 200
   else:
      response['message'] = 'Error, Please make sure to fill all field.'
      response['code'] = 400
      
   res = json.dumps(response)
   return res

    
if __name__ == '__main__':
   app.run(debug = True)

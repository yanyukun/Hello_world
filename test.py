
from flask import Flask, request, Response


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/json',methods=['GET','POST'])
def my_json():
    #r = request.files['file']
    #ipdb.set_trace()
    ret = request.form['title']
    print(ret)
    return ret


if __name__ == '__main__':
    app.run(debug=True)


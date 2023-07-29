from flask import Flask, jsonify, render_template, request
import scraping
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/find-info/', methods=['GET'])
def get_info():
  print ('I got clicked!')
  search_param = request.args.get('request')
  print(search_param)
  search_param = search_param.replace("+", ' ')

  return jsonify(scraping.scrapeData(search_param))

if __name__ == '__main__':
  app.run(debug=True)
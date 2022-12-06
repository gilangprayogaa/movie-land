from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

api_key = "YOUR_API_KEY"
baseurl = "https://api.themoviedb.org/3/movie/popular/?api_key="+api_key
tvurl = "https://api.themoviedb.org/3/tv/popular?api_key="+api_key

@app.route('/index')
def index():
    req = requests.get(baseurl)
    json_data = json.loads(req.content)
    
    return render_template("index.html", data=json_data["results"])

@app.route('/result', methods=['GET', 'POST'])
def movie():
    search_name = request.form['search_name']
    search_url = "https://api.themoviedb.org/3/search/movie/?api_key={}&query={}".format(api_key, search_name)
    search_response = requests.get(search_url).json()
    
    tv_name = request.form['search_name']
    searchtv_url = "https://api.themoviedb.org/3/search/tv/?api_key={}&query={}".format(api_key, tv_name)
    searchtv_response = requests.get(searchtv_url).json()
    
    return render_template("result.html", datas = search_response["results"], search_name=search_name,
                           tvs = searchtv_response["results"])

@app.route('/tv_show')
def tv_show():
    req = requests.get(tvurl)
    jsondata = json.loads(req.content)

    return render_template("tv_show.html", data=jsondata["results"])

if __name__ == "__main__":
    app.run(debug=True)
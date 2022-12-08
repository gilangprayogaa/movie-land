from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

api_key = "50608f765499e5417950395204296c05"
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

@app.route('/detail_m/<title>')
def detail_m(title):
    detail_url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(title, api_key)
    detail_response = requests.get(detail_url).json()
    
    credits_url = "https://api.themoviedb.org/3/movie/{}/credits?api_key={}".format(title, api_key)
    credits_response = requests.get(credits_url).json()
        
    return render_template('detail.html', data_detail=detail_response, data_credits=credits_response["cast"])

@app.route('/detail_t/<name>')
def detail_t(name):
    details_url = "https://api.themoviedb.org/3/tv/{}?api_key={}".format(name, api_key)
    details_response = requests.get(details_url).json()
    
    credits_tv_url = "https://api.themoviedb.org/3/tv/{}/credits?api_key={}".format(name, api_key)
    credits_tv_response = requests.get(credits_tv_url).json()    
    
    return render_template('detail_tv.html', data_details=details_response, credits_tv=credits_tv_response["cast"])

if __name__ == "__main__":
    app.run(debug=True)

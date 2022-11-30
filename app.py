from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

api_key = "YOUR_API_KEY"
baseurl = "https://api.themoviedb.org/3/movie/popular/?api_key="+api_key

@app.route('/')
def index():
    req = requests.get(baseurl)
    json_data = json.loads(req.content)
    
    return render_template("index.html", data=json_data["results"])

@app.route('/movie_result', methods=['GET', 'POST'])
def search_movie():
    movie_name = request.form['movie_name']
    search_url = "https://api.themoviedb.org/3/search/movie/?api_key={}&query={}".format(api_key, movie_name)
    search_response = requests.get(search_url).json()
    
    return render_template("movie_result.html", datas = search_response["results"], movie_name=movie_name)

if __name__ == "__main__":
    app.run(debug=True)
from application import app

#application = Flask(__name__, template_folder='/opt/basic_movie_db/templates')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 

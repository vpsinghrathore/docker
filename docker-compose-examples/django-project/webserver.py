import flask
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/connectdb', methods=['GET'])
def connectdb():
    conn = None
    conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.exeucte('Select version()')
    version = cur.fetchone()
    cur.close()
    if conn != None:
            return "<h1>Great! I am running using docker compose setup! As i can connect to Postgres DB with version: " + version + "</h1>"
    else:
            return "<h1>Sorry! Your docker compose setup is not working as unable to connect to DB!</h1>"

@app.route('/', methods=['GET'])
def home():
    return "<h1>Great!HAPPY API Programming !</h1>"

@app.route('/get-apis', methods=['GET'])
def getapis():
    return "<h1>/connectdb - Only single API supported</h1>"

# Start Program on on localhost on port 80
app.run(port=80)

import flask
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/connectdb', methods=['GET'])
def home():
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

@app.route('/vptesting', methods=['GET'])
def vptesting():
    return "<h1>Great! I am access my own URI</h1>"

# Start Program on on localhost on port 8000
app.run(host='0.0.0.0', port=8000)

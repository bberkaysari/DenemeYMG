from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="db",
        database="testdb",
        user="postgres",
        password="123456"
    )

@app.route('/')
def index():
    return render_template_string(open("static/index.html").read())

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    cur.close()
    conn.close()
    return f"Merhaba, {name}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
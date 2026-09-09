from flask import Flask, render_template
import psycopg2
import os
DBURL = os.getenv("DATABASE_URL")

app = Flask(__name__)


@app.route("/")
def home():
    conn = psycopg2.connect(DBURL)
    # Create cursor
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students;")
    rows = cursor.fetchone()
    cursor.close()
    conn.close()


    return render_template("index.html",data=rows)



if __name__ == "__main__":
    app.run(debug=True)


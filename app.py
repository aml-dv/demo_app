from flask import Flask, render_template
import psycopg2
DBURL="postgresql://demo_db_06rw_user:icEAsFoU1KaAbYCOy9lFJCE1zd7rt0gc@dpg-daghj1942hec73ccp3hg-a/demo_db_06rw"
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


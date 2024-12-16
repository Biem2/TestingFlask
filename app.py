from flask import Flask, render_template, request

app = Flask(__name__)

# Halaman utama dengan metode GET
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Halaman untuk menerima data dengan metode POST
@app.route('/submit', methods=['POST'])
def submit():
    # Mengambil data dari form
    name = request.form['name']
    email = request.form['email']
    
    return f"Nama: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)

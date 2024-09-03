from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    # Run optimization logic here
    return {"result": "Optimization successful!"}

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
from your_simulation_module import run_simulation

app = Flask(__name__)

@app.route('/')
def home():
    result = run_simulation()  # Adjust this to your actual simulation function
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Portfolio Flask server running at http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)

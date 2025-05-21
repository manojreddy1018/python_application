from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Application deployed successfully'

if __name__ == '__main__':
    # Run the app on Unix/Linux systems, listening on all interfaces
    app.run(host='0.0.0.0', port=5000)


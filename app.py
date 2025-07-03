from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db
from routes import api_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)
app.register_blueprint(api_bp)
@app.route('/')
def health_check():
    return jsonify({"status": "API está funcionando!"})

if __name__ == '__main__':
    with app.app_context():

        pass
    app.run(debug=True, host='0.0.0.0', port=5000)

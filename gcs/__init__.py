
from flask import Flask, jsonify


def gcs_app(config=None):
    app = Flask(__name__)
    app.config.from_prefixed_env()
    app.bucket_name = app.config.get('BUCKET_NAME', 'local')

    from .gcs_routes import gcs_bp  # Assuming your blueprint is named `game_bp`
    app.register_blueprint(gcs_bp)

    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({'status': 'ok'})

    return app

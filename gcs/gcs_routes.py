from flask import Blueprint, jsonify, request, current_app
from .gcs import Bucket


gcs_bp = Blueprint('game_bp', __name__)

# MYBUCKET = 'my-bucket-name'


@gcs_bp.route('/write', methods=['POST'])
def write():
    filename = request.json['filename']
    content = request.json['content']
    current_app.logger.info(f"Writing in bucket{current_app.bucket_name} file {filename} with content {content}")
    mybucket = Bucket(current_app.bucket_name)
    mybucket.write(filename, content)
    return jsonify({'status': 'ok'})


@gcs_bp.route('/read/<filename>')
def read(filename):
    mybucket = Bucket(current_app.bucket_name)
    current_app.logger.info(f"Reading file {filename}")
    return jsonify({'status': 'ok', 'content': mybucket.read(filename)})

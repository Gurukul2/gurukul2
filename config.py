import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'b9fcd3a2e4f5a6b7c8d9e0f1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1'
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB limit for uploaded files
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

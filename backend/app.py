from flask import Flask
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.chat_routes import chat_bp
from routes.admin_routes import admin_bp

app = Flask(__name__,
template_folder="../frontend/templates",
static_folder="../frontend/static")

app.secret_key="skillplatformsecret"

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
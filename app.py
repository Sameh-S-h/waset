from flask import Flask, render_template, session
from core.db_singleton import DatabaseConnection
from repositories.repository_factory import RepositoryFactory
from controllers.auth_controller import auth_bp
from controllers.listing_controller import listing_bp
from controllers.user_controller import user_bp

app = Flask(__name__)
app.secret_key = 'waset_secret_key_123'

app.register_blueprint(auth_bp)
app.register_blueprint(listing_bp)
app.register_blueprint(user_bp)

@app.route("/")
def home():
    listing_repo = RepositoryFactory.get_repository("listing")
    listings = listing_repo.get_all_listings()
    return render_template('index.html', listings=listings)

if __name__ == "__main__":
    db = DatabaseConnection()
    app.run(debug=True)




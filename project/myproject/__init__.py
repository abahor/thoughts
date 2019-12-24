from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy

# ----- initialization of app
app = Flask(__name__)

# ----- initialization of db --- migrate
db = SQLAlchemy(app)
Migrate(app, db)

# -------- configuration for db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codeXz:hpprobook450g3*@127.0.0.1/thoughts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'


# ------- dos attack protection
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10000 per day", "300 per hour"]
)

# ----- Mail ----
app.config.update(
    debug=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='jousefgamal46@gmail.com',
    MAIL_PASSWORD='jousefgamal123456789'
)
mail = Mail(app)

# ---------------- LOGIN
login = LoginManager()
login.init_app(app)
login.login_view = 'users.login'

from myproject.users.users import users
app.register_blueprint(users)

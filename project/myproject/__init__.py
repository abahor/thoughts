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
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codeXz:hpprobook450g3*@127.0.0.1/thoughts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
=======
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://codeXz:hpprobook450g3*@127.0.0.1/social'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
>>>>>>> fb76cf676707eecdc4d497e125ad225af6850874
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
<<<<<<< HEAD

from myproject.users.users import users
=======
login.refresh_view = "users.change"
from myproject.messages.messages import messages
from myproject.users.users import users


app.register_blueprint(messages)
>>>>>>> fb76cf676707eecdc4d497e125ad225af6850874
app.register_blueprint(users)

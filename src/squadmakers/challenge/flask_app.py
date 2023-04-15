from squadmakers.challenge import __version__
from squadmakers.challenge.config import config
from squadmakers.challenge.db.sqlalchemy import Session
from squadmakers.challenge.utils.web.flask.app.app_factory import AppFactory

app_factory = AppFactory(__version__, Session)
app = app_factory.make_flask(config)

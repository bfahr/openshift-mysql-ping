import os
from flask import Flask
from pymysql import connect
from pymysql.cursors import DictCursor

application = Flask(__name__)


def db_conf():
    opts = dict()
    opts['user'] = os.environ.get('DB_USER')
    opts['password'] = os.environ.get('DB_PASSWORD')
    opts['database'] = os.environ.get('DB_NAME')
    opts['port'] = int(os.environ.get('DB_PORT', '3306'))
    return opts


@application.route('/')
def root():
    return("Hello there")


@application.route('/ping/<host>')
def ping(host):
    opts = db_conf()
    opts['host'] = host
    db = connect(**opts)
    try:
        db.ping()
        db.close()
        return("Ping to {} was successful".format(host))
    except Exception as e:
        return("Ping to {} failed with error<br/><pre>{}</pre>".format(host, e))


if __name__ == "__main__":
    application.run()

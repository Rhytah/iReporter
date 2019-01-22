from flask import Flask
from reporter_api import app

from database.server import DatabaseConnect




if __name__ == '__main__':
    app.run(debug=True, port =5000)
    db = DatabaseConnect()
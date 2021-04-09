from application import db


# drop and then create tables from scratch. All previous data is wiped, so this file should be run only to setup or restart the entire system
db.drop_all()
db.create_all()
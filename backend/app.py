from application import app, db
from os import getenv

if __name__ == "__main__":
    if getenv("CREATE_SCHEMA") is not None:
        if getenv("CREATE_SCHEMA").lower() == "true":
            print("Creating table schema")
            db.drop_all()
            db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
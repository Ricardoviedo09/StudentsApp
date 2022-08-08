from flask import request, jsonify
from config.connection import app, db, student_schema, students_schema
import routes.Students as students


@app.route('/')
def index():
    return jsonify({'Message': 'Welcome to api'})


if __name__ == '__main__':
    app.run(debug=True)

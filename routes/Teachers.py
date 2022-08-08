from flask import request, jsonify
from config.connection import app, db, teacher_schema, teachers_schema
from models.Teachers import Teachers


@app.route('/teachers', methods=['POST'])
def create_teacher():
    try:
        name = request.json['name']
        lastname = request.json['lastname']
        course = request.json['course']

        new_teacher = Teachers(name, lastname, course)

        db.session.add(new_teacher)
        db.session.commit()

        return teacher_schema.jsonify(new_teacher)

    except Exception:
        return jsonify({'ERROR': 'No data Found'})


@app.route('/teachers', methods=['GET'])
def get_all_teachers():
    all_teachers = Teachers.query.all()
    result = teachers_schema.dump(all_teachers)

    return jsonify(Students=result)

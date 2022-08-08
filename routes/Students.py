from flask import request, jsonify
from config.connection import app, db, student_schema, students_schema
from models.Students import Students


@app.route('/students', methods=['POST'])
def create_student():
    try:
        name = request.json['name']
        lastname = request.json['lastname']

        new_student = Students(name, lastname)

        db.session.add(new_student)
        db.session.commit()

        return student_schema.jsonify(new_student)

    except Exception:
        return jsonify({'ERROR': 'No data Found'})


@app.route('/students', methods=['GET'])
def get_all_students():
    all_students = Students.query.all()
    result = students_schema.dump(all_students)

    return jsonify(Students=result)

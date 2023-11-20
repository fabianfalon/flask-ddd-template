from flask import Blueprint, request
from src.app.controllers.course_finder import CourseFinderController
from src.app.controllers.course_creator import CreateCourseController
from src.app.controllers.course_list import GetCourseController
from src.contexts.courses.infrastructure.serializers import CourseSchema

blueprint = Blueprint("course", __name__)


@blueprint.route("/courses", methods=("POST", "GET"))
def create():
    if request.method == "POST":
        course = CreateCourseController().execute(request)
        return CourseSchema().dump(course), 200
    else:
        courses = GetCourseController().execute()
        data = CourseSchema(many=True).dump(list(courses))
        return {"data": data}, 20


@blueprint.route("/courses/<title>", methods=("GET",))
def course_finder(title):
    if request.method == "GET":
        payload = []
        courses = CourseFinderController().execute(request)
        if not courses:
            title = request.json.get("title")
            return {"error": f"course: {title} not found"}, 404
        for course in courses:
            payload.append({"id": course.id, "title": course.title, "duration": course.duration})

        return payload, 20

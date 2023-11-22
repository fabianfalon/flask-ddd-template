from flask import Blueprint, request

from src.app.controllers.course_creator import CreateCourseController
from src.app.controllers.course_finder import CourseFinderController
from src.app.controllers.course_list import GetCourseController
from src.app.controllers.review_creator import CreateReviewController
from src.contexts.courses.infrastructure.serializers import CourseSchema
from src.contexts.reviews.infrastructure.marshaller.serializers import ReviewSchema

blueprint = Blueprint("course", __name__)


@blueprint.route("/courses", methods=("POST", "GET"))
def create():
    if request.method == "POST":
        course = CreateCourseController().execute(request)
        return CourseSchema().dump(course), 200
    courses = GetCourseController().execute()

    data = CourseSchema(many=True).dump(list(courses))
    return {"data": data}, 200


@blueprint.route("/courses/<title>", methods=("GET",))
def course_finder(title):
    if request.method == "GET":
        course = CourseFinderController().execute(request)
        if not course:
            title = request.json.get("title")
            return {"error": f"course: {title} not found"}, 404
        return CourseSchema().dump(course), 200


@blueprint.route("/courses/<course_id>/review", methods=("GET", "POST"))
def course_review_creator(course_id):
    if request.method == "POST":
        review = CreateReviewController().execute(request, course_id)
        return ReviewSchema().dump(review), 200

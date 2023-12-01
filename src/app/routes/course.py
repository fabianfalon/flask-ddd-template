import sys

from dependency_injector.wiring import inject, Provide
from flask import Blueprint, request

from src.app.controllers.courses.course_creator import CreateCourseController
from src.app.injections.containers import Containers, containers_app
from src.app.controllers.courses.course_finder import CourseFinderController
from src.app.controllers.courses.course_list import GetCourseController
from src.app.controllers.reviews.review_creator import CreateReviewController
from src.app.controllers.reviews.review_list_by_course import ListReviewByCourseController
from src.contexts.courses.infrastructure.serializers import CourseSchema
from src.contexts.reviews.infrastructure.marshaller.serializers import ReviewSchema

blueprint = Blueprint("course", __name__)


@blueprint.route("/courses", methods=("POST", "GET"))
@inject
def create(
    controller=Provide[Containers.course_creator_controller],
):
    if request.method == "POST":
        course = controller.execute(request)
        return CourseSchema().dump(course), 200
    courses = GetCourseController().execute()

    data = CourseSchema(many=True).dump(list(courses))
    return {"data": data}, 200


@blueprint.route("/courses/<course_id>", methods=("GET",))
def course_finder(course_id):
    if request.method == "GET":
        course = CourseFinderController().execute(course_id)
        if not course:
            title = request.json.get("title")
            return {"error": f"course: {title} not found"}, 404
        return CourseSchema().dump(course), 200


@blueprint.route("/courses/<course_id>/review", methods=("GET", "POST"))
@inject
def course_review_creator(
    course_id,
    review_list_controller=Provide[Containers.review_list_controller],
    create_review_controller=Provide[Containers.create_review_controller],
):
    if request.method == "POST":
        review = create_review_controller.execute(request, course_id)
        return ReviewSchema().dump(review), 200

    reviews = review_list_controller.execute(course_id)
    data = ReviewSchema(many=True).dump(reviews)
    return {"data": data}, 200


containers_app.wire(modules=[sys.modules[__name__]])

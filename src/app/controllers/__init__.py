import importlib

from src.app.injections.containers import containers_app

course_creator = importlib.import_module("src.app.controllers.courses.course_creator")
course_list = importlib.import_module("src.app.controllers.courses.course_list")

review_creator = importlib.import_module("src.app.controllers.reviews.review_creator")
review_list = importlib.import_module("src.app.controllers.reviews.review_list_by_course")

containers_app.wire(
    modules=[
        course_creator,
        course_list,
        review_creator,
        review_list
    ]
)

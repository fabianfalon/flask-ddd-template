from dependency_injector import containers, providers

from src.app.controllers.courses.course_creator import CreateCourseController
from src.app.controllers.reviews.review_list_by_course import ListReviewByCourseController

from src.contexts.courses.infrastructure.storage.mongo import MongoRepository as CourseMongoRepository
from src.contexts.shared.infrastructure.eventbus.in_memory_event_bus import InMemoryEventBus

from src.contexts.reviews.infrastructure.storage.mongo import MongoRepository as ReviewMongoRepository


class Containers(containers.DeclarativeContainer):

    course_repository = providers.Singleton(CourseMongoRepository)
    event_bus = providers.Singleton(InMemoryEventBus)
    course_creator_controller = providers.Singleton(
        CreateCourseController, repository=course_repository, event_bus=event_bus
    )

    review_repository = providers.Singleton(ReviewMongoRepository)
    review_list_controller = providers.Singleton(ListReviewByCourseController, review_repository)

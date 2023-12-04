from dependency_injector import containers, providers

from src.contexts.courses.application.create.course_creator import CourseCreator
from src.contexts.courses.application.create.course_get_all import CourseGetAll
from src.contexts.courses.domain.course_finder import CourseFinder

from src.contexts.courses.infrastructure.storage.mongo import MongoRepository as CourseMongoRepository
from src.contexts.reviews.application.create.review_creator import ReviewCreator
from src.contexts.reviews.application.find.review_get_all import ReviewGetAllByCourse
from src.contexts.shared.infrastructure.eventbus.in_memory_event_bus import InMemoryEventBus

from src.contexts.reviews.infrastructure.storage.mongo import MongoRepository as ReviewMongoRepository


class Containers(containers.DeclarativeContainer):
    course_repository = providers.Singleton(CourseMongoRepository)
    event_bus = providers.Singleton(InMemoryEventBus)

    course_creator = providers.Singleton(
        CourseCreator, course_repository, event_bus
    )

    course_get_all = providers.Singleton(
        CourseGetAll, course_repository
    )
    #### reviews containers
    review_repository = providers.Singleton(ReviewMongoRepository)
    finder = providers.Singleton(CourseFinder, course_repository)

    review_creator = providers.Singleton(
        ReviewCreator, review_repository, finder
    )

    review_get_all_by_course = providers.Singleton(
        ReviewGetAllByCourse, review_repository
    )


# containers_app: Containers = Containers()

from post.models import Post, Person


class PostParser:

    def __init__(self, fields: dict) -> None:
        self._fields = fields

    def parse(self):
        for element in self._fields:
            person_id = element.pop("userId", None)
            person = self.get_person(person_id)
            if person is None:
                raise TypeError("Person not found")

            id_ = int(element.pop("id"))
            post = Post.get_instance_by_id(id_)
            post.person = person
            post.insert_fields(element)

    def get_person(self, id_):
        try:
            return Person.objects.get(id=id_)
        except Person.DoesNotExist:
            return None

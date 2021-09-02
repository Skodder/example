from django.core.management.base import BaseCommand, CommandError
from post.models import Person, Company, Addres
from post.utils import PersonParser, PostParser
import urllib.request, json 
 
    
class Command(BaseCommand):
    help = "Запустить парсер json'ов"

    def handle(self, *args, **options):

        persons_json = self.get_json("http://jsonplaceholder.typicode.com/users")
        person_parser = PersonParser(persons_json)
        person_parser.parse()

        posts_json = self.get_json("http://jsonplaceholder.typicode.com/posts")
        post_parser = PostParser(posts_json)
        post_parser.parse()

    def get_json(self, url: str):
        """Получить json объект с переданного адреса."""
        with urllib.request.urlopen(url) as response:
            result = json.loads(response.read().decode())
        return result


from post.models import Person, Company, Addres


class PersonParser:

    def __init__(self, fields: dict) -> None:
        self._fields = fields

    def parse(self):
        for element in self._fields:
            address = element.pop("address", None)
            company = element.pop("company", None)
            id_ = int(element.pop("id"))
            person = Person.get_instance_by_id(id_)
            company_obj = self.get_company(company)
            address_obj = self.get_address(address)
            person.company = company_obj
            person.addres = address_obj
            person.insert_fields(element)

    def get_company(self, fields: dict) -> Company:
        result = Company()
        phrase = fields.pop("catchPhrase")
        result.catch_phrase = phrase
        result.insert_fields(fields)
        return result

    def get_address(self, fields: dict) -> Addres:
        geo_code: dict = fields.pop("geo")
        result: Addres = Addres()
        result.lat = geo_code.get("lat")
        result.lng = geo_code.get("lng")
        result.insert_fields(fields)
        return result

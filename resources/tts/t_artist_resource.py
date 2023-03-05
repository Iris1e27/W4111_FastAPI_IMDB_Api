from resources.mysql_data_service import MySQLDataService, MySQLDataServiceConfig
from resources.imdb_resources.artist_resource import ArtistResource
import json
from service_factory import ServiceFactory

service_factory = ServiceFactory()
artist_resource = service_factory.get_resource("ArtistResource")


def t1_get_by_key():

    a_resource = artist_resource
    result = a_resource.get_by_key("nm0389698")
    print("t1: result = \n", json.dumps(result.dict(), indent=2))


def t2_get_primaryName():

    a_resource = artist_resource
    result = a_resource.get(primaryName='Sophie Turner')
    print("t2: result = \n", json.dumps(result.dict(), indent=2))

def t3_get_birthYear():

    a_resource = artist_resource
    result = a_resource.get(birthYear='1990')
    print("t3: result = \n", json.dumps(result.dict(), indent=2))

def t4_delete_primaryName():

    a_resource = artist_resource
    result = a_resource.delete(primaryName='David Rintoul')
    print("t4: result = \n", result)

def t5_update_primaryName():

    a_resource = artist_resource
    a_row = {
        "nconst": "nm0727778",
        "primaryName": "David Rintoul",
        "birthYear": "1988",
        "deathYear": "1999"
    }
    result = a_resource.update(primaryName='David Rintoul', newValues=a_row)
    print("t5: result = \n", result)

def t6_post():

    a_resource = artist_resource
    a_row = {
        "nconst": "nm0727778",
        "primaryName": "David Rintoul",
        "birthYear": "1948",
        "deathYear": "1977"
      }
    result = a_resource.post(a_row)
    print("t6: result = \n", a_row["nconst"])



if __name__ == "__main__":
    t1_get_by_key()
    # t2_get_primaryName()
    # t3_get_birthYear()
    # t4_delete_primaryName()
    # t5_update_primaryName()
    # t6_post()
from dojos_and_ninjas_app.config.pymysqlconnection import connectToMySQL
from dojos_and_ninjas_app.models.dojos_model import Dojos

class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        

    @classmethod
    def get_with_dojos(cls, id):
        
        data = {
            'id' : id
        }
        
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        # result = results[0]        
        dojos = []
        
        for dojo in results:
            ninja = cls(dojo)
            dojo_data = {
                **dojo,
                'id' : dojo['dojos.id'],
                'created_at' : dojo['dojos.created_at'],
                'updated_at' : dojo['dojos.updated_at']
            }
            
            ninja.dojos = Dojos(dojo_data)
            dojos.append(ninja)
        return dojos


    @classmethod
    def create(cls, data):
            
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
            
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        
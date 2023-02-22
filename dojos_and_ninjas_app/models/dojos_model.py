from dojos_and_ninjas_app.config.pymysqlconnection import connectToMySQL

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    
    
    
    @classmethod
    def get_all(cls):
        
        query = "SELECT * FROM dojos"
        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
            
        return dojos
    
    @classmethod
    def get_one(cls, id):
        
        data = {
            'id' : id
        }
        query = "SELECT * FROM dojos WHERE id=%(id)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        result = results[0]
        
        return cls(result)
    
    @classmethod
    def get_one_by_name(cls, name):
        
        data = {
            'name' : name
        }
        query = "SELECT dojos.id FROM dojos WHERE name=%(name)s"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        # result = results[0]
        
        return (results)

    
    
    @classmethod
    def create(cls, data):
        
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    

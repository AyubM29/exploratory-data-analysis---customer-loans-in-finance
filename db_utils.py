from sqlalchemy import create_engine
import yaml

class RDSDatabaseConnector:

   def __init__(self, dict_credentials):
      self.dict_credentials = dict_credentials

   def db_engine(self):
       print(self.dict_credentials)

   def create_engine(self):
       
       DATABASE_TYPE = 'postgresql'
       DBAPI = 'psycopg2'
       ENDPOINT = credentials["RDS_HOST"]
       USER = credentials["RDS_USER"] 
       PASSWORD = credentials["RDS_PASSWORD"]
       PORT = credentials["RDS_PORT"]
       DATABASE = credentials["RDS_DATABASE"]
       engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")
       engine.connect()
       return create_engine
       
       


       

      
      
def load_credentials(filepath):  

    with open(filepath, mode="r") as file:
        dict_credentials = yaml.safe_load(file)
        return dict_credentials


credentials = load_credentials('credentials.yaml')
print (credentials)


my_object = RDSDatabaseConnector(credentials)
engine = my_object.create_engine()

print(engine)







        

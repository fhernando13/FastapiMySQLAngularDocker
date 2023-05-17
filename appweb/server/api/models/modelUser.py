from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.conexion import meta_data, engine


users = Table("users", meta_data, Column("id", Integer, primary_key=True),
                             Column("name", String(255)),
                             Column("lastname", String(255)),
                             Column("email", String(255)),
                             Column("age", String(3)),
                             Column("password", String(255)))

              
meta_data.create_all(engine)           
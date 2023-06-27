from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.conexion import meta_data, engine


users = Table("users", meta_data, Column("id", Integer, primary_key=True),
                             Column("name", String(255)),
                             Column("lastname", String(255)),
                             Column("phonework", String(10)),
                             Column("phonepersonal", String(10)),
                             Column("birthdate", String(8)),
                             Column("email", String(255)),
                             Column("password", String(255)))

           
meta_data.create_all(engine)           
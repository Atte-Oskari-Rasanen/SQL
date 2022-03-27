import numpy as np
import sqlalchemy
from faker import Faker
from sqlalchemy import Table, Column, Integer, String, MetaData, Date, 

class SQLData:
    def __init__(self, server:str, db:str, uid:str, pwd:str) -> None:
        self.__fake = Faker()
        self.__server = server
        self.__db = db
        self.__uid = uid
        self.__pwd = pwd
        self.__tables = dict()
    
    def connect(self) -> None:
        pass
    
    def drop_all_tables(self) -> None:
        pass
    
    def create_tables(self) -> None:
        pass
    
    def populate_tables(self) -> None:
        pass

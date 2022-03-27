class SQLData:
    #...
    def connect(self) -> None:
        self.__engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.__uid}:{self.__pwd}@{self.__server}/{self.__db}"
        )
        self.__conn = self.__engine.connect()
        self.__meta = MetaData(bind=self.__engine)

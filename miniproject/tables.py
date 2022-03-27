class SQLData:
    #...
    def create_tables(self) -> None:
        self.__tables['jobs'] = Table (
            'jobs', self.__meta,
            Column('job_id', Integer, primary_key=True, autoincrement=True, nullable=False),
            Column('Info', String(255))
        )

        self.__tables['companies'] = Table(
            'companies', self.__meta, 
            Column('company_id', Integer, primary_key=True, autoincrement=True, nullable=False),
            Column('name', String(255), nullable=False),
            Column('comment', String(255)),
            Column('address', String(255)),
        )

        self.__tables['persons'] = Table(
            'persons', self.__meta,
            Column('person_id', Integer, primary_key=True, autoincrement=True, nullable=False),
            Column('job_id', Integer, ForeignKey('jobs.job_id'), nullable=False),
            Column('company_id', Integer, ForeignKey('companies.company_id'), nullable=False),
            Column('last_name', String(255), nullable=False),
            Column('first_name', String(255)),
            Column('date_of_birth', Date),
            Column('address', String(255)),
            Column('country', String(255)),
            Column('zipcode', String(10)),
            Column('salary', Integer)
        )

        self.__meta.create_all()

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DbSetting(object):
    """"""

    DIALECT = "mysql"
    DRIVER = "mysqldb"
    USERNAME = "devsaichikawa"
    PASSWORD = "Asagakita40813011"
    HOST = "localhost"
    PORT = 3306
    DATABASE = "dev_carcass_db"
    CHARSET_TYPE = "utf8"

    DB_URL = \
        f"{ DIALECT }+{ DRIVER }://{ USERNAME }:{ PASSWORD }@{ HOST }:{ PORT }/{ DATABASE }?charset={ CHARSET_TYPE }"

    def get_db_engine(self):
        """"""
        return create_engine(self.DB_URL, echo=True)

    def dispose_db_engine(self, engine):
        """"""
        return engine.dispose()

    def get_db_session(self):
        """"""
        return scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.get_db_engine())
        )

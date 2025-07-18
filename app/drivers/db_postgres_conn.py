from os import getenv
import urllib
from database_connect import DbConnection


class PostgresDBConn(DbConnection):

    def _get_db_credentials(self, database: str) -> dict:
        return {
            "name": f'BANCO MAIN {getenv("ENVIRONMENT")}',
            "username": "admin",
            "uri": "",
            "server": getenv("ANALISE_PARECER_FINANCEIRO_DB_SERVER"),
            "database": getenv("ANALISE_PARECER_FINANCEIRO_DB_DATABASE"),
            "tipobanco": getenv("ANALISE_PARECER_FINANCEIRO_DB_TIPO_BANCO"),
            "password": urllib.parse.quote_plus(
                getenv("ANALISE_PARECER_FINANCEIRO_DB_PASSWORD")
            ),
        }

    def __exit__(self, exc_type, exc_value, traceback):
        session = getattr(self, '_local_session', None)
        if session:
            session.expunge_all()
        super().__exit__(exc_type, exc_value, traceback)
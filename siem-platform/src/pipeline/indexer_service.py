class IndexerService:
    def __init__(self, es_client, db_client):
        self.es_client = es_client
        self.db_client = db_client

    def index_log(self, log_data):
        """
        Indexe les données de log dans Elasticsearch ou PostgreSQL.
        """
        if self.es_client:
            self.index_in_elasticsearch(log_data)
        if self.db_client:
            self.index_in_postgresql(log_data)

    def index_in_elasticsearch(self, log_data):
        """
        Indexe les données de log dans Elasticsearch.
        """
        try:
            response = self.es_client.index(index='logs', body=log_data)
            return response
        except Exception as e:
            print(f"Erreur lors de l'indexation dans Elasticsearch: {e}")

    def index_in_postgresql(self, log_data):
        """
        Indexe les données de log dans PostgreSQL.
        """
        try:
            # Exemple d'insertion dans PostgreSQL
            query = "INSERT INTO logs (data) VALUES (%s)"
            self.db_client.execute(query, (log_data,))
            self.db_client.commit()
        except Exception as e:
            print(f"Erreur lors de l'indexation dans PostgreSQL: {e}")
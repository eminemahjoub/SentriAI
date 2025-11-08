class ESClient:
    def __init__(self, host='localhost', port=9200, index='logs'):
        from elasticsearch import Elasticsearch
        self.host = host
        self.port = port
        self.index = index
        self.client = Elasticsearch([{'host': self.host, 'port': self.port}])

    def index_document(self, document):
        response = self.client.index(index=self.index, body=document)
        return response

    def search(self, query):
        response = self.client.search(index=self.index, body=query)
        return response

    def delete_index(self):
        response = self.client.indices.delete(index=self.index, ignore=[400, 404])
        return response

    def create_index(self, settings=None):
        if not self.client.indices.exists(index=self.index):
            response = self.client.indices.create(index=self.index, body=settings)
            return response
        return {"error": "Index already exists."}
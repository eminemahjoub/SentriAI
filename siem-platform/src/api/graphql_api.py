from fastapi import FastAPI, HTTPException
from graphql import GraphQLSchema, GraphQLObjectType, GraphQLField, GraphQLString
from starlette.graphql import GraphQLApp

app = FastAPI()

# Define a simple GraphQL schema
query = GraphQLObjectType(
    name='Query',
    fields={
        'hello': GraphQLField(GraphQLString, resolver=lambda *_: 'Hello, world!')
    }
)

schema = GraphQLSchema(query=query)

# Add GraphQL endpoint
app.add_route("/graphql", GraphQLApp(schema=schema))

@app.get("/")
async def root():
    return {"message": "Welcome to the SIEM platform API!"}
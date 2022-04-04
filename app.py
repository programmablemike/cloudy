from api import app
from ariadne import (load_schema_from_path, make_executable_schema,
                     graphql_sync, snake_case_fallback_resolvers, MutationType, QueryType)
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from os.path import abspath
from json import load as json_load

EXAMPLES_DIRECTORY = abspath("./examples/cloudinary-api")

type_defs = load_schema_from_path('schema.graphql')
# The built-in Query and Mutator object types
# These are registered in make_executable_schema to provide custom event handlers for requests
query = QueryType()
mutation = MutationType()
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    ''' Displays the graphql playground for request testing '''
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=["POST"])
def graphql_server():
    ''' The main graphql query and mutator route '''
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


@query.field("healthy")
def resolve_healthy(*_):
    '''
    Handler for the healthy query
    Gives a naive healthcheck that on says 'OK'.
    '''
    return {
        "message": "OK"
    }


@mutation.field("uploadImage")
def resolve_upload_image(_, info: object, file: str, upload_preset: str, signature: str):
    '''
    Handler for uploadImage mutator requests
    '''
    #####
    # TODO(mlee): Replace this with a query to the Cloudinary API
    #####
    return json_load(open(EXAMPLES_DIRECTORY + "/upload_response.json"))


@mutation.field("renameImage")
def resolve_rename_image(_, info: object, from_public_id: str, to_public_id: str, signature: str):
    '''
    Handler for renameImage mutator requests
    '''
    #####
    # TODO(mlee): Replace this with a query to the Cloudinary API
    #####
    return json_load(open(EXAMPLES_DIRECTORY + "/rename_response.json"))


@mutation.field("destroyImage")
def resolve_destroy_image(_, info: object, public_id: str, signature: str):
    '''
    Handler for destroyImage mutator requests
    '''
    #####
    # TODO(mlee): Replace this with a query to the Cloudinary API
    #####
    return json_load(open(EXAMPLES_DIRECTORY + "/destroy_response.json"))

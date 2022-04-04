from ariadne import gql, load_schema_from_path
from os.path import abspath

SCHEMA_PATH = "../../schema.graphql"


def setup_graphql():
    schema_file = abspath(SCHEMA_PATH)
    schema = load_schema_from_path(schema_file)

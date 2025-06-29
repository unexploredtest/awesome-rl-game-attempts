import sys
import json

import jsonschema

SCHEMA_PATH = "src/attempts-schema.json"
DATA_PATH = "src/attempts.json"

def is_json_valid(data_path, schema_path):
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)

    with open(data_path) as data_file:
        data = json.load(data_file)

    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print("JSON data is invalid:", e.message)
        return False


if __name__ == "__main__":
    if(is_json_valid(DATA_PATH, SCHEMA_PATH)):
        print("No issues where found.")
        sys.exit(0)
    else:
        sys.exit(1)

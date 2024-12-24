import argparse

import orjson

# TODO: Command line tool, load data from json files into mongodb
# TODO: Command line tool, load data from mongodb into json files


def load_db():
    pass


def save_db():
    pass


def init_db():
    # Load the data
    with open("data/base/slot_type.json", "r") as file:
        data = orjson.loads(file.read())
        # TODO: Load the data into the database

    with open("data/base/resource_type.json", "r") as file:
        data = orjson.loads(file.read())
        # TODO: Load the data into the database

    with open("data/base/process_unit_type.json", "r") as file:
        data = orjson.loads(file.read())
        # TODO: Load the data into the database


def main():
    # Set up three commands: load, save, and init
    parser = argparse.ArgumentParser(description="Load, save, and initialize data in DynamoDB")
    subparsers = parser.add_subparsers(dest="command")

    # Load command
    subparsers.add_parser("load")
    subparsers.add_parser("save")
    subparsers.add_parser("init")

    args = parser.parse_args()

    match args.command:
        case "load":
            load_db()
        case "save":
            save_db()
        case "init":
            init_db()


if __name__ == "__main__":
    main()

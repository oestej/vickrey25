import boto3
from boto3.dynamodb.types import TypeDeserializer

from vickrey25.models.slot_type import SlotTypeRegistry
from vickrey25.models.resource_type import ResourceTypeRegistry
from vickrey25.models.process_unit_type import ProcessUnitTypeRegistry
SLOT_TYPE = SlotTypeRegistry()
RESOURCE_TYPE = ResourceTypeRegistry()
PROCESS_UNIT_TYPE = ProcessUnitTypeRegistry()


def _load_table(table_name: str):
    session = boto3.Session()
    client = session.client("dynamodb")

    paginator = client.get_paginator('scan')
    response_iterator = paginator.paginate(
        TableName=table_name
    )

    data = []
    for page in response_iterator:
        for item in page['Items']:
            # convert to python types
            deserializer = TypeDeserializer()
            python_data = {k: deserializer.deserialize(v) for k, v in item.items()}

            # append to list
            data.append(python_data['data'])

    return data


def init(table_names: dict[str, str]):
    SLOT_TYPE.load(data=_load_table(table_names["slot_type"]))
    RESOURCE_TYPE.load(data=_load_table(table_names["resource_type"]), slot_types=SLOT_TYPE)
    PROCESS_UNIT_TYPE.load(data=_load_table(table_names["process_unit_type"]), resource_types=RESOURCE_TYPE)

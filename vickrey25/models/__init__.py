from vickrey25.models.slot_type import SlotTypeRegistry
from vickrey25.models.resource_type import ResourceTypeRegistry

SLOT_TYPE = SlotTypeRegistry()
RESOURCE_TYPE = ResourceTypeRegistry()


def init():
    SLOT_TYPE.load()
    RESOURCE_TYPE.load(slot_types=SLOT_TYPE)

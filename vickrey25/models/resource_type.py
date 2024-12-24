from enum import Enum
from pydantic.dataclasses import dataclass
from vickrey25.models.slot_type import SlotType, SlotTypeRegistry


# TODO This needs a refactor

class ResourceClass(str, Enum):
    NONSTORABLE = "nonstorable"
    SOLID = "solid"
    SOLID_PERISHABLE = "solid_perishable"


@dataclass
class ResourceType:
    resource_type_id: str
    resource_type_name: str
    unit_name: str
    allowed_slot_types: list[SlotType]


@dataclass
class NonstorableResourceType(ResourceType):
    pass


@dataclass
class StorableResourceType(ResourceType):
    perishable: bool = False
    decay_points: int | None = None


@dataclass
class SolidResourceType(StorableResourceType):
    unit_m3: float
    unit_kg: float


class ResourceTypeRegistry:
    def __init__(self):
        self.resource_types = {}

    def load(self, slot_types: SlotTypeRegistry):
        # TODO: Load resource types from database
        pass

    def get(self, resource_type_id: str) -> ResourceType | None:
        return self.resource_types.get(resource_type_id, None)

    def __getitem__(self, resource_type_id: str) -> ResourceType:
        return self.get(resource_type_id)

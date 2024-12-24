from enum import Enum

from pydantic.dataclasses import dataclass
from vickrey25.models.slot_type import SlotType, SlotTypeRegistry


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

    def load(self, slot_types: SlotTypeRegistry, data: list[dict]):

        for item in data:
            # Map slot type ids to slot types
            slot_types = []
            for slot_type_id in item["allowed_slot_types"]:
                slot_types.append(slot_types[slot_type_id])
            item["allowed_slot_types"] = slot_types

            match item["resource_class"]:
                case ResourceClass.NONSTORABLE:
                    resource_type = NonstorableResourceType(**item)
                case ResourceClass.SOLID:
                    resource_type = SolidResourceType(**item)
                case ResourceClass.SOLID_PERISHABLE:
                    resource_type = StorableResourceType(**item)

            self.resource_types[resource_type.resource_type_id] = resource_type

    def get(self, resource_type_id: str) -> ResourceType | None:
        return self.resource_types.get(resource_type_id, None)

    def __getitem__(self, resource_type_id: str) -> ResourceType:
        return self.get(resource_type_id)

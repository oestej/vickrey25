from enum import Enum

from pydantic.dataclasses import dataclass

from vickrey25.models.resource_type import ResourceType, ResourceTypeRegistry


@dataclass
class IOSlotType:
    resource_type: ResourceType
    quantity: int


class EnvironmentRequirement(str, Enum):
    FLOWING_WATER_SLOT = "flowing_water_slot"


@dataclass
class EnvironmentSlotType:
    env: EnvironmentRequirement
    quantity: int


@dataclass
class ProcessUnitOption:
    inputs: list[IOSlotType | EnvironmentSlotType]
    outputs: list[IOSlotType]


@dataclass
class ProcessUnitType:
    process_unit_type_id: str
    process_unit_type_name: str
    sequence_order: int
    units_per_day: int
    process_options: list[ProcessUnitOption]


class ProcessUnitTypeRegistry:
    def __init__(self):
        self.process_unit_types = {}

    def load(self, data: list[dict], resource_types: ResourceTypeRegistry):
        for item in data:
            # TODO WIP - This is not ready yet
            process_unit_type = ProcessUnitType(**item)
            self.process_unit_types[process_unit_type.process_unit_type_id] = process_unit_type

    def get(self, process_unit_type_id: str) -> ProcessUnitType | None:
        return self.process_unit_types.get(process_unit_type_id, None)

    def __getitem__(self, process_unit_type_id: str) -> ProcessUnitType:
        return self.get(process_unit_type_id)

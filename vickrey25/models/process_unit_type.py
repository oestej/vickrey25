from dataclasses import dataclass

from vickrey25.models.resource_type import ResourceType


# Single Definition - Process Unit
@dataclass
class IOSlotType:
    resource_type: ResourceType
    quantity: int


@dataclass
class EnvironmentSlotType:
    # TODO: Defined Environmental Condition Slot Types
    pass


@dataclass
class ProcessUnitOption:
    inputs: list[IOSlotType | EnvironmentSlotType]
    outputs: list[IOSlotType]


@dataclass
class ProcessUnitType:
    process_unit_type_id: str
    process_unit_type_name: str
    sequence_order: int
    process_options: list[ProcessUnitOption]
# End Single Definition

# TODO WIP

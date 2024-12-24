from dataclasses import dataclass


@dataclass
class SlotType:
    slot_type_id: str
    slot_type_name: str
    is_storable: bool


@dataclass
class ResourceType:
    resource_type_id: str
    resource_type_name: str
    allowed_slot_types: list[SlotType]


@dataclass
class NonstorableResourceType(ResourceType):
    pass


@dataclass
class SolidResourceType(ResourceType):
    unit_m3: float
    unit_kg: float


# Single Definition - Process Unit
@dataclass
class IOSlotType:
    resource_type: ResourceType
    quantity: int


@dataclass
class ProcessUnitOption:
    inputs: list[IOSlotType]
    outputs: list[IOSlotType]


@dataclass
class ProcessUnitType:
    process_unit_type_id: str
    process_unit_type_name: str
    sequence_order: int
    process_options: list[ProcessUnitOption]
# End Single Definition

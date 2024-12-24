from dataclasses import dataclass

from vickrey25.models.process_unit_type import ProcessUnitType
from vickrey25.models.slot_type import SlotType


@dataclass
class Slot:
    slot_type: SlotType


@dataclass
class StorageSlot(Slot):
    capacity_m3: float
    capacity_kg: float


@dataclass
class ProcessUnit:
    type: ProcessUnitType
    inputs: list[Slot]
    outputs: list[Slot]

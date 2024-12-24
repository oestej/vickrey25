from dataclasses import dataclass

from vickrey25.type_def import ProcessUnitType, SlotType


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

from pydantic.dataclasses import dataclass
from pydantic import field

# Slot type is a read-only definition; not writeable during operations


@dataclass
class SlotType:
    slot_type_id: str
    slot_type_name: str
    is_storable: bool = field(default=False)


class SlotTypeRegistry:
    def __init__(self):
        self.slot_types = {}

    def load(self):
        # TODO: Load slot types from database
        pass

    def get(self, slot_type_id: str) -> SlotType | None:
        return self.slot_types.get(slot_type_id, None)

    def __getitem__(self, slot_type_id: str) -> SlotType:
        return self.get(slot_type_id)

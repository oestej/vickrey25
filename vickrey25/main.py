import nanoid

from obj_def import StorageSlot, ProcessUnit
from type_def import ProcessUnitOption, ProcessUnitType, SolidResourceType, SlotType


def main():
    bulk_storage_type = SlotType(slot_type_id=nanoid.generate(), slot_type_name="Bulk Storage", is_storable=True)
    rye_grain = SolidResourceType(
        resource_type_id=nanoid.generate(),
        resource_type_name="Rye Grain",
        unit_m3=0.001,
        unit_kg=0.001,
        allowed_slot_types=[bulk_storage_type],
    )
    wheat_grain = SolidResourceType(
        resource_type_id=nanoid.generate(),
        resource_type_name="Wheat Grain",
        unit_m3=0.001,
        unit_kg=0.001,
        allowed_slot_types=[bulk_storage_type],
    )
    rye_flour = SolidResourceType(
        resource_type_id=nanoid.generate(),
        resource_type_name="Rye Flour",
        unit_m3=0.001,
        unit_kg=0.001,
        allowed_slot_types=[bulk_storage_type],
    )
    wheat_flour = SolidResourceType(
        resource_type_id=nanoid.generate(),
        resource_type_name="Wheat Flour",
        unit_m3=0.001,
        unit_kg=0.001,
        allowed_slot_types=[bulk_storage_type],
    )
    grain_mill = ProcessUnitType(
        process_unit_type_id=nanoid.generate(),
        process_unit_type_name="Grain Mill",
        sequence_order=1,
        process_options=[
            ProcessUnitOption(inputs=[(rye_grain, 1)], outputs=[(rye_flour, 1)]),
            ProcessUnitOption(inputs=[(wheat_grain, 1)], outputs=[(wheat_flour, 1)])
        ]
    )

    input_storage = StorageSlot(
        slot_type=bulk_storage_type,
        capacity_m3=100,
        capacity_kg=100,
    )
    output_storage = StorageSlot(
        slot_type=bulk_storage_type,
        capacity_m3=100,
        capacity_kg=100,
    )

    grain_mill_process_unit = ProcessUnit(
        type=grain_mill,
        inputs=[input_storage],
        outputs=[output_storage],
    )

    # All type definitions are cachable across entire run
    # All objects are cacheable within a single sequence step

    # Running Process Units - should run in sequence order
    # TODO: To run a process unit, first total all goods available in the input storage
    # TODO: Then total all space available in the output storage by allowed slot type
    # TODO: Then go through the process options and find the first option that has enough space in the output storage and enough goods in the input storage
    # TODO: If no option is found, log why it cannot be run
    # TODO: Then update the input storage and output storage

    # Storage Purge - should run after all process units are run
    # TODO: Check if a storage slot has is_storable set to False, if so, remove the goods from the storage slot


if __name__ == "__main__":
    main()

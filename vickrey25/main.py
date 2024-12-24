from vickrey25 import models


# TODO:
# - Define a water wheel process unit [produces kinetic energy from environmental condition: flowing water]
# - Build the code to load/save to/from DynamoDB
# - Build the code to run process units

# TODO (Further)
# - Environmental Conditions - Village (population)
# - Environmental Conditions - Seasons
# - Production Unit [grouping of process units]
# - Wheat Farm [produces wheat from environmental condition, threshing process units, etc]
# - Logging [produces wood from environmental condition, sawmill milling process units, etc]
# - Quarrying [produces stone from environmental condition, stone milling process units, etc]
# - Build a production unit for each one of the above
# - Crafting [job shop style]
# - Specialist jobs [crafting, etc]


def main():
    models.init()
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
    # TODO: Decrement perishable goods by decay_points
    # TODO: If decay points are 0, remove the goods from the storage slot


if __name__ == "__main__":
    main()

from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class Fishsanity(Toggle):
    """
    Adds locations for collecting each of the 17 types of fish.
    """

    display_name = "Fishsanity"

@dataclass
class BuildJetpackOptions(PerGameCommonOptions):
    fishsanity: Fishsanity
from dataclasses import dataclass

from Options import Choice, DeathLink, OptionGroup, PerGameCommonOptions, Range, Toggle

class Fishsanity(Toggle):
    """
    Adds locations for collecting each of the 17 types of fish.
    """

    display_name = "Fishsanity"

class HarshPressure(Toggle):
    """
    Triples the oxygen penalty for diving deeper than your Diving Suit level allows for.
    Does not affect logic, as entering high pressure zones is never in logic.
    """

    display_name = "Harsh Pressure"

class NerfSkyFish(Toggle):
    """
    Reduces the sell price of Cloudswim, Skyfish, and Spacefish, making Jetpacks less overpowered.
    Logic is adjusted to account for this change.
    """

    display_name = "Nerf Sky Fish"

class ExtraUpgrades(Toggle):
    """
    Adds extra upgrades not present in the original game.
    Rapid Dive: Hold down to dive faster
    Shield: Lose less oxygen when getting hurt by hostile fish
    Insurance: When drowning, fish are sold for a fraction of their normal sell price. Materials are still lost.
    
    Note: This adds 11 items. Fishsanity must be enabled for there to be enough space for these items.
    If Fishsanity is not enabled, this option will be forced off.
    """

    display_name = "Extra Upgrades"

class TrapChance(Range):
    """
    Percentage chance to replace money filler with a Hostile Trap.
    Hostile Traps turn all fish hostile for 10 seconds.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 0

class GoldStatue(Choice):
    """
    How the Gold Statue item should be handled.
    Filler: The Gold Statue doesn't do anything.
    Item Requirement: The Gold Statue item is required to make the ending star spawn.
    Location Requirement: Same as Item Requirement, but the Gold Statue is also placed on its own location.
    """

    display_name = "Gold Statue Behaviour"

    option_filler = 0
    option_item_requirement = 1
    option_location_requirement = 2

    default = option_filler

@dataclass
class BuildJetpackOptions(PerGameCommonOptions):
    death_link: DeathLink
    fishsanity: Fishsanity
    harsh_pressure: HarshPressure
    nerf_sky_fish: NerfSkyFish
    extra_upgrades: ExtraUpgrades
    trap_chance: TrapChance
    gold_statue: GoldStatue

option_groups = [
    OptionGroup(
        "Items and Locations",
        [Fishsanity, ExtraUpgrades, TrapChance, GoldStatue]
    ),
    OptionGroup(
        "Game Tweaks",
        [HarshPressure, NerfSkyFish]
    )
]

option_presets = {
    "Painful": {
        "death_link": True,
        "fishsanity": False,
        "harsh_pressure": True,
        "nerf_sky_fish": True,
        "extra_upgrades": False,
        "trap_chance": TrapChance.range_end,
        "gold_statue": GoldStatue.option_location_requirement
    },
    "Developers' Preference": {
        "death_link": False,
        "fishsanity": True,
        "harsh_pressure": True,
        "nerf_sky_fish": True,
        "extra_upgrades": True,
        "trap_chance": 50,
        "gold_statue": GoldStatue.option_location_requirement
    },
    "Surprise Me": {
        "death_link": "random",
        "fishsanity": "random",
        "harsh_pressure": "random",
        "nerf_sky_fish": "random",
        "extra_upgrades": "random",
        "trap_chance": "random",
        "gold_statue": "random"
    }
}
from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import BuildJetpackWorld

def set_all_rules(world: BuildJetpackWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)

def upgrade_tier_requirement(world: BuildJetpackWorld, tier: int) -> Rule:
    if (world.options.nerf_sky_fish and tier <= 4):
        return (Has("Diving Suit", count=tier-1) & Has("Oxygen Mask", count=tier-1)) | Has("Jetpack", count=tier-1)
    elif tier <= 6 and not world.options.nerf_sky_fish:
        return (Has("Diving Suit", count=tier-1) & Has("Oxygen Mask", count=tier-1)) | Has("Jetpack", count=tier//2)
    elif tier <= 6:
        return (Has("Diving Suit", count=tier-1) & Has("Oxygen Mask", count=tier-1))
    else:
        return Has("Diving Suit", count=tier-1) & Has("Oxygen Mask", count=6) # you can survive depth 8 just fine with only 6 oxygen masks

def set_shop_tier_rules(tier: int, world: BuildJetpackWorld):
    access: Rule = upgrade_tier_requirement(world, tier)
    stringtier = str(tier)
    world.set_rule(world.get_location("Diving Suit "+stringtier), access)
    world.set_rule(world.get_location("Oxygen Mask "+stringtier), access)
    world.set_rule(world.get_location("Magnet "+stringtier), access)
    if (tier < 8):
        world.set_rule(world.get_location("Backpack "+stringtier), access)
        world.set_rule(world.get_location("Fins "+stringtier), access)

def set_all_location_rules(world: BuildJetpackWorld) -> None:
    for i in range(2,9): # skip tier 1, which needs no rules
        set_shop_tier_rules(i, world)

    world.set_rule(world.get_location("Raft Expansion 1"), Has("Rock"))
    world.set_rule(world.get_location("Raft Expansion 2"), Has("Rock"))
    world.set_rule(world.get_location("Raft Expansion 3"), Has("More Rock"))
    world.set_rule(world.get_location("Jetpack 1"), Has("More Rock") & Has("Raft Expansion", count=1))
    world.set_rule(world.get_location("Jetpack 2"), Has("More Rock") & Has("Raft Expansion", count=1))
    world.set_rule(world.get_location("Jetpack 3"), Has("More Gold") & Has("Raft Expansion", count=1))
    world.set_rule(world.get_location("Radar 1"), Has("Strings") & Has("Raft Expansion", count=2))
    world.set_rule(world.get_location("Radar 2"), Has("More Strings") & Has("Raft Expansion", count=2))
    world.set_rule(world.get_location("Radar 3"), Has("More Strings") & Has("Rock") & Has("Raft Expansion", count=2)) # rock requirement is unnecessary, but makes more sense in UT /explain
    world.set_rule(world.get_location("Radar 4"), Has("Gold") & Has("Raft Expansion", count=2))
    world.set_rule(world.get_location("Radar 5"), Has("Gold") & Has("Raft Expansion", count=2))
    world.set_rule(world.get_location("Gold Statue"), Has("More Gold") & Has("Raft Expansion", count=3))

    if world.options.gold_statue.value > 0:
        world.set_rule(world.get_location("Reach for the Stars"), Has("Gold Statue"))


def set_completion_condition(world: BuildJetpackWorld) -> None:
    world.set_completion_rule(Has("Victory"))
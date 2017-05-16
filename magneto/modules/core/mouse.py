from dragonfly import (
    Choice,
    Function,
    Playback,
    )

import aenea
import aenea.misc
import aenea.vocabulary
import aenea.configuration
import aenea.format

from aenea import (
    AeneaContext,
    AppContext,
    Alternative,
    CompoundRule,
    Dictation,
    DictList,
    DictListRef,
    Grammar,
    IntegerRef,
    Key,
    Literal,
    ProxyAppContext,
    MappingRule,
    Mouse,
    NeverContext,
    Repetition,
    Repeat,
    RuleRef,
    Sequence,
    Text
    )

from magneto.nexus import nexus
from magneto.mergerule import MergeRule

print('loading shortcut rules')

def adjust_and_click_mouse(button, direction, n500):
    if direction is "left":
        Mouse("<-%s,0>" % n500).execute()
    elif direction is "right":
        Mouse("<%s,0>" % n500).execute()
    elif direction is "up":
        Mouse("<0, -%s>" % n500).execute()
    elif direction is "down":
        Mouse("<0, %s>" % n500).execute()
    Mouse(button).execute()

def click_mouse(button):
    Mouse("left").execute()

class Mousing(MergeRule):
    mapping = {
        # "jump": Function(move_mouse),
        "[<button>] kick": Function(click_mouse),
        # "[<button>] click": Function(move_and_click_mouse),
        "[<button>] lick [<n500>]": Function(adjust_and_click_mouse, button="left", direction="left"),
        "[<button>] rick [<n500>]": Function(adjust_and_click_mouse, button="left", direction="right"),
        "[<button>] sick [<n500>]": Function(adjust_and_click_mouse, button="left", direction="up"),
        "[<button>] dick [<n500>]": Function(adjust_and_click_mouse, button="left", direction="down"),
    }

    extras = [
        IntegerRef("n500", 1, 500),
        Choice("button",
            {"left": "left",
            "right": "right",
            "middle": "middle",
            "dub": "double"}),
    ]

    defaults = {
        "n100": 1,
        "button": 'left',
    }

nexus().merger.add_global_rule(Mousing())
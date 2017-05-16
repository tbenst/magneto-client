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

repeat_shortcut = {
    "fly": "c-right",
    "swim": "c-left",
    "undo": "c-z",
    "redo": "c-y",
    "conduct": "c-d",
    "conger": "c-c",
    "queue": "cs-right",
    "buffer": "cs-left",
    "shin": "s-right",
    "shine": "s-left",
    "shown": "s-down",
    "shop": "s-up",
    "indent": "c-rbracket",
    "outdent": "c-lbracket",

}

single_shortcut = {
    # copy and paste are implemented in copypaste.py
    "prequel": "space,equal,space",
    "save": "c-s",
    "duple": "end,s-home,c-c,end,enter,c-v",
    "find": "c-f",
    "new tab": "c-t",
    "new window": "c-n",
    "new terminal": "ca-t",
    "cut": "c-x",
}

def single_press(single_shortcut):
    press_shortcut(single_shortcut)

def repeat_press(repeat_shortcut, n500):
    press_shortcut(repeat_shortcut, n500)

def press_shortcut(shortcut, n500=1):
    for x in range(n500):
        Key(shortcut).execute()

def swap():
    pass

workmap = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "0",
    11: "hyphen",
    12: "equal"
}
def workspace_switcher(n12):
    Key("ca-"+workmap[n12]).execute()

def workspace_mover(n12):
    Key("caw-"+workmap[n12]).execute()


def resize_window(window_direction):
    if window_direction is "left":
        Key("cw-left").execute()
    elif window_direction is "right":
        Key("cw-right").execute()
    elif window_direction is "maximize":
        Key("cw-up").execute()
    elif window_direction is "minimize":
        Key("cw-down").execute()


class Shortcuts(MergeRule):
    mapping = {
        "<single_shortcut>": Function(single_press),
        "<repeat_shortcut> [<n500>]": Function(repeat_press),
        "work <n12>": Function(workspace_switcher),
        "switch [<n100>]": Key('alt:down,tab:%(n100)s,alt:up'),
        "swap [<n100>]": Key('alt:down,backtick:%(n100)s,alt:up'),
        "swipe [<n100>]": Key('alt:down,ctrl:down,tab:%(n100)s,ctrl:down,alt:up'),
        "window move <n12>": Function(workspace_mover),
        "window <window_direction>": Function(resize_window),
        "launcher": Key("win:down,ctrl:down,l,ctrl:up,win:up"),
        # "swap <n100>": Key('alt:down/25,tab/25:%(n100)s,alt:up')
    }

    extras = [
        IntegerRef("n100", 1, 100),
        IntegerRef("n500", 1, 500),
        IntegerRef("n12", 1, 13),
        Choice("single_shortcut", single_shortcut),
        Choice("repeat_shortcut", repeat_shortcut),
        Choice("window_direction", {
            "left": "left",
            "right": "right",
            "maximize": "maximize",
            "minimize": "minimize",
            })
    ]

    defaults = {
        "n100": 1,
        "n500": 1,
    }

nexus().merger.add_global_rule(Shortcuts())

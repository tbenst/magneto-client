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

print('loading keyboard rules')




# def get_typing_key_choice(spec):
#     return Choice(spec, {

alphabet_key = {
    "arch": "a",
    "brov": "b", 
    "char": "c", 
    "delta": "d", 
    "echo": "e", 
    "frank": "f", 
    "golf": "g", 
    "hotel": "h", 
    "India": "i", 
    "julia": "j", 
    "kilo": "k", 
    "Lima": "l", 
    "Mike": "m", 
    "Nancy": "n", 
    "oscar": "o", 
    "prime": "p", 
    "Quid": "q", 
    "Roma": "r", 
    "Sarah": "s", 
    "tango": "t", 
    "Uni": "u", 
    "victor": "v", 
    "whiskey": "w", 
    "x-ray": "x", 
    "yankee": "y", 
    "Zulu": "z",
}

standard_key = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "quote": "dquote",
    "squat": "squote",
    "slash": "slash",
    "backslash": "backslash",
    "fin": "hyphen",
    "commie": "comma",
    "coming": "comma",
    "dot": " dot",
    "question": "question",
    "laser": "home",
    "razor": "end",
    "clamor": "exclamation",
    "at sign": "at",
    "hash": "hash",
    "cole": "colon",#?
    "call": "colon",#?
    "mace": "space",
    "peace": "lparen",
    "possum": "rparen",
    "brax": "lbracket",
    "bro": "rbracket",
    "brace": "lbrace",
    "bross": "rbrace",
    "lang": "langle",
    "rang": "rangle",
    "plus": "plus",
    "minus": "minus",
    # "plus minus": "plusminus", # this fails silently as it creates a conflicting command
    "percent": "percent",
    "semi": "semicolon",
    "dollar": "dollar",
    "carrot": "caret", #?
    "amp": "ampersand",
    "star": "asterisk",
    "score": "underscore",
    "tilde": "tilde",
    "vertical": "bar",
    "escape": "escape",
    "funk one": "f1",
    "funk to": "f2",
    "funk three": "f3",
    "funk for": "f4",
    "funk five": "f5",
    "funk six": "f6",
    "funk seven": "f7",
    "funk eight": "f8",
    "funk nine": "f9",
    "funk ten": "f10",
    "funk eleven": "f11",
    "funk twelve": "f12",
}

repeat_key = {
    "shock": "enter",
    "slap": "enter",
    "insert": "insert",
    "deli": "del", #?
    "clear": "backspace",
    "sauce": "up",
    "dunce": "down",
    "ross": "right",
    "lease": "left",
    "tabby": "tab",
    "sad": "pgup",
    "dad": "pgdown",
    "equal": "equal",
}

modifier_key = {
    "con": "c",
    "shift": "s",
    "alt": "a",
    "chief": "cs",
    "colt": "ca",
    "copper": "cw",
    "shalt": "sa"
        }

modifier_full_name = {
    "control": "ctrl",
    "shift": "shift",
    "alt": "alt",
    "super": "win",
}

any_key = standard_key.copy()
any_key.update(repeat_key) # merge dict
any_key.update(alphabet_key)

single_key = standard_key.copy()
# single_key.update(alphabet_key)


def alphabet_press(alphabet_key, modify_letter=None):
    if modify_letter is "cap":
        alphabet_key = alphabet_key.upper()

    any_press(alphabet_key)


def single_press(single_key):
    any_press(single_key)

def repeat_press(repeat_key, n500):
    any_press(repeat_key, n500)

def any_press( any_key, n100=1, modifier_key=None ):
    if modifier_key is None:
        k = any_key
    else:
        k = modifier_key + "-" + any_key
    for x in range(n100):
        Key(k).execute()

def super_press(any_key=None):
    if any_key is None:
        Key("win").execute()
    else:
        Key("w-%s" % any_key).execute()

class Keyboard(MergeRule):

    mapping = {
        "<single_key>": Function(single_press),
        "[<modify_letter>] <alphabet_key>": Function(alphabet_press),
        "<repeat_key> [<n500>]": Function(repeat_press),
        '<modifier_key> <any_key> [<n100>]': Function(any_press),
        "develop testing": Key('colon'),
        "super [<any_key>]": Function(super_press),
        "hold <modifier_full_name>": Key("%(modifier_full_name)s:down"),
        "release": Key("ctrl:up,alt:up,shift:up,win:up")
    }

    extras = [
        IntegerRef("n100", 1, 100),
        IntegerRef("n500", 1, 500),
        Choice("single_key", single_key),
        Choice("repeat_key", repeat_key),
        Choice("any_key", any_key),
        Choice("modifier_key", modifier_key),
        Choice("alphabet_key", alphabet_key),
        Choice("modify_letter", {"cap": "cap"}),
        Choice("modifier_full_name", modifier_full_name)
    ]

    defaults = {
        "n100": 1,
        "n500": 1,
    }

nexus().merger.add_global_rule(Keyboard())

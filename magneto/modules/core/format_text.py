
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

print('loading Format Text rules')

format_choices = {
    "snake": "lowercase_with_underscore",
    "sing": "first_upper_no_space",
    "dolphin": "lowercase_with_hyphen",
    "camel": "camelFormat",
    "yell": "YELLFORMAT",
    "symbol": "append_colon_with_underscore",
    "plain": "plain_format",
    "casual": "casual_format_",
    "prose": "Prose_format",
    "smoosh": "smooshformat",
    "title": "Uppercase_Each_Word_With_Space",
    "gerish": "TitleCamelFormat"
}

TEXT_FORMAT = "plain_format"
LAST_DICTATION = ""

def prepare_text(the_format, t):
    global TEXT_FORMAT
    t = str(t)
    if the_format is None:
        the_format = TEXT_FORMAT


    if the_format is "Prose_format":
        t = t.capitalize() + " "
    elif the_format is "lowercase_with_underscore":
        t = "_".join(t.lower().split(" "))
    elif the_format is "first_upper_no_space":
        t = t.capitalize()
        t = "".join(t.split(" "))
    elif the_format is "lowercase_with_hyphen":
        t = "-".join(t.lower().split(" "))
    elif the_format is "camelFormat":
        t = t.title()
        t = t[0].lower() + t[1:]
        t = "".join(t.split(" "))
    elif the_format is "YELLFORMAT":
        t = t.upper()
        t = "".join(t.split(" "))
    elif the_format is "smooshformat":
        t = t.lower()
        t = "".join(t.split(" "))
    elif the_format is "plain_format":
        t = t.lower()
    elif the_format is "casual_format_":
        t = t.lower() + " "
    elif the_format is "append_colon_with_underscore":
        t = ":" + t.lower()
        t = "".join(t.split(" "))
    elif the_format is "Uppercase_Each_Word_With_Space":
        t = t.title()
    elif the_format is "TitleCamelFormat":
        t = t.title()
        t = "".join(t.split(" "))
    
    TEXT_FORMAT = the_format
    return t

def set_format(the_format):
    global TEXT_FORMAT
    TEXT_FORMAT = the_format

def format_text(t, the_format=None):
    t = prepare_text(the_format, t)

    Text(t).execute()


class FormatText(MergeRule):

    mapping = {
        "<the_format> <t> [stop]": Function(format_text),
        # should make this a 'non' in caster lingo
        "<t>": Function(format_text),
        "format <the_format>": Function(set_format),
    }

    extras = [
        Choice("the_format", format_choices),
        Dictation("t")
    ]

    defaults = {
        "n100": 1,
        "n500": 1,
    }

nexus().merger.add_global_rule(FormatText())
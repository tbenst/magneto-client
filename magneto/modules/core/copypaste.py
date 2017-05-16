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
from magneto import settings
from magneto.settings import ModuleDictionary

print('loading copypaste rules')

try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise

CLIPBOARD = ModuleDictionary("core\\copypaste")

def paste(t,n):
    if n != 0:
        t=n
    if t=="default":
        Key("c-v").execute()
    else:
        global CLIPBOARD
        key = str(t)
        if key in CLIPBOARD.dictionary:
            previous = aenea.communications.server.paste(CLIPBOARD.dictionary[key])
            Key("c-v").execute()
            # restore previous clipboard value
            aenea.communications.server.paste(previous)
        else:
            print("No key '%s' in clipboard dictionary" % key)

def copy(t,n):
    if n != 0:
        t=n
    global CLIPBOARD
    key = str(t)
    selected_text = aenea.communications.server.copy()
    if key=="default":
        propagate_copy()
        Key("c-c").execute()
    CLIPBOARD[key] = selected_text

def propagate_copy():
    """move previous copy to index 2, 2 to 3, etc. drop 9.

    TODO Function not working"""
    print("propagating")
    for i in range(8,1):
        previous = str(i)
        next_key = str(i+1)
        if previous in CLIPBOARD:
            CLIPBOARD[next_key] = CLIPBOARD[previous]
    CLIPBOARD["1"] = CLIPBOARD["default"]

class CopyPaste(MergeRule):
    mapping = {
        "copy [<t> | <n>]": Function(copy),
        "paste [<t> | <n>]": Function(paste),
    }

    extras = [
        Dictation("t"),
        IntegerRef("n",0,9)
    ]

    defaults = {
        "t": 'default',
        "n": 0
    }

nexus().merger.add_global_rule(CopyPaste())
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
from magneto.modules.core.copypaste import CLIPBOARD

print('loading copypaste rules')

try:
    import aenea.communications
except ImportError:
    print 'Unable to import Aenea client-side modules.'
    raise


bash_context = AeneaContext(
    ProxyAppContext(cls_name='Terminal', cls='Terminal'),
    AppContext(executable='Terminal')
    )

bash_grammar = Grammar('bash', context=bash_context)



dictionary = ModuleDictionary("apps\\bash")

def paste(t,n):
    if n != 0:
        t=n
    if t=="default":
        Key("cs-v").execute()
    else:
        global CLIPBOARD
        key = str(t)
        if key in CLIPBOARD.dictionary:
            previous = aenea.communications.server.paste(CLIPBOARD.dictionary[key])
            Key("cs-v").execute()
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
    CLIPBOARD[key] = selected_text
    if key=="default":
        propagate_copy()
        Key("cs-c").execute()

def propagate_copy():
    "move previous copy to index 2, 2 to 3, etc. drop 9."
    for i in reversed(range(8,1)):
        previous = str(i)
        next_key = str(i+1)
        CLIPBOARD[next_key] = CLIPBOARD[previous]
    CLIPBOARD["1"] = CLIPBOARD["default"]

class Bash(MergeRule):

    mapping = {
        "pseudo-": Text("sudo "),
        "change": Text("cd "),
        "list": Key("l,s,enter"),
        "sublime": Text("subl "),
        "home": Text("~/"),
        "pie": Text("py"),
        "copy": Key("cs-c"),
        "copy <t>": Function(copy),
        "paste": Key("cs-v"),
        "paste <t>": Function(paste),
        "make directory": Text("mkdir "),
        ".Thought": Text(".."),
        "parent": Text("../"),
        "remote <ssh_server>": Text('ssh %(ssh_server)s'),
        "dropbox": Text("cd ~/Dropbox/"),
        "reset": Key("c-c,c-c,up,enter")
    }

    extras = [
        Choice('ssh_server', {}),
        Dictation("t"),
    ]

    defaults = {
        "t": 'default',
    }


bash_grammar.add_rule(Bash())

from dragonfly import (
    Choice,
    Function,
    Playback,
    )

from aenea import (
    AeneaContext,
    AppContext,
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

from magneto.mergerule import MergeRule
from magneto.settings import ModuleDictionary



from magneto.nexus import nexus
from magneto.mergerule import MergeRule

print('loading purescript rules')

def _import(t):
    Text("import "+ t).execute()

class Purescript(MergeRule):

    mapping = {
    Spec.IMPORT+" <t>": Function(_import)
    }

    extras = [
        Dictation("t"),

    ]

    defaults = {
    }

nexus().merger.add_global_rule(Purescript())


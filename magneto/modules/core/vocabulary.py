
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
from magneto.settings import ModuleDictionary

print('loading Vocabulary')

dictionary = ModuleDictionary("core\\vocabulary").dictionary
print("dict",dictionary)

class Vocabulary(MergeRule):
    mapping = {key: Text(value) for key,value in dictionary.items()}

nexus().merger.add_global_rule(Vocabulary())
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


sublime_context = AeneaContext(
    ProxyAppContext(cls_name='Sublime', cls='Sublime'),
    AppContext(executable='Sublime')
    )

sublime_grammar = Grammar('sublime', context=sublime_context)


dictionary = ModuleDictionary("apps\\sublime")

def go_to_line(n1000):
    Key("c-g").execute()
    Text(str(n1000)).execute()
    Key("enter").execute()


class Sublime(MergeRule):

    mapping = {
        "line <n1000>": Function(go_to_line),

    }

    extras = [
        IntegerRef("n1000", 1, 1000),
    ]

    defaults = {

    }


sublime_grammar.add_rule(Sublime())

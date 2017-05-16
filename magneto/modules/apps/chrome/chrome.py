# from dragonfly import (
#     Choice,
#     Function,
#     Playback,
#     )

# from aenea import (
#     AeneaContext,
#     AppContext,
#     Grammar,
#     IntegerRef,
#     Key,
#     Literal,
#     ProxyAppContext,
#     MappingRule,
#     NeverContext,
#     Repetition,
#     Repeat,
#     RuleRef,
#     Sequence,
#     Text
#     )

# from magneto.mergerule import MergeRule

# chrome_context = AeneaContext(
#     ProxyAppContext(cls_name='Terminal', cls='Terminal'),
#     AppContext(executable='Terminal')
#     )

# bash_grammar = Grammar('bash', context=bash_context)


# class Bash(MergeRule):

#     mapping = {
#         "pseudo-": Text("sudo "),
#         "change": Text("cd "),
#         "list": Key("l,s,enter"),
#         "sublime": Text("subl "),
#         "home": Text("~/"),
#         "pie": Text("py"),
#         "copy": Key("cs-c"),
#         "paste": Key("cs-v"),
#         "make directory": Text("mkdir ")

#     }

#     extras = [

#     ]

#     defaults = {

#     }


# bash_grammar.add_rule(Bash())

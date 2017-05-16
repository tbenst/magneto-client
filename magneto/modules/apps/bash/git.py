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

from bash import bash_grammar

print('loading git rules')

def git(git_command,name=""):
    t = "git "
    if git_command is "clone":
        t += "clone git@github.com:"
    elif git_command is "add":
        t += "add ."
    elif git_command is "delete":
        t += "push origin --delete {} && git branch -d {}".format(name,name)
    elif git_command is "all":
        t += 'add . && git commit -m "" && git push'
    elif git_command is "commit":
        t += 'commit -m ""'
        Key("left").execute()
    elif git_command is "pull":
        t += "pull "
    elif git_command is "push":
        t += "push "
    elif git_command is "checkout":
        t += "checkout "
    elif git_command is "init":
        t += "init "
    elif git_command is "status":
        t += "status "
    else:
        t += git_command + " "
    Text(t).execute()

    if git_command is "all":
        Key("c-left:3,right:3").execute()
    

class Get(MergeRule):

    mapping = {
        "get <git_command> [<name>]": Function(git),
    }

    extras = [
        Choice("git_command", {
            "clone": "clone",
            "add": "add",
            "all": "all",
            "commit": 'commit',
            "pull": "pull",
            "push": "push",
            "checkout": "checkout",
            "And it": "init",
            "merge": "merge",
            "delete": "delete",
            "stash": "stash",
            "stash apply": "stash apply",
            "status": "status"
            }),
        Dictation("name")
    ]

    defaults = {

    }

bash_grammar.add_rule(Get())

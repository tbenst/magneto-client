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

print('loading docker rules')

class Docker(MergeRule):

    mapping = {
        "(docker|darker|doctor) build": Text("sudo docker build ."),
        '(docker|darker|doctor)': Text("sudo docker "),
        '(docker|darker|doctor) build (tag|tagged)': Text("sudo docker build -t \"\" .") + Key("left:3"),
        '(docker|darker|doctor) list images': Text("sudo docker images") + Key("enter"),
        '(docker|darker|doctor) list containers': Text("sudo docker ps -a") + Key("enter"),
        '(docker|darker|doctor) stop': Text("sudo docker stop "),
        '(docker|darker|doctor) (remove|delete) image': Text("sudo docker rmi "),
        '(docker|darker|doctor) (remove|delete) [container]': Text("sudo docker rm "),
        '(docker|darker|doctor) run': Text("sudo docker run "),
        '(docker|darker|doctor) compose all': Text("sudo docker-compose stop && sudo docker-compose build && sudo docker-compose up"),
        '(docker|darker|doctor) inspect': Text("sudo docker inspect "),
        '(docker|darker|doctor) enter': Text("sudo ~/bin/docker-enter "),
        '(docker|darker|doctor) remove all': Text("docker rm -f $(docker ps -a -q)"),
        '(docker|darker|doctor) remove images': Text("docker rmi $(docker images -q)"),
    }

    extras = [

    ]

    defaults = {

    }


bash_grammar.add_rule(Docker())

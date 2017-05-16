
from dragonfly import Function, Playback
from magneto.nexus import nexus
from magneto import settings
from magneto.mergerule import MergeRule
from subprocess import Popen
import aenea

print('loading Dragon rules')

def reboot_dragon():
    popen_params = []
    popen_params.append(settings.PATH + r'\\bin\\reboot.bat')
    popen_params.append(settings.MAGNETO['path']['dragon'])
    print(popen_params)
    Popen(popen_params)

def do_nothing():
    pass

do_nothing_words = [
    "him",
    "the",
    "it's"
]
def test_server_functionality():
    aenea.communications.server.greet_user("tyler")
    aenea.communications.server.paste("testing one two three")

class Dragon(MergeRule):



    mapping = {
        "reboot dragon": Function(reboot_dragon),
        "snooze": Playback([(["go to sleep"], 0.0)]),
        # the next two words are often misrecognized on their own
        "him": Function(do_nothing),
        "the": Function(do_nothing),
        "it's": Function(do_nothing),
        "server test": Function(test_server_functionality)
    }
    mapping.update({word: Function(do_nothing) for word in do_nothing_words})

    extras = [
    ]

    defaults = {
    }

nexus().merger.add_global_rule(Dragon())
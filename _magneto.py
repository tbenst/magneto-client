#! python2.7
'''
main magneto module
Created on Aug 7, 2016
Based on Caster by synkarius
Forked and modified by tbenst
'''
import logging
logging.basicConfig()

from magneto import settings, nexus
import os

settings.set_path(os.path.join(os.path.dirname(__file__), "magneto\\"))
# settings.set_path("E://magneto/etc/magneto.yaml")
print('settings', settings.MAGNETO)
NEXUS = nexus.nexus()

from magneto.mergerule import MergeRule
from magneto.ccrmerger import Inf
from magneto import modules

from dragonfly import (
    Choice,
    Function,
    # Key,
    Playback,
    # Repeat,
    # Text
    )

from aenea import (
	Key,
	Text,
	Choice,
	MappingRule,
	Grammar
	)
print('global rules', NEXUS.merger.global_rule_names())

class MainRule(MappingRule):
    
    @staticmethod
    def generate_ccr_choices(nexus):
        choices = {}
        # this uses a different nexus in original code foo some reason..
        for ccr_choice in NEXUS.merger.global_rule_names():
            choices[ccr_choice] = ccr_choice
        return Choice("name", choices)
    # @staticmethod
    # def generate_sm_ccr_choices(nexus):
    #     choices = {}
    #     # this uses a different nexus in original code foo some reason..
    #     for ccr_choice in NEXUS.merger.selfmod_rule_names():
    #         choices[ccr_choice] = ccr_choice
    #     return Choice("name2", choices)
    
    mapping = {
    # # Dragon NaturallySpeaking commands moved to dragon.py
    
    # # hardware management
    # "volume <volume_mode> [<n>]":   R(Function(navigation.volume_control, extra={'n', 'volume_mode'}), rdescript="Volume Control"),
    
    # # window management
    # 'minimize':                     Playback([(["minimize", "window"], 0.0)]),
    # 'maximize':                     Playback([(["maximize", "window"], 0.0)]),
    # "remax":                        R(Key("a-space/10,r/10,a-space/10,x"), rdescript="Force Maximize"),
        
    # # passwords
    # 'hash password <text> <text2> <text3>':                    R(Function(password.hash_password), rdescript="Get Hash Password"),
    # 'get password <text> <text2> <text3>':                     R(Function(password.get_password), rdescript="Get Seed Password"),
    # 'get restricted password <text> <text2> <text3>':          R(Function(password.get_restricted_password), rdescript="Get Char-Restricted Password"),
    # 'quick pass <text> <text2> <text3>':                       R(Function(password.get_simple_password), rdescript="Get Crappy Password"),
    
    # # mouse alternatives
    # "legion [<monitor>]":           R(Function(navigation.mouse_alternates, mode="legion", nexus=NEXUS), rdescript="Activate Legion"),
    # "rainbow [<monitor>]":          R(Function(navigation.mouse_alternates, mode="rainbow", nexus=NEXUS), rdescript="Activate Rainbow Grid"),
    # "douglas [<monitor>]":          R(Function(navigation.mouse_alternates, mode="douglas", nexus=NEXUS), rdescript="Activate Douglas Grid"),
    
    # # symbol match
    # "scan directory":               R(Function(scanner.scan_directory, nexus=NEXUS), rdescript="Scan Directory For PITA"),
    # "rescan current":               R(Function(scanner.rescan_current_file), rdescript="Rescan Current File For PITA"),
    # "begin symbol training":        R(Function(trainer.trainer_box, nexus=NEXUS), rdescript="Train From Scanned Directory") , 
    # ccr de/activation
    "<enable> <name>":              Function(NEXUS.merger.global_rule_changer(), save=True),
    # "<enable> <name2>":             Function(NEXUS.merger.selfmod_rule_changer(), save=True),
    
    
    }
    extras = [
              # IntegerRefST("n", 1, 50),
              # Dictation("text"),
              # Dictation("text2"),
              # Dictation("text3"),
              Choice("enable",
                    {"enable": True, "disable": False
                    }),
              # Choice("volume_mode",
              #       {"mute": "mute", "up":"up", "down":"down"
              #        }),
              generate_ccr_choices.__func__(NEXUS),
              # generate_sm_ccr_choices.__func__(NEXUS),
             ]
    defaults = {
		       # "n": 1, "nnv": 1,
               # "text": "", "volume_mode": "setsysvolume",
               "enable":-1
               }


grammar = Grammar('general')
grammar.add_rule(MainRule())
# grammar.add_rule(Again(NEXUS))
# grammar.add_rule(VanillaAlias(name="vanilla alias"))
grammar.load()

NEXUS.merger.update_config()
NEXUS.merger.merge(Inf.BOOT)

# if settings.MAGNETO["miscellaneous"]["status_window_enabled"]:
#     print("\nWARNING: Status Window is an experimental feature, and there is a known freezing glitch with it.\n")
#     utilities.launch_status()

print("*- Starting " + "magneto" + " -*")

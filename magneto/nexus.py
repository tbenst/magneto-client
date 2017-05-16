# from dragonfly.grammar.grammar_base import Grammar
# from dragonfly.grammar.recobs import RecognitionHistory
from aenea import Grammar
# from aenea import RecognitionHistory

# from caster.lib import settings
# from caster.lib.ctrl.dependencies import DependencyMan
# from caster.lib.ctrl.intermediary import StatusIntermediaryAll
# from caster.lib.ctrl.switcher import AutoSwitcher
# from caster.lib.ctrl.wsrdf import TimerForWSR, RecognitionHistoryForWSR
# from caster.lib.dfplus.communication import Communicator
# from caster.lib.dfplus.merge.ccrmerger import CCRMerger
# from caster.lib.dfplus.state.stack import CasterState
# from aenea.strict import *
from magneto.ccrmerger import CCRMerger


class Nexus:
    # def __init__(self, real_merger_config=True):
    def __init__(self):
        
        # self.state = CasterState()
        
        # self.clipboard = {}
        self.sticky = []
        
        # self.history = RecognitionHistoryForWSR(20)
        # if not settings.WSR:
        #     self.history = RecognitionHistory(20)
            # self.history.register()
        # self.history = RecognitionHistory(20)
        # self.history.register()
        # self.state.set_stack_history(self.history)
        self.preserved = None
        
        # self.timer = TimerForWSR(0.025)
        # if not settings.WSR:
            # from dragonfly.timer import _Timer
            # self.timer = _Timer(0.025)
        # from dragonfly.timer import _Timer
        # self.timer = _Timer(0.025)
        
        # self.comm = Communicator()
        # self.intermediary = StatusIntermediary(self.comm, self.timer)
        
        # self.dep = DependencyMan()
        
        self.macros_grammar = Grammar("recorded_macros")
        
        # self.merger = CCRMerger(real_merger_config)
        self.merger = CCRMerger()
        # self.auto = AutoSwitcher(self)


_NEXUS = None
def nexus():
    global _NEXUS
    if _NEXUS is None:
        _NEXUS = Nexus()
    return _NEXUS

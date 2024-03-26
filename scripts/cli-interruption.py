import logging, signal
from modules import shared

sharedStateLog = logging.getLogger('modules.shared_state')
sharedStateLog.setLevel(logging.INFO)

oldCtrlC = signal.getsignal(signal.SIGINT)

def newCtrlC(*args, **kwargs):
    if shared.state.job != "" and not shared.state.interrupted:
        print()
        print('Caught KeyboardInterrupt, interrupting generation...', flush=True)
        shared.state.interrupt()
    else:
        oldCtrlC(*args, **kwargs)

signal.signal(signal.SIGINT, newCtrlC)

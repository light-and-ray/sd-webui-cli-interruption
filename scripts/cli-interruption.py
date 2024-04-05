import logging, signal, sys
from modules import shared, script_callbacks

sharedStateLog = logging.getLogger('modules.shared_state')

if sharedStateLog.getEffectiveLevel() > logging.INFO:
    sharedStateLog.setLevel(logging.INFO)

if sharedStateLog.handlers == []:
    handler = logging.StreamHandler(sys.stdout)
    sharedStateLog.addHandler(handler)


oldCtrlC = signal.getsignal(signal.SIGINT)

def newCtrlC(*args, **kwargs):
    if shared.state.job != "" and not shared.state.interrupted:
        print()
        print('Caught KeyboardInterrupt, interrupting generation...', flush=True)
        shared.state.interrupt()
    else:
        oldCtrlC(*args, **kwargs)

signal.signal(signal.SIGINT, newCtrlC)


def un_patch():
    signal.signal(signal.SIGINT, oldCtrlC)

script_callbacks.on_script_unloaded(un_patch)

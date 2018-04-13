#
# HELPERS
#
def log(msg,noisy,level='INFO'):
    if noisy:
        print("[{}] SUBLIME-REMOTE: {}".format(level,msg))
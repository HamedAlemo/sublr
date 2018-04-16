from __future__ import print_function
import os
import re
import json
from glob import glob
import webbrowser as web
import sublr.constants as c
import sublr.config as config
import sublr.utils as utils
from shutil import copyfile, move
#
# CONFIG CONSTANTS
#
PORT=config.get('port')
REMOTE_PATH=config.get('remote_path')
SSH_KEY=config.get('ssh_key')
NOISY=config.get('noisy')
AUTO_INIT=config.get('auto_init')


#
# METHODS
#
def create(ident,ip,remote_path=REMOTE_PATH,ssh_key=SSH_KEY,auto_init=AUTO_INIT,noisy=NOISY):
    """ create new remote sftp-config file

        Args:

            ident<str>: name used to identify sftp-config
            ip<str>:     
                - ip address for remote config
                - must be valid ip or include the string 'dev'
            remote_path<str>: path to the code-base on remote instance
            ssh_key<str>: path to ssh key. default to gcloud (~/.ssh/google_compute_engine)
            auto_init<bool>: if true initialize remote after creation


    """
    cnfg=c.CONFIG_DICT.copy()
    if re.match(c.IP_REGEX,ip) or re.search('dev',ip):
        cnfg['sublr']=ident
        cnfg['host']=ip
        cnfg['remote_path']=remote_path
        cnfg['ssh_key_file']=ssh_key
        file=c.REMOTE_CONFIG_PATH_TMPL.format(ident)
        with open(file, 'w') as f:
            json.dump(cnfg,f,indent=4,sort_keys=True)
        if auto_init: 
            init(ident, noisy)
    else:
        utils.log(c.INVALID_IP_TMPL.format(ip),True,level="ERROR")


def init(ident,noisy=NOISY):
    """ initialize remote config
    """
    file=c.REMOTE_CONFIG_PATH_TMPL.format(ident)
    if os.path.exists(file):
        try:
            try:
                move(c.CONFIG_PATH,c.BAK_CONFIG_PATH)
            except IOError:
                utils.log(c.INITIAL_CONFIG,noisy)
            copyfile(file, c.CONFIG_PATH)
            utils.log(c.ON_TMPL.format(ident),noisy)
        except OSError:
            pass
    else:
        utils.log(c.FILE_DOES_NOT_EXIST_TMPL.format(file),True,level="ERROR")  


def off(noisy=NOISY):
    """ disable remote
    """
    try:
        os.remove(c.CONFIG_PATH)
        utils.log(c.OFF,noisy,level="INIT")
    except OSError:
        utils.log(c.NOT_ON,noisy,level="WARN")


def open_port(port=PORT,noisy=NOISY):
    """ open port for current remote in a web browser
    """
    with open(c.CONFIG_PATH, 'r') as f:
        cnfg=json.load(f)
    url=c.URL_TMPL.format(cnfg['host'],port)
    web.open_new_tab(url)
    utils.log(c.OPENED_TMPL.format(url),noisy)


def current():
    """ print current remote ident
    """
    try:
        with open(c.CONFIG_PATH, 'r') as f:
            cnfg=json.load(f)
        utils.log(c.WHO_TMPL.format(cnfg.get('sublr','unknown')),True)
    except IOError:
         utils.log(c.NOT_ON,True)


def list_remotes():
    """ list the idents for the available remote sftp-config files
    """
    selector=c.REMOTE_CONFIG_PATH_TMPL.format('*')
    root=c.REMOTE_CONFIG_PATH_TMPL.format('')
    files=glob(c.REMOTE_CONFIG_PATH_TMPL.format('*'))
    utils.log(c.AVAILABLE_REMOTES,True)
    for file in files:
        ident=file.replace(root,'')
        utils.log(c.AVAILABLE_REMOTE_TMPL.format(ident),True)


def remove(ident,noisy=NOISY):
    """ remove remote config
    """
    file=c.REMOTE_CONFIG_PATH_TMPL.format(ident)
    try:
        os.remove(file)
        utils.log(c.REMOVED_TMPL.format(ident),noisy)
    except OSError:
        utils.log(c.FILE_DOES_NOT_EXIST_TMPL.format(file),noisy,level="WARN")







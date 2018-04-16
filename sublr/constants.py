""" CONSTANTS
"""
#
# DEFAULT CONFIG
#
PORT=8888
NOISY=True
REMOTE_PATH=''
AUTO_INIT=True


#
# PRINT STRINGS
#
AVAILABLE_REMOTES="AVAILABLE REMOTES:"
INITIAL_CONFIG="on"
NOT_ON="disabled"
OFF="off"


#
# PATHS
#
CONFIG_PATH='sftp-config.json'
BAK_CONFIG_PATH='{}.bak'.format(CONFIG_PATH)
SUBLR_CONFIG_PATH='sublr.config.yaml'


#
# STRING TEMPLATES
#
URL_TMPL="http://{}:{}"
AVAILABLE_REMOTE_TMPL='\t  * {}'
REMOTE_CONFIG_PATH_TMPL="{}."+CONFIG_PATH
FILE_DOES_NOT_EXIST_TMPL="{} does not exist"
INVALID_IP_TMPL='{} is not a valid ip address'
OPENED_TMPL='opened {}'
REMOVED_TMPL='< {} > removed'
ON_TMPL='< {} >'
WHO_TMPL='< {} >'


#
# JSON TEMPLATES
#
CONFIG_DICT={
    "type": "sftp",
    "sync_down_on_open": False,
    "upload_on_save":True,
    "host": None,
    "remote_path": None,
    "user": "brook",
    "port":22,
    "ignore_regexes":[
        "/data/",
        "/.kaggle-cli/",
        "\\.sublime-(project|workspace)", 
        "sftp-config(-alt\\d?)?\\.json", 
        "sftp-settings\\.json", "/venv/", 
        "\\.svn", 
        "\\.hg", 
        "\\.git/", 
        "\\.bzr", 
        "_darcs", 
        "CVS", 
        "\\.DS_Store", 
        "Thumbs\\.db", 
        "desktop\\.ini"],
    "connect_timeout": 30,
    "ssh_key_file": None
}


#
# OTHER
#
SSH_KEY="~/.ssh/google_compute_engine"
IP_REGEX="\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
SUBLR_CONFIG_COMMENT="sublr: config"
SUBLR_CONFIG_EXISTS="sublr.config.yaml exists.  use force=True to overwrite."
SUBLR_CONFIG_CREATED="sublr.config.yaml created. edit file to change configuration"


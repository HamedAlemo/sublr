#
# CONFIG 
#
DEFAULT_PORT=8888
URL_TMPL="http://{}:{}"
NOISY=True
REMOTE_PATH=''
AUTO_INIT=True
#
# CONSTANTS 
#
IP_REGEX="\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
CONFIG_PATH='sftp-config.json'
BAK_CONFIG_PATH='{}.bak'.format(CONFIG_PATH)
AVAILABLE_REMOTES="AVAILABLE REMOTES:"
AVAILABLE_REMOTE_TMPL='\t  * {}'
REMOTE_CONFIG_PATH_TMPL="{}."+CONFIG_PATH
FILE_DOES_NOT_EXIST_TMPL="{} does not exist"
INITIAL_CONFIG="initial config"
NOT_ON="sublremote is not on"
INVALID_IP_TMPL='{} is not a valid ip address'
OPENED_TMPL='opened {}'
REMOVED_TMPL='< {} > removed'
ON_TMPL='< {} > on'
WHO_TMPL='< {} >'
SUBL_OFF='sublime-remote off'
#
# TEMPLATE FOR SublimeSFTP config file.
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
    "ssh_key_file": "~/.ssh/google_compute_engine"
}

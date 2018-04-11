#
# CONFIG 
#
DEFAULT_PORT=8888
URL_TMPL="http://{}:{}"
NOSIY=True
REMOTE_PATH='~/'
NOT_ON="sublremote is not on"
#
# CONSTANTS 
#
IP_REGEX="\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
CONFIG_PATH='sftp-config.json'
BAK_CONFIG_PATH='{}.bak'.format(CONFIG_PATH)
REMOTE_CONFIG_PATH_TMPL="{}."+CONFIG_PATH
FILE_DOES_NOT_EXIST="{} does not exist"
OPENED_TMPL='opened {}'
ON_TMPL='<{}> on'
HELP="""\tOne of the following:\n
\t\t* "<REMOTE_IDENT>" (turn on sublr for ident)
\t\t* "init <IP_ADDRESS> <REMOTE_PATH|optional>" (create new subl.sftp file)
\t\t* "off" (turn off sublr)
\t\t* "who" (return the current remote ident) 
"""
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

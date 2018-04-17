##### SUBLIME REMOTE: A companion to SublimeSFTP

_CLI for managing multiple SublimeSFTP config files_

[SUBLIME-SFTP](https://wbond.net/sublime_packages/sftp) makes it easy to sync your local Sublime with a remote instance. However, when using multiple remote instances, such as a CPU for development and GPU for training, it can get be bit cumbersome. Sublime-Remote is a CLI to make that easy.

---

##### INSTALL

```bash
git clone https://github.com/brookisme/sublr.git
cd sublr
pip install -e .
```

---

##### USAGE

```bash
# create configurations for a cpu and gpu
sublr create cpu 12.345.678.910 path/to/code/base
sublr create gpu 10.987.654.321 path/to/code/base
# turn on syncing with the cpu
sublr init cpu
# turn off syncing
sublr off
# remove config for the gpu
sublr remove gpu
# open a port for the current remote in web-browser
sublr open
```

---

##### DOCS

```bash
$ sublr --help
Usage: sublr [OPTIONS] COMMAND [ARGS]...

Options:
  --noisy BOOLEAN  print info and warning messages
  --help           Show this message and exit.

Commands:
  config   generate config file
  create   create and initialize new remote config
  current  print current remote ident
  init     initialize a new sftp-config
  list     list available remote configs
  off      turn off sublr
  open     open current port for the current remote
  remove   remove sftp-config for ident
```

1. [create](#create): creates a new config file for a remote instance
2. [init](#init): initialize sublime-sftp for a a remote instance
3. [off](#off): turn off sublime-remote
4. [open](#open): open port for remote instance in a web-browser
5. [current](#current): print currently enabled remote instance
6. [list](#list): list remote instances with sftp-configs
7. [remove](#remove): remove sftp-config for remote instance
8. [config](#config): generate sublr config file 

---

<a name='create'></a>

##### CREATE

Create and Initialize new sftp-config for remote instance.

- IDENT: id for instance
- IP: ip-address for remote instance. must be valid ip-address or include the string 'dev'
- REMOTE_PATH: path for the code on remote instance (defaults to '')
- AUTO_INIT: if true initialize sftp-config after creation (defaults to true)

```bash
# Usage: sublr create [OPTIONS] IDENT IP [REMOTE_PATH] [AUTO_INIT]
$ sublr create cpu 12.345.678.910 path/to/code/base
[INFO] SUBLIME-REMOTE: < cpu > on

$ sublr create gpu 10.987.654.321 path/to/code/base
[INFO] SUBLIME-REMOTE: < gpu > on
```

---

<a name='init'></a>

##### INIT

- IDENT: initialize sftp-config for `ident`

```bash
# Usage: sublr init [OPTIONS] IDENT
$ sublr init cpu
[INFO] SUBLIME-REMOTE: < cpu > on
```
---

<a name='off'></a>

##### OFF

```bash
# Usage: sublr off [OPTIONS]
$ sublr off
[INIT] SUBLIME-REMOTE: off
```

---

<a name='open'></a>

##### OPEN

Open port in web-browser. Defaults to 8888 or to port in [sublr.config.yaml](#config)

```bash
# Usage: sublr open [OPTIONS] [PORT]
$ sublr open
[INFO] SUBLIME-REMOTE: opened http://12.345.678.910:8888
```

---

<a name='current'></a>

##### CURRENT

```bash
# Usage: sublr current [OPTIONS]
$ sublr current
[INFO] SUBLIME-REMOTE: < cpu >
```

---

<a name='list'></a>

##### LIST

```bash
# Usage: sublr list [OPTIONS]
$ sublr list
[INFO] SUBLIME-REMOTE: AVAILABLE REMOTES:
[INFO] SUBLIME-REMOTE:    * cpu
[INFO] SUBLIME-REMOTE:    * gpu
```

---

<a name='remove'></a>

##### REMOVE

```bash
# Usage: sublr remove [OPTIONS] IDENT
$ sublr remove gpu
[INFO] SUBLIME-REMOTE: < gpu > removed

$ sublr list
[INFO] SUBLIME-REMOTE: AVAILABLE REMOTES:
[INFO] SUBLIME-REMOTE:    * cpu
```

---

<a name='config'></a>

##### CONFIG

Create custom default sublr config-values. Values can be updated directly through CLI, or you can edit the generated config file `sublr.config.yaml` directly.

- PORT: default sublr port (defaults to 8888)
- NOISY: default noisy option (defaults to True)
- REMOTE_PATH: defalut remote_path value (defaults to '')
- AUTO_INIT: default auto-init (defaults to true)

```bash
# Usage: sublr config [OPTIONS] [PORT] [REMOTE_PATH] [NOISY] [AUTO_INIT]
$ sublr config 8999
[INFO] SUBLIME-REMOTE: sublr.config.yaml created. edit file to change configuration

$ cat sublr.config.yaml 
# sublr: config
auto_init: true
noisy: true
port: 8999
remote_path: ''

$ sublr open
[INFO] SUBLIME-REMOTE: opened http://12.345.678.910:8999
```




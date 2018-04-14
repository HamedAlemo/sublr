##### SUBLIME REMOTE: A companion to SublimeSFTP

__CLI for managing multiple SublimeSFTP multiple config files__

[SUBLIME-SFTP](https://wbond.net/sublime_packages/sftp) makes it easy to sync your local Sublime with a remote instance. Often one needs multiple machines, for instance a CPU for initial development and GPU for training. Sublime-Remote is a CLI to makes that easy.

---

##### CLI

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

#### CREATE

```bash
# Usage: sublr create [OPTIONS] IDENT IP [REMOTE_PATH] [AUTO_INIT]
```

---

<a name='init'></a>

#### INIT

```bash
# Usage: sublr init [OPTIONS] IDENT
```
---

<a name='off'></a>

#### OFF

```bash
# Usage: sublr off [OPTIONS]
```

---

<a name='open'></a>

#### OPEN

```bash
# Usage: sublr open [OPTIONS] [PORT]
```

---

<a name='current'></a>

#### CURRENT

```bash
# Usage: sublr current [OPTIONS]
```

---

<a name='list'></a>

#### LIST

```bash
# Usage: sublr list [OPTIONS]
```

---

<a name='remove'></a>

#### REMOVE

```bash
# Usage: sublr remove [OPTIONS] IDENT
```

---

<a name='config'></a>

#### CONFIG

```bash
# Usage: sublr config [OPTIONS] [PORT] [REMOTE_PATH] [NOISY] [AUTO_INIT]
```




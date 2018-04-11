from __future__ import print_function
import os
import re
import json
import webbrowser as web
import sublr.config as c
import click
from shutil import copyfile, move


@click.group()
@click.option(
    '--noisy',
    default=c.NOSIY,
    help='print info and warning messages')
@click.pass_context
def cli(ctx,noisy):
    ctx.obj={}
    ctx.obj['noisy']=_is_true(noisy)


@click.command()
@click.pass_context
def off(ctx):
    try:
        os.remove(c.CONFIG_PATH)
    except OSError:
        _print(c.NOT_ON,ctx.obj['noisy'],level="WARN")


@click.command()
@click.argument('ident')
@click.pass_context
def remove(ctx,ident):
    file=c.REMOTE_CONFIG_PATH_TMPL.format(ident)
    try:
        os.remove(file)
    except OSError:
        _print(
            c.FILE_DOES_NOT_EXIST.format(file),
            ctx.obj['noisy'],
            level="WARN")


@click.command()
@click.argument('ident')
@click.pass_context
def on(ctx,ident):
    file=c.REMOTE_CONFIG_PATH_TMPL.format(ident)
    if os.path.exists(file):
        try:
            move(c.CONFIG_PATH,c.BAK_CONFIG_PATH)
            copyfile(file, c.CONFIG_PATH)
            _print(c.ON_TMPL.format(ident),ctx.obj['noisy'])
        except OSError:
            pass
    else:
        _print(c.FILE_DOES_NOT_EXIST.format(file),True,level="ERROR")  


@click.command()
@click.argument('port',default=c.DEFAULT_PORT)
@click.pass_context
def go(ctx,port=c.DEFAULT_PORT):
    with open(c.CONFIG_PATH, 'r') as f:
        cnfg=json.load(f)
    url=c.URL_TMPL.format(cnfg['host'],port)
    web.open_new_tab(url)
    _print(c.OPENED_TMPL.format(url),ctx.obj['noisy'])



@click.command()
@click.pass_context
def who(ctx):
    try:
        with open(c.CONFIG_PATH, 'r') as f:
            cnfg=json.load(f)
        _print(c.WHO_TMPL.format(cnfg.get('sublr','unknown')),True)
    except IOError:
         _print(c.SUBL_OFF,True)



@click.command()
@click.argument('ident')
@click.argument('ip')
@click.argument('remote_path',default=c.REMOTE_PATH)
@click.pass_context
def init(ctx,ident,ip,remote_path=c.REMOTE_PATH,auto_on=c.AUTO_ON):
    cnfg=c.CONFIG_DICT.copy()
    cnfg['host']=ip
    cnfg['remote_path']=remote_path
    cnfg['sublr']=ident
    file=c.REMOTE_CONFIG_PATH_TMPL.format(ident)
    with open(file, 'w') as f:
        json.dump(cnfg,f,indent=4,sort_keys=True)
    # TODO: refactor to move separate logic and click interface
    # "on" method repeated below to avoid `ctx.invoke`
    if os.path.exists(file):
        try:
            try:
                move(c.CONFIG_PATH,c.BAK_CONFIG_PATH)
            except IOError:
                _print(c.INITIAL_CONFIG,True)
            copyfile(file, c.CONFIG_PATH)
            _print(c.ON_TMPL.format(ident),ctx.obj['noisy'])
        except OSError:
            pass
    else:
        _print(c.FILE_DOES_NOT_EXIST.format(file),True,level="ERROR")  




#
# HELPERS
#
def _print(msg,noisy,level='INFO'):
    if noisy:
        print("[{}] SUBLIME-REMOTE: {}".format(level,msg))


def _is_true(b):
    if isinstance(b,str) or isinstance(b,unicode):
        return b.lower()!="false"
    else:
        return b




#
# MAIN
#
cli.add_command(on)
cli.add_command(off)
cli.add_command(init)
cli.add_command(who)
cli.add_command(go)
cli.add_command(remove)

if __name__ == '__main__':
    cli()

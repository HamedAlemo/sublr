from __future__ import print_function
import os
import re
import json
import webbrowser as web
import click
from shutil import copyfile, move
import sublr.core as core
import sublr.config as c



#
# PUBLIC
#
@click.group()
@click.option(
    '--noisy',
    default=c.NOISY,
    help='print info and warning messages')
@click.pass_context
def cli(ctx,noisy):
    ctx.obj={}
    ctx.obj['noisy']=_is_true(noisy)


@click.command(help='turn off sublr')
@click.pass_context
def off(ctx):
    core.off(noisy=ctx.obj['noisy'])


@click.command(help='remove sftp-config for ident')
@click.argument('ident')
@click.pass_context
def remove(ctx,ident):
    core.remove(ident,noisy=ctx.obj['noisy'])


@click.command(help='initialize a new sftp-config')
@click.argument('ident')
@click.pass_context
def init(ctx,ident):
    core.init(ident,noisy=ctx.obj['noisy'])  


@click.command(name='open',help='open current port for the current remote')
@click.argument('port',default=c.DEFAULT_PORT)
@click.pass_context
def open_port(ctx,port=c.DEFAULT_PORT):
    core.open_port(port,noisy=ctx.obj['noisy'])


@click.command(help='print current remote ident')
@click.pass_context
def current(ctx):
    core.current()


@click.command(help='create and initalize new remote config')
@click.argument('ident')
@click.argument('ip')
@click.argument('remote_path',default=c.REMOTE_PATH)
@click.argument('auto_on',default=c.AUTO_ON)
@click.pass_context
def create(ctx,ident,ip,remote_path=c.REMOTE_PATH,auto_on=c.AUTO_ON):
    core.create(ident,ip,remote_path,auto_on)


@click.command(name='list',help='list available remote configs')
def list_remotes():
    core.list_remotes()


#
# INTERNAL
#
def _is_true(b):
    if isinstance(b,str) or isinstance(b,unicode):
        return b.lower()!="false"
    else:
        return b


#
# MAIN
#
cli.add_command(init)
cli.add_command(off)
cli.add_command(create)
cli.add_command(current)
cli.add_command(open_port)
cli.add_command(list_remotes)
cli.add_command(remove)


if __name__ == '__main__':
    cli()

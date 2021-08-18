#!/usr/bin/env python

from hello import addthis
import click
import sys

@click.command()
@click.option('--x', required = True, type = int, help="First number to add")
@click.option('--y', required = True, type = int, help="Second number to add")
def calladdthis(x, y):
    ''' This is a CLI that add x and y
    '''
    result = addthis(x, y)
    click.echo(click.style(f'{result}', bg='red'))
    #click.echo(click.style(f'{result}', bg='green')) 

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    calladdthis()
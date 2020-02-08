import os
import click
from ..core.rawdata import RawData
from ..core.rankings import Rankings
from . import util


CACHE_BASE = os.path.join(os.environ['HOME'], '.tickercache')


@click.group()
def main():
    pass


@main.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def chart(ticker):
    data = RawData(CACHE_BASE).chart(ticker)
    util.out.json(data)


@main.command()
@click.option('--ticker', required=True, type=str, callback=util.ensure_valid_ticker)
def summary(ticker):
    data = RawData(CACHE_BASE).summary(ticker)
    util.out.json(data)


@main.group()
def rank():
    pass


@rank.command()
def pe():
    data = Rankings(cache_base=CACHE_BASE).pe()
    util.out.json(data)


@rank.command()
def peg():
    data = Rankings(cache_base=CACHE_BASE).peg()
    util.out.json(data)


@rank.command()
def growth():
    data = Rankings(cache_base=CACHE_BASE).growth()
    util.out.json(data)
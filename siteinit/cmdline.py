from argparse import ArgumentParser
from shutil import copytree

from .settings import SITE_ROOT

def init(args):
	src = SITE_ROOT
	dest = args.sitepath
	copytree(src, dest)
	print "init'd!"

parser = ArgumentParser()
parser.set_defaults(func=init)
parser.set_defaults(sitepath='site-init')
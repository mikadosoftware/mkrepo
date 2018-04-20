#! -*- coding:utf-8 -*-
"""
Designed to mkae simplified repo framework
I suspect I will be making a lot of them

There are 2 kinds of repo I suspect

* a microservice - that expects to have dockerfiles, jenkins etc
* a developer (CLI) tool - probably just something like todoinator. Does one thing. Adequately.
  Will be just the README and help file in the one module I suspect.
  Needs a deploy means in setup

# TODO: idempotent - can be run over any dir, and will create only missing parts

"""
from docopt import docopt
import shutil
import os

DOCOPT = """Make a repo for python

Usage:
    mkrepo.py <pkgname> <rootdir> [--cli]
    mkrepo.py (-h | --help)
    mkrepo.py (-t | --test)
 
Options:
    -h --help     Show this screen
    -t --test     Run tests  
    --cli         Create repo suitable for cli tool not micro-web-service

"""

def mk_dir_cli():
    dirs = []
    files = ['version', 'setup.py', '.gitignore']

def mk_dir_uservice():
    dirs = []
    files = ['setup.py',]

def get_template(templatename):
    # read from our location
    with open(os.path.join(THISDIR, 'templates', templatename), encoding="utf-8") as fo:
        template = fo.read()
    return template

def write_file(filename, text):
    """ """
    if not os.path.isabs(filename):
        pth = os.path.join(ROOTDIR, filename)
    else:
        pth = filename
    with open(pth, 'w', encoding="utf-8") as fo:
        fo.write(text)
        
def mk_dir(rootdir):
    """If not existing, create rootdir

    >>> os.makedirs('/tmp/foo1')
    >>> mk_dir('/tmp/foo1/wibble')
    >>> os.isdir('/tmp/foo1/wibble')
    True
    >>> shutil.rmtree('/tmp/foo1')

    """
    print(rootdir)
    print(PKGNAME)
    
    os.makedirs(rootdir, exist_ok=True)
    os.makedirs(os.path.join(rootdir, PKGNAME), exist_ok=True)
    print(os.path.join(rootdir, PKGNAME, '__init__.py'))
    write_file(os.path.join(rootdir, PKGNAME, '__init__.py'), '')
    
##############################################################

def mk_setup(pkgname):
    template = get_template('setup.py')
    text = template.format(pkgname=pkgname)
    write_file('setup.py', text)

def mk_version():
    write_file('VERSION', '0.0.0')
    
def mk_license():
    template = get_template('LICENSE')
    write_file('LICENSE', template)

def mk_authors():
    write_file('AUTHORS', 'Paul Brian <paul@mikadosoftware.com>')

def mk_contributing():
    template = get_template('CONTRIBUTING')
    write_file('CONTRIBUTING', template)

def mk_dockerfile():
    write_file('Dockerfile', 'FROM ubuntu:latest')

def mk_jenkinsfile():
    write_file('Jenkinsfile', 'TBD')

def mk_manifest():
    write_file('MANIFEST.in', 'include LICENSE')

def mk_make():
    write_file('Makefile', 'TBD')
    
def mk_docs():
    os.makedirs(os.path.join(ROOTDIR, 'docs'), exist_ok=True)

def mk_tests():
    os.makedirs(os.path.join(ROOTDIR, 'tests'), exist_ok=True)

def mk_readme():
    write_file('README.rst',
               '{pkgname}\n{underline}\n'.format(pkgname=PKGNAME,
                                                 underline='='*len(PKGNAME)))

def mk_gitignore():
    template = get_template('.gitignore')
    write_file('.gitignore', template)

def mk_requirements():
    write_file('requirements.txt', '# populate as needed')
###############################################################
ROOTDIR = None
PKGNAME = None
THISDIR = None

def run(args):
    global THISDIR, ROOTDIR, PKGNAME
    if args['--test']:
        runtests()
    else:
        PKGNAME = args['<pkgname>']
        parentdir = args['<rootdir>']
        ROOTDIR = os.path.join(parentdir, PKGNAME)
        THISDIR = os.path.dirname(os.path.abspath(__file__))
        doall()
        
def doall():
    mk_dir(ROOTDIR)
    mk_setup(PKGNAME)
    mk_version()
    mk_license()
    mk_authors()
    mk_contributing()
    mk_dockerfile()
    mk_jenkinsfile()
    mk_manifest()
    mk_make()
    mk_readme()
    mk_gitignore()
    mk_requirements()
    mk_docs()
    mk_tests()

def runtests():
    import doctests
    doctests.testmod()

def main():
    args = docopt(DOCOPT)
    run(args)

if __name__ == '__main__':
    main()

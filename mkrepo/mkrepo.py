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
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
log.addHandler(ch)


DOCOPT = """Make a repo for python

Usage:
    mkrepo.py <pkgname> <rootdir> [--dryrun]
    mkrepo.py (-h | --help)
    mkrepo.py (-t | --test)
 
Options:
    -h --help     Show this screen
    -t --test     Run tests  
    --dryrun      Do not actually create files

"""

def mk_dir_cli():
    dirs = []
    files = ['version', 'setup.py', '.gitignore']

def mk_dir_uservice():
    dirs = []
    files = ['setup.py',]

def get_template(templatename):
    # read from our location
    with open(os.path.join(TEMPLATEDIR, templatename), encoding="utf-8") as fo:
        template = fo.read()
    return template

def write_file(filename, text):
    """ """
    if not os.path.isabs(filename):
        pth = os.path.join(ROOTDIR, filename)
    else:
        pth = filename
    if os.path.isfile(pth):
        log.warning("File %s exists - will not overwrite", pth)
    else:
        if DRYRUN:
            log.info("Dry Run - would have written %s", pth)
        else:
            log.info("Writing file %s", pth)
            with open(pth, 'w', encoding="utf-8") as fo:
                fo.write(text)

def dir_maker(dirpath):
    """proxy for os.makedirs"""
    if DRYRUN:
        log.info("Dry Run - would have mkdir %s", dirpath)
    else:
        log.info("Make dir %s", dirpath)
        os.makedirs(dirpath, exist_ok=True)
            
    
def mk_dir(rootdir):
    """If not existing, create rootdir

    >>> os.makedirs('/tmp/foo1')
    >>> mk_dir('/tmp/foo1/wibble')
    >>> os.isdir('/tmp/foo1/wibble')
    True
    >>> shutil.rmtree('/tmp/foo1')

    """
    dir_maker(rootdir)
    dir_maker(os.path.join(rootdir, PKGNAME))
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
    dir_maker(os.path.join(ROOTDIR, 'docs'))

def mk_tests():
    dir_maker(os.path.join(ROOTDIR, 'tests'))

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
TEMPLATEDIR = None
DRYRUN = False

def run(args):
    global TEMPLATEDIR, ROOTDIR, PKGNAME, DRYRUN
    if args['--test']:
        runtests()
    else:
        DRYRUN = args['--dryrun']
        PKGNAME = args['<pkgname>'].lower()
        pkgtitle = PKGNAME.title()
        parentdir = args['<rootdir>']
        ROOTDIR = os.path.abspath(os.path.join(parentdir, pkgtitle))
        TEMPLATEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   'templates')
        print(f"ROOTDIR {ROOTDIR} \nPKGNAME {PKGNAME} \nTEMPLATEDIR {TEMPLATEDIR}")
        
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

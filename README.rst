mkrepo
======

To generate a new skeleton repo / pkg

   python3 mkrepo.py <pkgname> <rootdir>

Some conventions
----------------

I find that a lot of *developer tools* are command line based, and
just useful to have as little scripts.

There are 2 main approaches to providing command line tools via python
pacakges, the 'entrypoint' and the 'script'.  The entrypoint approach
is *fine*. It basically drops a little script into your PATH that imports
some code form setuputils and then says 'run the function X in package Y'

The script appraoch is simpler - no indirection, and is literally a script
you write - I prefer now to make this a little docopt script that imports
the (library) and does one little thing.  todoinator is a fairly good example.

::
   
  $ echo $PATH
  /home/pbrian/venvs/mikadolib/bin:/usr/local/bin:/usr/local/sbin:
               ^^^^^^^^^^^^^^^^^^^^    
  The venv is use for "general work" is first on my path, thanks to
  setup.py

	       


* SOme hints
Writing clean code (distilled form Uncle Bob)

https://github.com/zedr/clean-code-python


How to monitor code quality automatically and manually
------------------------------------------------------

WE have two sets of code quality measures - the automat*able* part,
that is represented by code linting and testing.

Why do we test?  For *one* reason - to ensure we have not regressed -
made changes that break things that previously were working.  This is
important.

I am not a huge fan of the TDD movement.  It is important to write
tests, yes.  But to design by writing tests is like


PyLint
------

Pylint is both *great* and *annoying*.

::

   pylint --list-msgs

   Will output a complete list of the messages it checks for and the rationales.

   pylint --generate-rcfile

   A good starting point.


https://github.com/zedr/clean-code-python


How to monitor code quality automatically and manually
------------------------------------------------------

WE have two sets of code quality measures - the automat*able* part,
that is represented by code linting and testing.

Why do we test?  For *one* reason - to ensure we have not regressed -
made changes that break things that previously were working.  This is
important.

I am not a huge fan of the TDD movement.  It is important to write
tests, yes.  But to design by writing tests is like


PyLint
------

Pylint is both *great* and *annoying*.

::

   pylint --list-msgs

   Will output a complete list of the messages it checks for and the rationales.

   pylint --generate-rcfile

   A good starting point.



https://github.com/zedr/clean-code-python


How to monitor code quality automatically and manually
------------------------------------------------------

WE have two sets of code quality measures - the automat*able* part,
that is represented by code linting and testing.

Why do we test?  For *one* reason - to ensure we have not regressed -
made changes that break things that previously were working.  This is
important.

I am not a huge fan of the TDD movement.  It is important to write
tests, yes.  But to design by writing tests is like


PyLint
------

Pylint is both *great* and *annoying*.

::

   pylint --list-msgs

   Will output a complete list of the messages it checks for and the rationales.

   pylint --generate-rcfile

   A good starting point but we want to 

   
   $ pylint --list-msgs | cut -d " " -f 1 | grep . | sed 's/://g' | sort

We then adjust the .pylintrc to have the complete set of messages, and
we selectively disable some.  mkrepo uses a fairly reasonable
default - trying ofr the Goldilocks zone of not too much not too
little


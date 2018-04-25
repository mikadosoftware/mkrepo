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

	       

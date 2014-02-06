Installing
==========

``krunner-vim-sessions`` is written in `Python`_ so it requires PyKDE4.

.. _Python: http://python.org/

You can get the source code from the Mercurial repository or, a ready to
install, packaged version from `downloads.mornie.org/krunner-vim-sessions`_.

.. _downloads.mornie.org/krunner-vim-sessions: http://downloads.mornie.org/krunner-vim-sessions/


From the Mercurial repository
-----------------------------

1. Clone ``krunner-vim-sessions`` repository.
   For example, if you want to install version 0.1 you have to do::

    $ hg clone -r 0.1 http://hg.mornie.org/krunner-vim-sessions

2. Install using the provided ``Makefile``.

   ::

    $ make install


From a packaged version
-----------------------

1. Download the package from `downloads.mornie.org/krunner-vim-sessions`_.
   For example, if you want to install version 0.1::

    $ wget http://downloads.mornie.org/krunner-vim-sessions/krunner-vim-sessions-0.1.tar.gz

2. Once downloaded the tarball you have to do::

    $ tar zxf krunner-vim-sessions-0.1.tar.gz
    $ cd krunner-vim-sessions-0.1/
    $ make install

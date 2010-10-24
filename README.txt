Introduction
============
Torii allow the access to a running zope server over a unix-domain-socket. Torii make
also possible to run scripts from the command line to the server. In addition it's provide a python-
prompt connected to the zope-server. It means the full access of the Zope and ZODB at the runtime.

This additional package make the interface to plone. It provides some scripts, a global 
variable 'plone' and set the siteManager(access to persistence zope.components ) at the startup

Use it with buildout::

    [torii]
    recipe = raptus.recipe.torii
    socket-path = ${buildout:directory}/var/torii.sock
    threaded = True
    extends =
        raptus.torii.plone


`more information at raptus.torii <http://pypi.python.org/pypi/raptus.torii>`_

Copyright and credits
=====================

raptus.torii is copyright 2010 by raptus_ , and is licensed under the GPL. 
See LICENSE.txt for details.

.. _raptus: http://www.raptus.ch/ 
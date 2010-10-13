import os
import logging
from zope.app import publication
from zope import site

_params = None
def initialize(params):
    # someone know a better way as this?
    from raptus.torii import plone as self
    self._params = params


def getPlone():
    plone = app
    plone_location = _params.get('plone-location', None)
    if plone_location:
        for i in plone_location.split('.'):
            plone = getattr(plone, i, None)
            if plone is None:
                break
    else:
        plone = None

    
    """ set a event for the plone siteManager inside the running 
        torii-thread. This way we can use the full component
        architecture on the given plone instance.
        more info --> zope/site/site.txt
    """
    if plone is not None:
        ev = publication.interfaces.BeforeTraverseEvent(plone, plone.REQUEST)
        site.threadSiteSubscriber(plone, ev)
    else:
        logging.warning('plone-location is not correctly setted')
    return plone


scripts = dict(rebuild_catalogs='%s/scripts/rebuild_catalogs.py' % os.path.dirname(__file__),
               quickinstall='%s/scripts/quickinstall.py' % os.path.dirname(__file__))

properties = dict(plone=getPlone)
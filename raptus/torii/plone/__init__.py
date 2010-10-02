import os

_params = None
def initialize(params):
    # someone know a better way as this?
    from raptus.torii import plone as self
    self._params = params

def getPlone():
    temp = app
    plone = _params.get('plone-location', None)
    if plone:
        for i in plone.split('.'):
            temp = getattr(temp, i)
        return temp
    return None


scripts = dict(rebuild_catalogs='%s/scripts/rebuild_catalogs.py' % os.path.dirname(__file__),
               quickinstall='%s/scripts/quickinstall.py' % os.path.dirname(__file__))

properties = dict(plone=getPlone)
import transaction

plone.portal_catalog.refreshCatalog()

transaction.commit()
print 'done'
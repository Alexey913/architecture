import zope.interface


class IModelChanger(zope.interface.Interface):

    def notife_change(sender):
        ...
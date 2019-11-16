# -*- coding: utf-8 -*-
import info

class subinfo(info.infoclass):
    def setTargets(self):
        ver = '5.25'
        self.targets[ver] = 'yaz-%s-lib-win64.zip' % ver
        self.targetInstSrc[ver] = 'yaz-'+ver
        self.targetDigests[ver] = 'ad1d92db2eba69f9200c233743f280010cb11e21'
        self.description = 'yaz'
        self.defaultTarget = ver

from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)

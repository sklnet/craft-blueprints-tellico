# -*- coding: utf-8 -*-
import info

class subinfo(info.infoclass):
    def setTargets(self):
        ver = '5.25.0'
        self.targets[ver] = 'https://github.com/sklnet/craft-blueprints-tellico/raw/master/libs/yaz/yaz-%s-lib-win64.zip' % ver
        self.targetInstSrc[ver] = 'yaz-'+ver
        self.targetDigests[ver] = '0f00b41e61de47a19ee616baa3e62e7d2c8d649c'
        self.description = 'yaz'
        self.defaultTarget = ver

from Package.BinaryPackageBase import *

class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)
        self.subinfo.options.package.withCompiler = False
        self.subinfo.options.package.withSources = False

    def unpack(self):
        if not BinaryPackageBase.unpack(self): return False
        return True

    def install(self):
        if not os.path.isdir(os.path.join(self.installDir(), "bin")):
            os.makedirs(os.path.join(self.installDir(), "bin"))
        shutil.copy(os.path.join(self.sourceDir(), "bin", "*"),os.path.join(self.installDir(), "bin"))
					
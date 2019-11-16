import info

class subinfo(info.infoclass):
    def setTargets(self):
        ver = "2.4.5"
        self.targets[ver] = f"https://libopenraw.freedesktop.org/download/exempi-{ver}.tar.bz2"
        self.targetInstSrc[ver] = 'exempi-'+ver
        self.targetDigests[ver] = ("9e22935ab834f556a3e9e00c3a871a773dc08db9")
        self.defaultTarget = ver
    def setDependencies(self):
        self.buildDependencies["libs/boost/boost-headers"] = None

from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        self.subinfo.options.configure.args = ""
        self.subinfo.options.configure.autoreconf = False

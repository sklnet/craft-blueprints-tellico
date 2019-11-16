import info

class subinfo(info.infoclass):
    def setTargets(self):
        ver = "3.0.3"
        self.targets[ver] = f"https://downloads.sourceforge.net/project/libcsv/libcsv/libcsv-{ver}/libcsv-{ver}.tar.gz"
        self.targetInstSrc[ver] = 'libcsv-'+ver
        self.targetDigests[ver] = ("2f637343c3dfac80559595f519e8f78f25acc7c1")
        self.defaultTarget = ver


from Package.AutoToolsPackageBase import *

class Package(AutoToolsPackageBase):
    def __init__(self, **args):
        AutoToolsPackageBase.__init__(self)
        self.subinfo.options.configure.args = ""
        self.subinfo.options.configure.autoreconf = False

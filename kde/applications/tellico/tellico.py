import info


class subinfo(info.infoclass):
    def setTargets(self):
        ver = "3.3.1"
        self.targets[ver] = f"http://tellico-project.org/files/tellico-{ver}.tar.xz"
        self.targetInstSrc[ver] = 'tellico-'+ver
        self.targetDigests[ver] = ("6b02d44d3107d29f7c71b9b01d45d8a5736d6959")
        self.description = "tellico"
        self.defaultTarget = ver

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcodecs"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kcompletion"] = None
        self.runtimeDependencies["kde/frameworks/tier3/khtml"] = None
        self.runtimeDependencies["kde/frameworks/tier2/kfilemetadata"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kitemmodels"] = None
        self.runtimeDependencies["kde/frameworks/tier3/knewstuff"] = None
        self.runtimeDependencies["qt-libs/poppler"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["libs/yaz"] = None
        self.buildDependencies["dev-utils/png2ico"] = None
        self.buildDependencies["libs/libcsv"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args = "-DENABLE_CDTEXT=FALSE -DBUILD_TESTS=FALSE"
        self.defines["shortcuts"] = [{"name" : "tellico", "target":"bin/tellico.exe", "description" : self.subinfo.description}]
        self.defines["icon"] = os.path.join(self.packageDir(), "tellico.ico")
        self.defines["icon_png"] = os.path.join(self.sourceDir(), "icons", "128-apps-tellico.png")
        self.defines["file_types"] = [".tc"]

import os
from conans import ConanFile, CMake
from conans.tools import download, unzip

class Eigen3Conan(ConanFile):
    name = "Eigen3"
    version = "3.2.8"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports = ["FindEigen3.cmake"]
    url="http://github.com/bilke/conan-eigen3"
    license="http://eigen.tuxfamily.org/index.php?title=Main_Page#License"

    ZIP_FOLDER_NAME = "%s" % version

    def source(self):
        zip_name = self.ZIP_FOLDER_NAME + ".zip"
        download("http://bitbucket.org/eigen/eigen/get/%s" % zip_name , zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def config(self):
        self.settings.remove("compiler")
        self.settings.remove("os")
        self.settings.remove("arch")
        self.settings.remove("build_type")
        self.options.remove("shared")

    def build(self):
        return

    def package(self):
        self.copy("FindEigen3.cmake", ".", ".")
        self.copy("*", dst="Eigen", src="eigen-eigen-07105f7124f9/Eigen")

    def package_info(self):
        self.cpp_info.includedirs = ['.']

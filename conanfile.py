import os
from conans import ConanFile
from conans.tools import download, unzip

class Eigen3Conan(ConanFile):
    name = "Eigen3"
    description = "Eigen is a C++ template library for linear algebra"
    version = "3.2.10"
    generators = "cmake"
    exports = ["FindEigen3.cmake"]
    url="http://github.com/bilke/conan-eigen3"
    license="http://eigen.tuxfamily.org/index.php?title=Main_Page#License"

    def conan_info(self):
        self.info.requires.clear()
        self.info.settings.clear()

    def source(self):
        zip_name = "%s.zip" % self.version
        download("http://bitbucket.org/eigen/eigen/get/%s" % zip_name , zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def config(self):
        self.options.remove("shared")

    def build(self):
        return

    def package(self):
        self.copy("FindEigen3.cmake", ".", ".")
        self.copy("*", dst="Eigen", src="eigen-eigen-dc6cfdf9bcec/Eigen")
        self.copy("*", dst="unsupported", src="eigen-eigen-dc6cfdf9bcec/unsupported")

    def package_info(self):
        self.cpp_info.includedirs = ['.', './unsupported']

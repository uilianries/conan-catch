"""Conan recipe for Catch
"""
from conans import ConanFile
from conans.tools import download
from conans.tools import check_md5


class CatchConan(ConanFile):
    """Download Catch Cpp, build and create package
    """
    name = "Catch"
    version = "1.9.6"
    generators = "cmake"
    url = "https://github.com/uilianries/conan-catch"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "Boost"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD"

    def source(self):
        header_name = "catch.hpp"
        download("https://github.com/philsquared/Catch/releases/download/v%s/%s" % (self.version, header_name), header_name)
        check_md5(header_name, "6e3c2c7dd06d31ae9112b3816da24712")

    def package(self):
        self.copy(pattern="catch.hpp", dst="include")

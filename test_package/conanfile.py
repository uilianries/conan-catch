"""Recipe validation for Catch-1.9.4
"""
from os import environ
from os import getenv
from conans import ConanFile, CMake


class TestCatchConan(ConanFile):
    """Build test using target package and execute all tests
    """
    target = "Catch"
    name = "%s-test" % target
    version = "1.9.4"
    author = "Uilian Ries <uilianries@gmail.com>"
    license = "Boost"
    settings = "os", "compiler", "build_type", "arch"
    channel = getenv("CONAN_CHANNEL", "testing")
    user = getenv("CONAN_USERNAME", "uilianries")
    requires = "%s/%s@%s/%s" % (target, version, user, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.build()

    def test(self):
        cmake = CMake(self)
        cmake.configure(build_dir="./")
        cmake.test()

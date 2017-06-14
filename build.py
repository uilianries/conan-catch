"""This script build Conan.io package to multiple platforms."""
from os import getenv
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    mingw_configurations = [("6.3", "x86_64", "seh", "posix"),
                            ("6.3", "x86_64", "sjlj", "posix"),
                            ("6.3", "x86", "sjlj", "posix"),
                            ("6.3", "x86", "dwarf2", "posix")]
    builder = ConanMultiPackager(mingw_configurations=mingw_configurations)
    builder.password = getenv("CONAN_PASSWORD")
    builder.add_common_builds(pure_c=False)
    builder.run()

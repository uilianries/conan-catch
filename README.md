[![Build Status](https://travis-ci.org/uilianries/conan-catch.svg?branch=release/1.9.2)](https://travis-ci.org/uilianries/conan-catch) [![Build status](https://ci.appveyor.com/api/projects/status/wnf26emviga6pal0/branch/release/1.9.2?svg=true)](https://ci.appveyor.com/project/uilianries/conan-catch/branch/release/1.9.2) [![badge](https://img.shields.io/badge/conan.io-Catch%2F1.9.2-green.svg?logo=data:image/png;base64%2CiVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAA1VBMVEUAAABhlctjlstkl8tlmMtlmMxlmcxmmcxnmsxpnMxpnM1qnc1sn85voM91oM11oc1xotB2oc56pNF6pNJ2ptJ8ptJ8ptN9ptN8p9N5qNJ9p9N9p9R8qtOBqdSAqtOAqtR%2BrNSCrNJ/rdWDrNWCsNWCsNaJs9eLs9iRvNuVvdyVv9yXwd2Zwt6axN6dxt%2Bfx%2BChyeGiyuGjyuCjyuGly%2BGlzOKmzOGozuKoz%2BKqz%2BOq0OOv1OWw1OWw1eWx1eWy1uay1%2Baz1%2Baz1%2Bez2Oe02Oe12ee22ujUGwH3AAAAAXRSTlMAQObYZgAAAAFiS0dEAIgFHUgAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfgBQkREyOxFIh/AAAAiklEQVQI12NgAAMbOwY4sLZ2NtQ1coVKWNvoc/Eq8XDr2wB5Ig62ekza9vaOqpK2TpoMzOxaFtwqZua2Bm4makIM7OzMAjoaCqYuxooSUqJALjs7o4yVpbowvzSUy87KqSwmxQfnsrPISyFzWeWAXCkpMaBVIC4bmCsOdgiUKwh3JojLgAQ4ZCE0AMm2D29tZwe6AAAAAElFTkSuQmCC)](http://www.conan.io/source/Catch/1.9.2/uilianries/stable) [![License: Boost](https://img.shields.io/badge/License-Boost%201.0-blue.svg)](https://github.com/philsquared/Catch/blob/master/LICENSE.txt)  [ ![Download](https://api.bintray.com/packages/uilianries/conan/Catch/images/download.svg?version=1.9.2%3Astable) ](https://bintray.com/uilianries/conan/Catch/1.9.2%3Astable/link)

# A modern, C++-native, header-only, framework for unit-tests, TDD and BDD

[Conan.io](https://conan.io) package for [Catch](https://github.com/philsquared/Catch) project

The packages generated with this **conanfile** can be found in [conan.io](https://bintray.com/uilianries/conan/Catch/1.9.2%3Astable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Add remote

Add Conan remote from bintray account

    $ conan remote add bintray https://api.bintray.com/conan/uilianries/conan

## Upload packages to server

    $ conan upload Catch/1.9.2@uilianries/stable --all

## Reuse the packages

### Basic setup

    $ conan install Catch/1.9.2@uilianries/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Catch/1.9.2@uilianries/stable

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

### License
[Boost](LICENSE)

cmake_minimum_required(VERSION 2.8)
project(catch-test CXX)

# Conan ########################################################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake) 
conan_basic_setup()

# Source files #################################################################
file(GLOB SOURCE_FILES src/*.cpp)

# Build application ############################################################
add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})

# Add Tests ####################################################################
enable_testing()
add_test(NAME test-all 
    COMMAND ${CMAKE_PROJECT_NAME}
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

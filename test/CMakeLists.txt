project(MyEigen3)
cmake_minimum_required(VERSION 2.8.12)

include(conanbuildinfo.cmake)

#conan_basic_setup()

#set(CMAKE_RUNTIME_OUTPUT_DIRECTORY bin)
#message("${CONAN_CMAKE_MODULE_PATH}")
set(CMAKE_MODULE_PATH ${CONAN_CMAKE_MODULE_PATH} ${CMAKE_MODULE_PATH})
find_package(Eigen3 REQUIRED)

include_directories(
	.
	${CONAN_INCLUDE_DIRS_EIGEN3}
)
add_executable(test eigentest.cpp)

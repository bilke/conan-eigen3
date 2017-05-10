find_path(Eigen3_INCLUDE_DIR NAMES Array
	PATHS ${CONAN_INCLUDE_DIRS_EIGEN3}
	PATH_SUFFIXES Eigen
	NO_DEFAULT_PATH
)

set(Eigen3_FOUND TRUE)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Eigen3 DEFAULT_MSG
	Eigen3_FOUND
	Eigen3_INCLUDE_DIR
)

set(Eigen3_INCLUDE_DIRS ${Eigen3_INCLUDE_DIR})

mark_as_advanced(Eigen3_INCLUDE_DIR)

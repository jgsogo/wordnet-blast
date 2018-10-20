from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "wnb"
    version = "0.6"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "wnb/*", "CMakeLists.txt"

    def requirements(self):
        self.requires("boost/1.68.0@conan/stable")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["wnb"]
#include <iostream>
#include "wnb/core/wordnet.hh"

int main() {
    std::cout << "Testing Conan package for wordnet-blast\n";

    try {
        wnb::wordnet wn("path/to/database/");
    }
    catch(std::runtime_error& e) {
        std::cout << "wordnet database not found :/\n";
    }
    return 0;
}

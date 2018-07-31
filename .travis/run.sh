#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

ls -la
BOOST_ROOT="$(python boost_root.py)"
mkdir build && cd build
cmake .. -DBOOST_ROOT:PATH=$BOOST_ROOT -DBUILD_TESTS:BOOL=ON -DCMAKE_INSTALL_PREFIX:PATH=install
cmake --build . --target install


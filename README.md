

[![Build status](https://ci.appveyor.com/api/projects/status/56yr3dbvm00nl0nt?svg=true)](https://ci.appveyor.com/project/jgsogo/wordnet-blast)
[![Build Status](https://travis-ci.org/jgsogo/wordnet-blast.svg?branch=master)](https://travis-ci.org/jgsogo/wordnet-blast)

WordNet Blast
=============

In memory access to the wordnet onthology.

DEPENDENCIES:

        boost 1.46
        wordnet-sense-index
        colordiff (for wntest)

INSTALL:

        cmake CMakeLists.txt
        make

TESTS: (Beta)

        make check

USAGE:

        #include "wordnet.hh"
        #include "wnb/nltk_similarity.hh"

        using namespace std;
        using namespace wnb;

        int main()
        {
            wordnet wn(PATH_TO_WORDNET);

            vector<synset> synsets1 = wn.get_synsets("cat");
            vector<synset> synsets2 = wn.get_synsets("dog");

            nltk_similarity similarity(wn);
            float d = similarity(synsets1[0], synsets2[0], 6);
        }

BUGS:

 - Word Morphing is sometimes incorrect.

REFERENCE:

George A. Miller (1995). WordNet: A Lexical Database for English.
Communications of the ACM Vol. 38, No. 11: 39-41.

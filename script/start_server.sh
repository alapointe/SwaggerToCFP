#!/usr/bin/sh

pushd /c/Users/Alexandra/stanford-corenlp-full-2018-02-27/stanford-corenlp-full-2018-02-27
java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer \
-serverProperties StanfordCoreNLP-french.properties \
-preload tokenize,ssplit,pos,parse \
-status_port 9004  -port 9004 -timeout 15000
popd
#!/usr/bin/sh

#Todo(JIRA-ALEX) if openapi3 exist, skip

mkdir -p lib
pushd lib
git clone https://github.com/Dorthu/openapi3.git
git checkout 1.8.2
popd
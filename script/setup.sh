#!/usr/bin/sh

python -m venv swaggertocfpenv
source swaggertocfpenv/Scripts/activate

mkdir -p lib
pushd lib
git clone https://github.com/Dorthu/openapi3.git
git checkout 1.8.2
popd

python -m pip install --upgrade pip
pip install -r requirements.txt
python --version
python main.py
to publish

in terminal run
python3 setup.py sdist

then
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

for username use __token__ then password would be an api token from pypi
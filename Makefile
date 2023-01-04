PYTHON   = python3
PIP      = pip3
REPONAME = tatiana

.PHONY: all install-deps check build docs install upload clean
.DEFAULT: all


all: install-deps check build docs
install-deps:
	$(PIP) install -r ./requirements.txt

check:
	flake8 --extend-ignore F401 ./tatiana/
	mypy ./tatiana/

build:
	$(PYTHON) -m build

docs:
	pdoc ./tatiana/ -o ./docs/ --math --logo "https://github.com/soyeltata/tatiana/raw/main/assets/tatiana-logo.png"

clean:
	rm -r dist/
	rm -r tatiana.egg-info/
	rm -r .mypy_cache/
	rm -r docs/*
	touch docs/.gitkeep

install:
	$(PIP) install -e .

upload:
	$(PYTHON) -m twine upload --repository $(REPONAME) dist/*
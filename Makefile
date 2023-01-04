PYTHON   = python3
PIP      = pip3
REPONAME = tatiana

.PHONY: all check build docs install upload clean
.DEFAULT: all


all: check build docs
check:
	flake8 --extend-ignore F401 .
	mypy .

build:
	$(PYTHON) -m build

docs:
	pdoc ./tatiana/ -o ./docs/ --logo "./assets/tatiana-logo.png"

clean:
	rm -r dist/
	rm -r docs/*
	touch docs/.gitkeep

install:
	$(PIP) install -e .

upload:
	$(PYTHON) -m twine upload --repository $(REPONAME) dist/*
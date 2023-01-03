PYTHON   = python3
PIP      = pip3
REPONAME = tatiana

.PHONY: all check build install upload clean
.DEFAULT: all


all: check build
check:
	flake8 --extend-ignore F401 .
	mypy .

build:
	$(PYTHON) -m build

clean:
	rm -r dist/

install:
	$(PIP) install -e .

upload:
	$(PYTHON) -m twine upload --repository $(REPONAME) dist/*
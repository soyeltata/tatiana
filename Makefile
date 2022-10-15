PYTHON   = python3
PIP      = pip3
REPONAME = tatiana

.PHONY: all build install upload clean
.DEFAULT: all


all: build
build:
	$(PYTHON) -m build

clean:
	rm -r dist/

install:
	$(PIP) install -e .

upload:
	$(PYTHON) -m twine upload --repository $(REPONAME) dist/*
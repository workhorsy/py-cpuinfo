
VERSION = 9.0.0

.PHONY: all
all:
	@echo build: Builds the python source dist package
	@echo install: Installs python source dist package
	@echo clean: Removes any generated files
	@echo rst: uses pandoc to generate the README.rst file from README.md
	@echo test: Runs the unit tests

.PHONY: clean-temp-files
clean-temp-files:
	rm -f *.pyc
	rm -f */*.pyc
	rm -f -rf __pycache__
	rm -f -rf */__pycache__
	rm -f -rf py_cpuinfo.egg-info
	rm -f -rf dist
	rm -f -rf build

.PHONY: clean-dist-files
clean-dist-files:
	rm -f -rf py-cpuinfo-$(VERSION)
	rm -f -rf py-cpuinfo-$(VERSION).tar.gz
	rm -f -rf py-cpuinfo-$(VERSION).zip
	rm -f -rf py_cpuinfo-$(VERSION)-py3-none-any.whl

.PHONY: clean
clean: clean-temp-files clean-dist-files

.PHONY: _actual_build
_actual_build:
	python3 setup.py sdist --formats=gztar,zip
	python3 setup.py bdist_wheel

build: clean _actual_build move_built
	$(MAKE) clean-temp-files

.PHONY: move_built
move_built:
	mv dist/py-cpuinfo-$(VERSION).tar.gz py-cpuinfo-$(VERSION).tar.gz
	mv dist/py-cpuinfo-$(VERSION).zip py-cpuinfo-$(VERSION).zip
	mv dist/py_cpuinfo-$(VERSION)-py3-none-any.whl py_cpuinfo-$(VERSION)-py3-none-any.whl

.PHONY: release
release:
	# Create release
	git commit -a -m "Release $(VERSION)"
	git push

	# Create and push tag
	git tag v$(VERSION) -m "Release $(VERSION)"
	git push --tags

.PHONY: upload
upload: clean _actual_build
	twine upload dist/py-cpuinfo-$(VERSION).tar.gz
	twine upload dist/py_cpuinfo-$(VERSION)-py3-none-any.whl

install: remove
	tar xzf py-cpuinfo-$(VERSION).tar.gz
	cd py-cpuinfo-$(VERSION)/ && python3 setup.py install
	rm -f -rf py-cpuinfo-$(VERSION)

	@echo now try "from cpuinfo import get_cpu_info"
	@echo "get_cpu_info()"

remove:
	rm -f -rf /usr/local/lib/python2.7/dist-packages/py_cpuinfo-$(VERSION)-py2.7.egg
	rm -f /usr/local/bin/cpuinfo

test:
	python3 setup.py test

rst:
	rm -f -rf README.rst
	pandoc --from=markdown --to=rst --output=README.rst README.md

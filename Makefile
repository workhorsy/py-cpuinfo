
VERSION = 7.0.0

all:
	@echo build: Builds the python source dist package
	@echo install: Installs python source dist package
	@echo clean: Removes any generated files
	@echo rst: uses pandoc to generate the README.rst file from README.md
	@echo test: Runs the unit tests

clean:
	rm -f *.pyc
	rm -f */*.pyc
	rm -f -rf __pycache__
	rm -f -rf */__pycache__
	rm -f -rf py_cpuinfo.egg-info
	rm -f -rf dist
	rm -f -rf py-cpuinfo-$(VERSION)
	rm -f -rf py-cpuinfo-$(VERSION).tar.gz
	rm -f -rf py-cpuinfo-$(VERSION).zip

build: clean
	python setup.py sdist --formats=gztar,zip
	mv dist/py-cpuinfo-$(VERSION).tar.gz py-cpuinfo-$(VERSION).tar.gz
	mv dist/py-cpuinfo-$(VERSION).zip py-cpuinfo-$(VERSION).zip
	rm -f -rf py_cpuinfo.egg-info
	rm -f -rf dist

release:
	# Create release
	git commit -a -m "Release $(VERSION)"
	git push

	# Create and push tag
	git tag v$(VERSION) -m "Release $(VERSION)"
	git push --tags

upload: clean
	python setup.py sdist --formats=gztar,zip
	twine upload dist/py-cpuinfo-$(VERSION).tar.gz

install: remove
	tar xzf py-cpuinfo-$(VERSION).tar.gz
	cd py-cpuinfo-$(VERSION)/ && python setup.py install
	rm -f -rf py-cpuinfo-$(VERSION)

	@echo now try "import cpuinfo"
	@echo "cpuinfo.get_cpu_info()"

remove:
	rm -f -rf /usr/local/lib/python2.7/dist-packages/py_cpuinfo-$(VERSION)-py2.7.egg
	rm -f /usr/local/bin/cpuinfo

test:
	python setup.py test

rst:
	rm -f -rf README.rst
	pandoc --from=markdown --to=rst --output=README.rst README.md

#!/bin/bash
set -e

echo "Finding OS ..."
homedir=~
OS="unknown"
PYINSTALLER="unknown"
PYTHON2="unknown"
PYTHON3="unknown"
if [[ "$OSTYPE" == "linux"* ]]; then
	OS="linux"
	PYINSTALLER="$homedir/.local/bin/pyinstaller"
	PYTHON2="python2"
	PYTHON3="python3"
elif [ "$OSTYPE" == "msys" ] || [ "$OSTYPE" == "win32" ]; then
	OS="windows"
	PYINSTALLER="pyinstaller"
	PYTHON2="py -2"
	PYTHON3="py -3"
else
	echo "Unknown OS: $OSTYPE"
	exit
fi

echo "Cleanup ..."
rm -rf -f build
rm -rf -f dist
rm -f *.spec
set +e
$PYTHON2 -m pip uninstall PyInstaller -y > /dev/null 2>&1
$PYTHON3 -m pip uninstall PyInstaller -y > /dev/null 2>&1
set -e

echo "Running Python 3 main ..."
$PYTHON3 test_main.py

echo "Running Python 3 NO main ..."
$PYTHON3 test_no_main.py

echo "Running Python 2 main ..."
$PYTHON2 test_main.py

echo "Running Python 2 NO main ..."
$PYTHON2 test_no_main.py

if [[ "$OS" != "windows" ]]; then
	echo "Running Python 2 PyInstaller NO main ..."
	$PYTHON2 -m pip install PyInstaller > /dev/null 2>&1
	$PYINSTALLER --onefile test_no_main.py > /dev/null 2>&1
	cd dist
	./test_no_main
	cd ..
	rm -rf -f build
	rm -rf -f dist
	set +e
	$PYTHON2 -m pip uninstall PyInstaller -y > /dev/null 2>&1
	$PYTHON3 -m pip uninstall PyInstaller -y > /dev/null 2>&1
	set -e
fi

echo "Running Python 2 PyInstaller main ..."
$PYTHON2 -m pip install PyInstaller > /dev/null 2>&1
$PYINSTALLER --onefile test_main.py > /dev/null 2>&1
cd dist
./test_main
cd ..
rm -rf -f build
rm -rf -f dist
set +e
$PYTHON2 -m pip uninstall PyInstaller -y > /dev/null 2>&1
$PYTHON3 -m pip uninstall PyInstaller -y > /dev/null 2>&1
set -e

if [[ "$OS" != "windows" ]]; then
	echo "Running Python 3 PyInstaller NO main ..."
	$PYTHON3 -m pip install PyInstaller > /dev/null 2>&1
	$PYINSTALLER --onefile test_no_main.py > /dev/null 2>&1
	cd dist
	./test_no_main
	cd ..
	rm -rf -f build
	rm -rf -f dist
	set +e
	$PYTHON2 -m pip uninstall PyInstaller -y > /dev/null 2>&1
	$PYTHON3 -m pip uninstall PyInstaller -y > /dev/null 2>&1
	set -e
fi

echo "Running Python 3 PyInstaller main ..."
$PYTHON3 -m pip install PyInstaller > /dev/null 2>&1
$PYINSTALLER --onefile test_main.py > /dev/null 2>&1
cd dist
./test_main
cd ..
rm -rf -f build
rm -rf -f dist
set +e
$PYTHON2 -m pip uninstall PyInstaller -y > /dev/null 2>&1
$PYTHON3 -m pip uninstall PyInstaller -y > /dev/null 2>&1
set -e

echo "Cleanup ..."
rm -rf -f build
rm -rf -f dist
rm -f *.spec
set +e
$PYTHON2 -m pip uninstall PyInstaller -y > /dev/null 2>&1
$PYTHON3 -m pip uninstall PyInstaller -y > /dev/null 2>&1
set -e

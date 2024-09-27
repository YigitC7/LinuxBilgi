python3 -m venv myenv
source myenv/bin/activate

pip install psutil
pip install distro
pip install termcolor
pip install colored

pip install pyinstaller
pyinstaller linuxinfo.py

cp -r dist/linuxinfo linuxinfo
sudo rm -r dist
sudo rm -r build
sudo rm -r myenv
sudo rm -f linuxinfo.spec

sudo g++ start.c -o /usr/local/bin/linuxbilgi
sudo cp -r linuxinfo /usr/local/bin/linuxinfo

echo Derleme işlemi tamamlandı

echo "Başlatmak için 'linuxbilgi' yazın"

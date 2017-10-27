sudo easy_install pip

sudo pip install virtualenv
if [ ! -d ./bin ]; then
  echo "creating virtualenv"
  virtualenv .
fi
source bin/activate

pip install --upgrade pip
pip install -r requirements.txt

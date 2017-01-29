# op je pi eenmalig
sudo apt-get install rsync


# op je computer eenmalig
Installeer NodeJS 7.4.0 https://nodejs.org/en/
Installeer git bash https://git-scm.com/download/win https://git-scm.com/download/mac

ssh-keygen -t rsa
ssh-copy-id pi@192.168.1.100

pip install pep8
cp pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit


# op je computer
./sync IPOMEDT/ pi@192.168.1.100 /home/pi/IPOMEDT
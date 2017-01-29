[![Code Issues](https://www.quantifiedcode.com/api/v1/project/17dda890cb9c4602bc64578f61af5d36/badge.svg)](https://www.quantifiedcode.com/app/project/17dda890cb9c4602bc64578f61af5d36)

[![Issue Count](https://codeclimate.com/github/Owain94/IPOMEDT/badges/issue_count.svg)](https://codeclimate.com/github/Owain94/IPOMEDT)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ead91d30041e46bcbaee89d62f923c36)](https://www.codacy.com/app/Owain94/IPOMEDT?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Owain94/IPOMEDT&amp;utm_campaign=Badge_Grade)


# Raspberry
sudo apt-get install rsync


# Computer
Install [NodeJS 7.4.0][1]

Install git bash [Windows][2], [MacOS][3]

# Setup ssh keys

ssh-keygen -t rsa

ssh-copy-id pi@192.168.1.100

pip install pep8

cp pre-commit .git/hooks/pre-commit

chmod +x .git/hooks/pre-commit


# Rsync watcher
./sync IPOMEDT/ pi@192.168.1.100 /home/pi/IPOMEDT

[1]: https://nodejs.org/en/
[2]: https://git-scm.com/download/win
[3]: https://git-scm.com/download/mac

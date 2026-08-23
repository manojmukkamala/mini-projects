# Raspberry pi:
----------------------------------------------------------------------------------------------------
sudo apt-get update
sudo apt-get upgrade

sudo apt-get update --fix-missing
sudo apt-get upgrade

sudo apt-get remove xrdp vnc4server tightvncserver
sudo apt-get install tightvncserver
sudo apt-get install xrdp

sudo raspi-config
sudo poweroff

sudo apt-get update
sudo apt-get upgrade
sudo shutdown

sudo gpasswd -d pi video
sudo gpasswd -d pi render
sudo raspi-config
----------------------------------------------------------------------------------------------------
sudo apt install -y curl
sudo apt install -y openjdk-8-jdk
sudo apt install -y nano
----------------------------------------------------------------------------------------------------
# Kafka:
curl "https://downloads.apache.org/kafka/3.2.1/kafka_2.13-3.2.1.tgz" -o ~/Downloads/kafka.tgz
mkdir ~/kafka && cd ~/kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1
cd ..
nano .bashrc

# PATH="$PATH:/home/pi/kafka/bin"

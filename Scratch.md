```bash
reboot
sudo apt update && sudo apt upgrade
sudo apt install xrdp
sudo systemctl status xrdp
sudo passwd ubuntu
sudo apt install ubuntu-desktop
sudo adduser xrdp ssl-cert

//rdp speed up tricks settings for ubuntu
gsettings set org.gnome.desktop.interface enable-animations false
sudo sed -i 's/max_bpp=32/max_bpp=16/g' /etc/xrdp/xrdp.ini && sudo reboot

//Install VSCode
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt install code -y
code --version

//Update VSCODE and run
sudo apt update && sudo apt upgrade -y
code


//Set key to environment variables
echo gpt_api_key
export gpt_api_key='sk-<apikey>'
echo $gpt_api_key


```

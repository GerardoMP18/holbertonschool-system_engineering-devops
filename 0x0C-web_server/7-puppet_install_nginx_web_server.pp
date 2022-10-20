# installs Ngnix.
exec { 'ngnix':
  command  => 'sudo apt update && sudo apt install -y nginx && sudo echo 'Hello World' | sudo tee /var/www/html/index.nginx-debian.html && new_string="a location /redirect_me\n \t{ \n\t rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent; \n \t}" && sudo sed -i "/server_name _;/$new_string" /etc/nginx/sites-available/default && sudo service nginx start',
  provider => shell
}

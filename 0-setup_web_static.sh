#!/usr/bin/env bash
# Bash script thta sets up the web servers for deployment of web_static
sudo apt list --installed 2>/dev/null | grep nginx || sudo apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
cat > /data/web_static/releases/test/index.html << EOF

<!DOCTYPE html>
<html>
<head>
</head>
<body>
Holberton School
</body>
</html>

EOF

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart

#!/usr/bin/env bash
#sets up a server for deployment of web_static

apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/releases/shared
echo "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '41i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart

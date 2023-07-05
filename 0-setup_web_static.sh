#!/usr/bin/env bash

# Install Nginx if not already installed
if ! dpkg-query -W -f='${Status}' nginx | grep "installed" >/dev/null; then
    apt-get -y update
    apt-get -y install nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html

# Create symbolic link
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_path="/etc/nginx/sites-available/default"
sed -i '/^\tlocation \/ {/a\\n\t\tlocation /hbnb_static/ {\n\t\t\talias /data/web_static/current/;\n\t\t}' $config_path

# Restart Nginx
service nginx restart


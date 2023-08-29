pkill -f chromium 
pkill -f node
pkill -f npm

cd /home/sotpurk/airport-node/
node index.js &

sleep 5

chromium --app=http://127.0.0.1:3002 --start-fullscreen

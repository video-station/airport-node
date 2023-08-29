pkill -f chromium || exit 0
pkill -f node || exit 0
pkill -f npm || exit 0

cd /home/sotpurk/airport-node/
node index.js &

sleep 5

chromium-browser --app=http://127.0.0.1:3002 --start-fullscreen

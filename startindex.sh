#pkill -f chromium || true
#pkill -f node || true
#pkill -f npm || true

cd /home/sotpurk/airport-node/
node index.js &

sleep 5

chromium-browser --app=http://127.0.0.1:3002 --start-fullscreen

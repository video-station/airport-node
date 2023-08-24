sleep 5
while true; do
tput setaf 3; echo "Starting Node"; tput sgr0
sleep 3

cd /home/sotpurk/airport-node/
node index.js

done &
sleep 3
while true; do
tput setaf 3; echo "Starting Browser"; tput sgr0
sleep 1

chromium --app=http://127.0.0.1:3000 --start-fullscreen


done &


sleep 0.5
while true; do
tput setaf 3; echo "Starting Browser"; tput sgr0
sleep 5

cp /media/usb/airport.xlsx /home/sotpurk/airport-node/data/

done &

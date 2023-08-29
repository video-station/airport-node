# sleep 5
# while true; do
# tput setaf 3; echo "Starting Node"; tput sgr0
# sleep 3

cd /home/sotpurk/airport-node/
node data.js &

sleep 5
# done &
# sleep 10
# while true; do
# tput setaf 3; echo "Starting Browser"; tput sgr0
# sleep 1

chromium-browser --app=http://127.0.0.1:3001 



# done &


# sleep 0.5
# while true; do
# tput setaf 3; echo "Starting Browser"; tput sgr0
# sleep 5

# cp /media/usb/airport.xlsx /home/sotpurk/airport-node/data/

# done &

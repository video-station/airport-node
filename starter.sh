sleep 10
pkill -f bt-agent &
pkill -f bt-obex &

su - sotpurk -c "/usr/bin/bash /home/sotpurk/airport-node/bluerecv.sh" &
#su - sotpurk -c "/usr/bin/bash /home/sotpurk/airport-node/blueagent.sh" &
sleep 3
while true; do
tput setaf 3; echo "Starting Switcher" ; tput sgr0
sleep 3
python3 -u /home/sotpurk/airport-node/switch.py #2>&1 | tee -a /logs/netman.log
done &
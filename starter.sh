sleep 10
pkill -f bt-agent &
pkill -f bt-obex &

su - sotpurk -c "/usr/bin/bash /home/sotpurk/airport-node/bluerecv.sh" &
#su - sotpurk -c "/usr/bin/bash /home/sotpurk/airport-node/blueagent.sh" &

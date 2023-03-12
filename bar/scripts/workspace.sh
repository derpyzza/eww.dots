hyprctl activewindow | awk '/workspace/ && NR>3 && NR<5 { print "("$2")" }' 


# Get Total number of windows in all workspaces and print them :)
hyprctl workspaces | grep 'windows' | tr -d "\n" | tr -d "windows: " | awk '{print "[" $1+$2+$3 "]"}'

# cmd=$(hyprctl activewindow | awk '/class/ && NR>1 {$1=""; print $2 " > "}' | tr -d '\n' && hyprctl activewindow | awk '/title/ && NR>1 {$1=""; print $1 " " $2 " " $3}')

# Get active window
cmd=$(hyprctl activewindow | awk '/title/ && NR>1 {$1=""; print $1 " " $2 " " $3}')

if [[ -z $cmd ]] 
then
	echo "Desktop"
else 
	echo $cmd
fi

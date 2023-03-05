#!/usr/bin/python
#by github.com/derpyzza :)
from subprocess import run
# (defwidget workspaces [] (literal :content workspaces))
#                          │
#                          │
#                          ▼
#                       Box Widget:
#                 ┌────────────────────┐
#                 │  ┌──────────────┐  │
#                 │  │              │─────────► if focused, class = "work_focused"
#                 │  │Button widget │  │          else if occupied class = "work_occupied"
#                 │  └──────────────┘  │          else class = unoccupied.
#                 │                    │          onclick = switch to desktop, set class = work_focused
#                 │  ┌──────────────┐  │
#                 │  │              │  │
#                 │  │ Other Button │  │
#                 │  └──────────────┘  │
#                 │                    │
#                 └────────────────────┘

#returns a string with the output of a command
def run_get(input):
    return run(input, capture_output=True, text=True, shell=True).stdout.replace('\n', ' ').strip()

workspaces = run_get("bspc query -D --names").split()
# Unnecessary. removes extra desktop on my laptop's screen ( i use an external monitor for most of my daily usage )
if workspaces[6] == "Desktop":
    workspaces.remove("Desktop")
focused = run_get("bspc query -D -d focused --names")
occupied = run_get("bspc query -D -d .occupied --names").split()
# Final literal widget string to be outputed.
final = "(box :spacing -5 :orientation \"v\" "

for work in workspaces:
    wk = ''
    ic=''
    if work == focused:
        wk = 'focused'
    else:
        wk = 'unoccupied'
    for o in occupied:
        if work == o and work != focused:
            wk = 'occupied'
            ic=''
    final += "(work :desk \"" + work + "\" :class \""+wk+"\" :icon \""+ic+"\" ) "
final += ")"

print(final)

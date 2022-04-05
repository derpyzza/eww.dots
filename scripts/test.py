#!/usr/bin/python
#by github.com/derpyzza :)

from subprocess import run
from sys import argv as args
import difflib

# comment
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

#for every occupied workspace, return "occupied"
#for every unfocused workspace, return "unoccupied"
#and for the focused workspace, return "focused"

def run_get(input):
    return run(input, capture_output=True, text=True, shell=True).stdout.replace('\n', ' ').strip()

# Workspace array
workspaces = run_get("bspc query -D --names").split()
if workspaces[6] == "Desktop":
    workspaces.remove("Desktop")
focused = run_get("bspc query -D -d focused --names")
# Array
occupied = run_get("bspc query -D -d .occupied --names").split()

for work in workspaces:
    wk = ''
    if work == focused:
        wk = 'focused'
    else:
        wk = 'unoccupied'
    for o in occupied:
        if work == o and work != focused:
            wk = 'occupied'
    print(work+': '+wk)

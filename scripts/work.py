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
def run_get(input):
    return run(input, capture_output=True, text=True, shell=True).stdout.replace('\n', ' ').strip()

workspaces = run_get("bspc query -D --names").split()
if workspaces[6] == "Desktop":
    workspaces.remove("Desktop")
focused = run_get("bspc query -D -d focused --names")
occupied = run_get("bspc query -D -d .occupied --names").split()
final = "(box :orientation \"v\" "

for work in workspaces:
    if work == focused:
        final += "(work :desk \"" + work + "\" :class \"focused\") "
    else:
        final += "(work :desk \"" + work + "\" :class \"unoccupied\") "
final += ")"

print(final)

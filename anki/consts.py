# -*- coding: utf-8 -*-
# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from anki.lang import _

# whether new cards should be mixed with reviews, or shown first or last
NEW_CARDS_DISTRIBUTE = 0
NEW_CARDS_LAST = 1
NEW_CARDS_FIRST = 2

# new card insertion order
NEW_CARDS_RANDOM = 0
NEW_CARDS_DUE = 1

# removal types
REM_CARD = 0
REM_NOTE = 1
REM_DECK = 2

# count display
COUNT_ANSWERED = 0
COUNT_REMAINING = 1

# media log
MEDIA_ADD = 0
MEDIA_REM = 1

# dynamic deck order
DYN_OLDEST = 0
DYN_RANDOM = 1
DYN_SMALLINT = 2
DYN_BIGINT = 3
DYN_LAPSES = 4
DYN_ADDED = 5
DYN_DUE = 6
DYN_REVADDED = 7
DYN_DUEPRIORITY = 8

DYN_MAX_SIZE = 99999

# model types
MODEL_STD = 0
MODEL_CLOZE = 1

STARTING_FACTOR = 2500

# deck schema & syncing vars
SCHEMA_VERSION = 11
SYNC_ZIP_SIZE = int(2.5*1024*1024)
SYNC_ZIP_COUNT = 25
SYNC_BASE = "https://sync%s.ankiweb.net/"
SYNC_VER = 9

HELP_SITE="http://ankisrs.net/docs/manual.html"

### NEW CONSTANTS
# Queue types
QUEUE_SCHED_BURIED = -3
QUEUE_USER_BURIED = -2
QUEUE_SUSPENDED = -1
QUEUE_NEW_CRAM = 0
QUEUE_LRN = 1
QUEUE_REV = 2
QUEUE_DAY_LRN = 3
QUEUE_PREVIEW = 4

# Revlog types
REVLOG_LRN = 0
REVLOG_REV = 1
REVLOG_RELRN = 2
REVLOG_CRAM = 3

# Card types
CARD_NEW = 0
CARD_LRN = 1
CARD_DUE = 2
CARD_FILTERED = 3

# Leech actions
LEECH_SUSPEND = 0
LEECH_TAGONLY = 1

# Buttons
BUTTON_ONE = 1
BUTTON_TWO = 2
BUTTON_THREE = 3
BUTTON_FOUR = 4
### Ends of NEW CONSTANTS

# Labels
##########################################################################

def newCardOrderLabels():
    return {
        0: _("Show new cards in random order"),
        1: _("Show new cards in order added")
        }

def newCardSchedulingLabels():
    return {
        0: _("Mix new cards and reviews"),
        1: _("Show new cards after reviews"),
        2: _("Show new cards before reviews"),
        }

def alignmentLabels():
    return {
        0: _("Center"),
        1: _("Left"),
        2: _("Right"),
        }

def dynOrderLabels():
    return {
        0: _("Oldest seen first"),
        1: _("Random"),
        2: _("Increasing intervals"),
        3: _("Decreasing intervals"),
        4: _("Most lapses"),
        5: _("Order added"),
        6: _("Order due"),
        7: _("Latest added first"),
        8: _("Relative overdueness"),
        }

# colors
colYoung = "#7c7"
colMature = "#070"
colCum = "rgba(0,0,0,0.9)"
colLearn = "#C35617"
colRelearn = "#c00"
colCram = "#ff0"
colIvl = "#077"
colHour = "#ccc"
colTime = "#770"
colUnseen = "#000"
colSusp = "#ff0"
colNew = "#000099"
colRev = "#007700"
colDue = "#007700"
colToday = "red"

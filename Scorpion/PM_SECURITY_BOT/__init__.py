#    scorpion - UserBot

#    Copyright (C) 2021 scorpion

#    This program is free software: you can redistribute it and/or modify

#    it under the terms of the GNU Affero General Public License as published by

#    the Free Software Foundation, either version 3 of the License, or

#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,

#    but WITHOUT ANY WARRANTY; without even the implied warranty of

#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License

#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from scorpion.plugins import OWNER_ID, SCORPION_NAME

import time

from datetime import datetime

from scorpion.scorpionConfig import Var

# start-other disabled

startotherdis = """

Hi there. I am {}'s bot. Nice to see you here.

""".format(SCORPION_NAME)

# start-other enabled

if Var.PMBOT_START_MSSG is None:

    MSSG = """

Hi there, I am {}'s personal bot....

if my master {} ignored DM 😂 Tell me that you want to say to my master..i will tell me😗.

DON'T SPAM HERE......

""".format(SCORPION_NAME)

else:

    MSSG = Var.PMBOT_START_MSSG

startotherena = MSSG

# start-owner

startowner = """

Welcome {}. master😌 THANKS TO DEPLOY ME Now I will protect you from all spammers....✌️

Choose options from below:

""".format(SCORPION_NAME)

# for ping

def get_readable_time(seconds: int) -> str:

    count = 0

    ping_time = ""

    time_list = []

    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:

        count += 1

        if count < 3:

            remainder, result = divmod(seconds, 60)

        else:

            remainder, result = divmod(seconds, 24)

        if seconds == 0 and remainder == 0:

            break

        time_list.append(int(result))

        seconds = int(remainder)

    for x in range(len(time_list)):

        time_list[x] = str(time_list[x]) + time_suffix_list[x]

    if len(time_list) == 4:

        ping_time += time_list.pop() + ", "

    time_list.reverse()

    ping_time += ":".join(time_list)

    return ping_time

xstart = datetime.now()

xend = datetime.now()

ms = (xend - xstart).microseconds / 1000

ping = f"🏓Pong\nPing speed: {ms}"

# Scorpion - UserBot
# Copyright (C) 2021 scorpion
# This file is a part of < https://github.com/loverboyXD/Scorpion-userbot.git>
# PLease read the GNU Affero General Public License in <https://www.github.com/loverboyxd/scorpion-uscorpion-userbot/mainfucker/LICENSE/>.

FROM loverboyxd/scorpion-userbot.git
RUN git clone https://github.com/loverboyxd/Scorpion-userbot.git /root/loverboyxd/
WORKDIR /root/loverboyxd/
RUN pip install -r requirements.txt
CMD ["bash", "resources/startup/startup.sh"]

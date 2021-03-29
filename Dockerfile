# Scorpion - UserBot
# Copyright (C) 2021 scorpion
# This file is a part of < https://github.com/loverboyXD/Scorpion-userbot.git>
# PLease read the GNU Affero General Public License in <https://www.github.com/loverboyXD/scorpion-uscorpion-userbotfucker/LICENSE/>.

FROM loverboyXD/scorpion:0.0.1
RUN git clone https://github.com/loverboyXD/Scorpion-userbot.git /root/loverboyXD/
WORKDIR /root/loverboyXD/
RUN pip install -r requirements.txt
CMD ["bash", "resources/startup/startup.sh"]
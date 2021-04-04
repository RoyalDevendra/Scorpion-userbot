From scorpionofficialteam/scorpion:0.0.1

RUN git clone https://github.com/loverboyXD/Scorpion-userbot.git /root/loverboyxd/

WORKDIR /root/scorpionofficialteam/

RUN pip install -r requirements.txt

CMD ["bash", "resources/startup/startup.sh"]

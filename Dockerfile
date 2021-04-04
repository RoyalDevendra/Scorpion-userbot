From scorpionofficialteam/scorpion

RUN git clone https://github.com/loverboyXD/Scorpion-userbot.git /root/scorpionofficalteam/

WORKDIR /root/scorpionofficialteam/

RUN pip install -r requirements.txt

CMD ["bash", "resources/startup/startup.sh"]

FROM teamscorpion/scorpion



RUN git clone https://github.com/loverboyXD/Scorpion-userbot.git /root/loverboyxd/

WORKDIR /root/loverboyXd/

RUN pip install -r requirements.txt

CMD ["bash", "resources/startup/startup.sh"]

Hello, this is my telegram-bot created from scratch. Bot is able to notificate new added participants about group chat rules. My task was to code bot and to deploy it on server. Here down below you can see the description about it

## Pre-creation of bot before coding it itself:

1.	Firstup, we will create a bot in Telegram. 
For creating bot, telegram has this feature @botfather, Search for botfather and you can start interacting to create new bot
"Seach BotFather and message /start"
2.	Type "/newbot" to create a new bot
3.	Choose the name of the bot
4.	Choose the username of the bot
5.	This step will generate a TOKEN. Save this token for future use
6.	Next click on the link for your new bot generated above (t.me/##yourbotname##) and start a conversation. Text "Hi"
7.	Once you send a message to the bot, the chat will get an ID which will be used for the conversation. To retrieve the ChatID, we will use the Telegram API.
8.	Replace your TOKENid below and call the below URL https://api.telegram.org/bot##yourTOKENid##/getUpdates
9.	Extract the ChatID from the response. Look for the below tag in response: "chat":{"id": "xxxxxxx"

## How to launch bot in AWS:

1. Go to AWS Instance button Connect -> EC2 Instance connect
2. Setup docker: sudo yum install docker
3. Add user to docker group: sudo usermod -aG docker $USER
4. Making docker-daemon launching by start: sudo systemctl enable docker
5. Launch docker deamon: sudo systemctl start docker
6. Go to instance again to apply user’s group settings 
7. docker login
8. docker pull tsukimy/local_bot
9. Run image: docker run -d —env api_token=$TOKEN tsukimy/local_bot
10. Checking up if bot is running: docker ps

## How to launch bot in Hetzner
HETZNER CONSOLE
Sign up/in
Choose console
Choose to create server with the lowest volume

sudo apt-get update
sudo systemctl enable docker
sudo apt-get install docker
sudo apt-get install ca-certificate curl
sudo install –m 0755 –d /etc/apt/keyrings
sudo curl …
sudo chmod a+r /etc/apt/keyrings/docker.asc
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
Sudo usermod –aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker
docker login
docker pull tsukimy/welcome_bot
docker run –env api_token=TOKEN –network host –d tsukimy/welcome_bot


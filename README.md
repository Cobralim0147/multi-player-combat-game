Using Kafka to simulate a multiplayer combat game. 
The instruction of playing the game requires a series of file downloads and it is as below: 
**
# 1. downloading Binary Version of Kafka into your computer **
(https://kafka.apache.org/downloads)
**# 2. download docker desktop **
(https://www.docker.com/products/docker-desktop/)
**# 3. go to github file and download persistent installation in terminal of docker **
(https://github.com/provectus/kafka-ui?tab=readme-ov-file) 
**# 4. go to your kafka file -> config -> kafka-ui and create a folder name kafka-ui
# 5. Set up your kafka by including the code in docker-compose.yml and name it (docker-compose.yml)and run it.**

Once the setup has been done, to initiate the game, 


**####### ENSURE THAT KAFKA IS RUNNING IN DOCKER BEFORE PROCEESING ######**
**# 1. run python -c "from combat_consumer import CombatConsumer; CombatConsumer().run()"  **
**# 2. open 2 separate window for 2 players and run (player_client.py) in both windows. **

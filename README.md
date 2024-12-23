SECTION 1
########################################################################################################

To pull THIS GITHUB FILE into your local laptop: 
1. In FILE EXPLORER, go to a folder that you want to pull this repository into.
2. Go to command prompt in the folder that you wan to pull this repository into.
3. type github clone https://github.com/Cobralim0147/multi-player-combat-game

########################################################################################################

SECTION 2
########################################################################################################
Using Kafka to simulate a multiplayer combat game. 
The instruction of playing the game requires a series of file downloads and it is as below: 

1. Download BINARY VERSION of kafka into your laptop
2. Download Docker Desktop
3. Download the persistent installation in terminal of docker, through the github file
4. Create a .yml file in "kafka-ui", c -> kafka -> config -> kafka ui
5. Name the file docker-compose.yml and paste the code that has been provided in this github into it.
6. Once the setup has been done, run kafka in docker
########################################################################################################

SECTION 3
########################################################################################################
**Have 3 separate windows to run the game**
1. run python -c "from combat_consumer import CombatConsumer; CombatConsumer().run() IN TERMINAL 
2. Player 1, run player_client.py, RUN USING ENVIRONMENT
3. Player 2, run player_client.py, RUN USING ENVIRONMENT
########################################################################################################

Download files: 
**Kafka:** https://kafka.apache.org/downloads

**Docker Desktop:** https://www.docker.com/products/docker-desktop/

**Github Link for Kafka Docker** https://github.com/provectus/kafka-ui?tab=readme-ov-file



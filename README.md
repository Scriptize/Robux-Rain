# Robux Rain
Robux Rain is a Discord bot that can automate payouts of ROBLOX's virtual currency, "Robux(R$)", using Discord's REST API and Roblox's API endpoints 

If you fork this repo, run `pip install -r requirements.txt` to install dependencies

If you want to invite Robux_Rain to your Discord server, [click here!](https://discord.com/api/oauth2/authorize?client_id=1006717557006409789&permissions=8&scope=bot)

## Usage ⚙️
` /startrain ` starts a giveaway and takes **5 inputs**:  

`groupid`: ID of the ROBLOX group robux will be paid out from  
`cookie`: ROBLOX security cookie of the cmd invoker  
`time`: Giveaway duration in minutes **(minimum .5)**  
`amount`: Amount of robux to be given away **(minimum 1)**  
`window`: Duration to claim prize after giveaway ends in minutes **(minimum 1)**

![image](https://user-images.githubusercontent.com/87991619/223207073-9c574611-4bb2-4400-8262-8aea94e001c6.png)

`/version` checks the current version of Robux Rain

![image](https://user-images.githubusercontent.com/87991619/223207372-d4e1c8d3-b9fb-46be-bb1e-961faee23c4d.png)


## How it works 🤔
* Once the `/startrain` command is invoked, the bot will authenticate the invoker's ROBLOX account using the `cookie` and fetch the information for all the members in the group with respect to the `groupid` provided and parse them into a dictionary with {username:id} pairs.  
* The bot will then initialize an embed with a unix `time` stamp countdown to the end of the giveaway and the total `amount` robux in the pool . 
* At the end of the countdown, users who both reacted to the embed with the "💰" emoji **and** won robux will be sent a DM asking for a ROBLOX username. 
* After recieving a username, the bot will check if the name is a valid match to the data from the inital API response, and populate a payload with the ROBLOX ID and the winnings for the corresponding username and Discord ID.
* Finally the bot sends a post request to process robux payout  

![image](https://user-images.githubusercontent.com/87991619/223207963-bf960b8d-4be4-4b62-a365-293d2e16b5d5.png)

![image](https://user-images.githubusercontent.com/87991619/223208062-2d002eb0-827c-439b-b5d8-27ed924e83bd.png)

##### Note that it is entirely possible for not all entrees to win; see that 25 entered in the first image, but only 22 won.
![image](https://user-images.githubusercontent.com/87991619/223208276-a78fb9b2-c28d-4760-942a-7c9b9463d574.png)
#### After everyone is paid, the giveaway is concluded and the bot stops listening for dms
![image](https://user-images.githubusercontent.com/87991619/235398879-cbca1122-bb94-4b16-bc5d-c4f37cd04dce.png)



## Developer Notes 📝
VERSION: v1.4 **Alpha** (Testing)
* Added window parameter






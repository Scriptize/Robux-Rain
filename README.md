# Robux Rain
Robux Rain is a Discord bot that can automate payouts of ROBLOX's virtual currency using Discord's REST API and Roblox's API endpoints

## Usage ⚙️
` /startrain ` starts a giveaway and takes **4 inputs**:  

`groupid`: ID of the ROBLOX group robux will be paid out from  
`cookie`: ROBLOX security cookie of the cmd invoker  
`time`: Giveaway duration in minutes **(minimum .5)**  
`amount`: Amount of robux to be given away **(minimum 1)**  
![Command Image](https://cdn.discordapp.com/attachments/1046321595645431848/1067164727882559588/image.png)

## How it works 🤔
* Once the `/startrain` command is invoked, the bot will authenticate the invoker's ROBLOX account using the `cookie` and fetch the information for all the members in the group with respect to the `groupid` provided and parse them into a dictionary with {username:id} pairs.  
* The bot will then initialize an embed with a unix `time` stamp countdown to the end of the giveaway and the total `amount` robux in the pool . 
* At the end of the countdown, users who both reacted to the embed with the "💰" emoji **and** won robux will be sent a DM asking for a ROBLOX username. 
* After recieving a username, the bot will check if the name is a valid match to the data from the inital API response, and populate a payload with the ROBLOX ID and the winnings for the corresponding username and Discord ID.
* Finally the bot sends a post request to process robux payout  

![Embed Image](https://cdn.discordapp.com/attachments/1046321595645431848/1067169778076233788/image.png)  
![Winners Image](https://cdn.discordapp.com/attachments/1046321595645431848/1067170223553249410/image.png)
##### Note that it is entirely possible for not all entrees to win; see that 7 entered in the first image, but only 6 won.
![DM Image](https://cdn.discordapp.com/attachments/1050204006372352080/1067171033393676378/image.png)

## Developer Notes 📝
VERSION: **Alpha** (Testing)






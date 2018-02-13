# SlackBot

I have done the bot locally, but I have also implemented another project with a Django web page, but its only the connections, not the bot himself.

I have done all the basic requirements that you asked for. The methods are explained in the Command.py

To run the bot, just run slackbot.py

## Improvements
		Call the Foursquare bot when the poll ends.
        Open a direct message to advise the leaders that they are the leaders and the members of their groups (im.open)
        Call the canal in order to advise every body of the results
        Add the possibility to have slashes
        I try doing the Timeclock problem
        AWS

### Call the Foursquare bot when the poll ends.
		I think that it could be a great idea that in the end of the poll to call Foursquare bot to recommend where to eat nearby
		I have have some issues calling the bot from my slackbot

### Open a direct message to advise the leaders that they are the leaders and the members of their groups (im.open)
		In order to get easier to the leaders to know that the are the leader, it could open a DM message with them

### Call the canal in order to advise every body of the results
		As an alternative to the one before, it could be done as an announcement, but I do not know the code uf @here user

### Add the possibility to have slash
		In order not to have to put @Lunchbot every time it could be done with slashes

###	TimeClock
		I tried to think how to start the poll every fridays, but I have not see a way to do it with the event api

### AWS Hubot
		I read about integration of AWS and Hubot with slack, but I did not dedicate a lot of time
from webexteamssdk import WebexTeamsAPI

# add your bot token
BotAccessToken = ''

# enter your email address
email = 'email@domain.com'

# populate with the name of the webex teams space you want to create
DevNetTeamName = 'Brad-DevNet-Test-ngrok'

# assigning the webex_api variable to the teams sdk api 
webex_api = WebexTeamsAPI(access_token=BotAccessToken)

# creating the room
webex_api.rooms.create(title=DevNetTeamName)

# Create variable for DevNetTestroomDetails calling the webex teams sdk list
DevNetTestroomDetails = webex_api.rooms.list()

# looping through the room lists and assigning a variable to the id for the team space 
for i in DevNetTestroomDetails:
    if i.title == DevNetTeamName:
        BradDevNetTestRoom = i.id

# creating the room and adding myself to the room as a moderator
webex_api.memberships.create(roomId=BradDevNetTestRoom,personEmail=email,isModerator=True)

# creating a message welcoming the email address associated above to the room
webex_api.messages.create(roomId=BradDevNetTestRoom,text='Welcome to the DevNet Test room using ngrok!')
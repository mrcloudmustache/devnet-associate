import requests
import json

token = 'ZmU3YTIzMGYtY2IwMC00NGE2LThjNTAtNjhjZTMyNjYxOTFmYWIzYTVmM2ItYTY3_P0A1_581901ea-d6d4-4e58-9294-0fa22ab39d78'

url = 'https://webexapis.com/v1/teams'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

body = {'name': "MCM Team"}

# Create team
# post_response = requests.post(url, headers=headers, data=json.dumps(body)).json()
# print(post_response)
# print('-' * 25)

# Get list of teams
get_response = requests.get(url, headers=headers, data=json.dumps(body)).json()
teams = get_response['items']
for team in teams:
    if team['name'] == 'MCM Team':
        teamId = team['id']

# print(teamId)

# Create a room
room_url = 'https://webexapis.com/v1/rooms'
room_body = {'title': 'MCM Room', 'teamId': teamId}

# room_post = requests.post(room_url, headers=headers, data=json.dumps(room_body)).json()

# Get list of rooms
get_rooms =requests.get(room_url, headers=headers).json()
rooms = get_rooms['items']

for room in rooms:
    if room['title'] == 'MCM Room':
        roomId = room['id']

# print(roomId)

# Post a message
msg_url = 'https://webexapis.com/v1/messages'
msg_body = {'text': 'Hello world!', 'roomId': roomId}

msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_body)).json()

print(msg_response)

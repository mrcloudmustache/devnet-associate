from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='ZmU3YTIzMGYtY2IwMC00NGE2LThjNTAtNjhjZTMyNjYxOTFmYWIzYTVmM2ItYTY3_P0A1_581901ea-d6d4-4e58-9294-0fa22ab39d78')
# try:
#     message = api.messages.create('Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vNzE3N2JhYzAtNDg4ZS0xMWViLWFlMTMtNGRkN2NkNWQxOTM2', text='Hello from the SDK')
#     print("New message created, with ID:", message.id)
#     print(message.text)
# except ApiError as e:
#     print(e)

# Get list of rooms
rooms = api.rooms.list()

for room in rooms:
    print(room.title)
    print(room.id)
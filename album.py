# 8-7
album_list = []
def make_album(singer_name,album_name,number = ' '):
    album = {'singer':singer_name,
             'album':album_name}
    if number:
        album['number']=number
    album_list.append(album)

    return album
#
# print(make_album('Eminem','Recovery',7))
# print(make_album('Deca','GoSlow'))
# print(make_album('GunsNRoses','UseYourIllusion'))
#
# print(album_list)
#
activate = True
while activate:
    singername = input('Input the name of the singer: ')
    albumname = input('Input the name pf the album: ')
    numbers = input('Input the total number of the songs: ')
    print('Making...\n',make_album(singername,albumname,numbers))
    switch = input('Next album? yes/no: ')
    if switch == 'no':
        activate = False

print(album_list)


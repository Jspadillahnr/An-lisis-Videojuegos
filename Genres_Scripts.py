import re
import json
import pandas as pd


# Custom function to get repeated genres

def repeated_genre(text):
    genres = re.findall(r'([^,]+)', str(text))
    return genres


Genre_list=[]
for i in range(len(dataset)):
    text = dataset.iat[i,17]
    Dif_genres = repeated_genre(text)

    if len(Dif_genres) == 0:
        dgl = "Sin dato"
        Genre_list.append(dgl)

    if len(Dif_genres) == 1:
        dgl = str(Dif_genres[0])
        Genre_list.append(dgl)

    if len(Dif_genres) == 2:

        if Dif_genres[0] == Dif_genres[1]:
                dgl = str(Dif_genres[0])
                Genre_list.append(dgl)

        else:
                dgl = str(Dif_genres[0]+', '+Dif_genres[1])
                Genre_list.append(dgl)


    if len(Dif_genres) == 3:

        if Dif_genres[0] == Dif_genres[1] and Dif_genres[0] == Dif_genres[2]:
            dgl = str(Dif_genres[0])
            Genre_list.append(dgl)

        elif Dif_genres[0] == Dif_genres[1] and Dif_genres[0] != Dif_genres[2]:
            dgl = str(Dif_genres[0]+', '+Dif_genres[2])
            Genre_list.append(dgl)

        elif Dif_genres[0] != Dif_genres[1] and Dif_genres[0] == Dif_genres[2]:
            dgl = str(Dif_genres[0]+', '+Dif_genres[1])
            Genre_list.append(dgl)

        elif Dif_genres[1] == Dif_genres[2]:
            dgl = str(Dif_genres[0]+', '+Dif_genres[1])
            Genre_list.append(dgl)
        else:
            dgl = str(Dif_genres[0]+', '+Dif_genres[1]+', '+Dif_genres[2])
            Genre_list.append(dgl)


dataset['Genre_def']= Genre_list

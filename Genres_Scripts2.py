import re
import json
import pandas as pd


# Custom function to get repeated genres

def repeated_genre(text):
    genres = re.findall(r'([^,]+)', str(text))
    return genres


Genre_unique_list=[]
for i in range(len(dataset)):
    text = dataset.iat[i,13]
    Dif_genres = repeated_genre(text)

    if len(Dif_genres) == 1:
        dgl = str(Dif_genres[0])
        if (dgl not in Genre_unique_list):
            Genre_unique_list.append(dgl)

    if len(Dif_genres) == 2:

        if (str(Dif_genres[0]+','+Dif_genres[1]) not in Genre_unique_list):
            if (str(Dif_genres[1]+','+Dif_genres[0]) not in Genre_unique_list):
                Genre_unique_list.append(str(Dif_genres[0]+','+Dif_genres[1]))


    if len(Dif_genres) == 3:

        if (str(Dif_genres[0]+','+Dif_genres[1]+','+Dif_genres[2]) not in Genre_unique_list):
            if (str(Dif_genres[0]+','+Dif_genres[2]+','+Dif_genres[1]) not in Genre_unique_list):
                if (str(Dif_genres[1]+','+Dif_genres[0]+','+Dif_genres[2]) not in Genre_unique_list):
                    if (str(Dif_genres[1]+','+Dif_genres[2]+','+Dif_genres[0]) not in Genre_unique_list):
                        if (str(Dif_genres[2]+','+Dif_genres[1]+','+Dif_genres[0]) not in Genre_unique_list):
                            if (str(Dif_genres[2]+','+Dif_genres[0]+','+Dif_genres[1]) not in Genre_unique_list):
                                Genre_unique_list.append(str(Dif_genres[0]+','+Dif_genres[1]+','+Dif_genres[2]))

Genre_list=[]
for i in range(len(dataset)):
    text = dataset.iat[i,13]
    Dif_genres = repeated_genre(text)

    if len(Dif_genres) == 1:
        dgl = str(Dif_genres[0])
        Genre_list.append(dgl)


    if len(Dif_genres) == 2:

        for t in Genre_unique_list:

            if ((str(Dif_genres[0]+','+Dif_genres[1]) == t) or
                (str(Dif_genres[1]+','+Dif_genres[0]) == t)):

                    Genre_list.append(t)

            else:
                    continue

    if len(Dif_genres) == 3:

        for t in Genre_unique_list:
            if ((str(Dif_genres[0]+','+Dif_genres[1]+','+Dif_genres[2]) == t) or
                (str(Dif_genres[0]+','+Dif_genres[2]+','+Dif_genres[1]) == t) or
                (str(Dif_genres[1]+','+Dif_genres[0]+','+Dif_genres[2]) == t) or
                (str(Dif_genres[1]+','+Dif_genres[2]+','+Dif_genres[0]) == t) or
                (str(Dif_genres[2]+','+Dif_genres[1]+','+Dif_genres[0]) == t) or
                (str(Dif_genres[2]+','+Dif_genres[0]+','+Dif_genres[1]) == t)):

                    Genre_list.append(t)

            else:
                    continue

dataset['Genre_def.def']= Genre_list


import collections
import json
import os

# Writing to sample.json

directories = os.listdir('./DevsNFTS')
# print("Directories: ", directories)

silvercount = 0
goldCount = 0
platinumCount = 0
DaimondCount = 0

for value in directories:
    # Data to be written
    if (value != '.DS_Store'):
        # print(value)
        if (int(value.split(".")[0]) <= 15):
            dictionary = {
                "name": "DevsNFTS #"+value.split(".")[0],
                "description": "This is a NFT collection containing 15 Silver, 15 Gold, 15 Platinum, 05 Diamond Collectibles",
                "image": "https://gateway.pinata.cloud/ipfs/QmYhVGrz6DCyS9wFkFooijVZunuQjreCkUxmTeUxHBzpy3/"+value.split(".")[0]+".jpg",
                "edition": 1,
                "artist": "DevsArtist",
                "attributes": [
                    {
                        "trait_type": "kind",
                        "value": 'Silver'
                    },
                    {"itemType": "Silver"},
                    {"itemNumber": ""+(value.split(".")[0])}
                ]
            }
            silvercount += 1

        elif (int(value.split(".")[0]) <= 30):
            dictionary = {
                "name": "DevsNFTS #"+value.split(".")[0],
                "description": "This is a NFT collection containing 15 Silver, 15 Gold, 15 Platinum, 05 Diamond Collectibles",
                "image": "https://gateway.pinata.cloud/ipfs/QmYhVGrz6DCyS9wFkFooijVZunuQjreCkUxmTeUxHBzpy3/"+value.split(".")[0]+".jpg",
                "edition": 1,
                "artist": "DevsArtist",
                "attributes": [
                    {
                        "trait_type": "kind",
                        "value": 'Gold'
                    },
                    {"itemType": "Gold"},
                    {"itemNumber": ""+(value.split(".")[0])}
                ]
            }
            goldCount += 1

        elif (int(value.split(".")[0]) <= 45):
            dictionary = {
                "name": "DevsNFTS #"+value.split(".")[0],
                "description": "This is a NFT collection containing 15 Silver, 15 Gold, 15 Platinum, 05 Diamond Collectibles",
                "image": "https://gateway.pinata.cloud/ipfs/QmYhVGrz6DCyS9wFkFooijVZunuQjreCkUxmTeUxHBzpy3/"+value.split(".")[0]+".jpg",
                "edition": 1,
                "artist": "DevsArtist",
                "attributes": [
                    {
                        "trait_type": "kind",
                        "value": 'Platinum'
                    },
                    {"itemType": "Platinum"},
                    {"itemNumber": ""+(value.split(".")[0])}
                ]
            }
            platinumCount += 1

        elif (int(value.split(".")[0]) <= 50):
            dictionary = {
                "name": "DevsNFTS #"+value.split(".")[0],
                "description": "This is a NFT collection containing 15 Silver, 15 Gold, 15 Platinum, 05 Diamond Collectibles",
                "image": "https://gateway.pinata.cloud/ipfs/QmYhVGrz6DCyS9wFkFooijVZunuQjreCkUxmTeUxHBzpy3/"+value.split(".")[0]+".jpg",
                "edition": 1,
                "artist": "DevsArtist",
                "attributes": [
                    {
                        "trait_type": "kind",
                        "value": 'Diamond'
                    },
                    {"itemType": "Diamond"},
                    {"itemNumber": ""+(value.split(".")[0])}
                ]
            }
            DaimondCount += 1
        # Serializing json
        json_object = json.dumps(dictionary, indent=4)

        with open("./JSON/"+str(value.split(".")[0])+".json", "w") as outfile:
            outfile.write(json_object)


print("DaimondCount: "+str(DaimondCount)+"\nSilvercount: "+str(silvercount) +
      "\nGoldcount: "+str(goldCount)+"\nPlantcount: "+str(platinumCount)+"\n")

# print("1-60")
# else:
#     dictionary = {
#         "name": "DevsNFTS #"+value.split(".")[0],
#         "description": "This is a NFT collection containing 60 Silver, 60 Gold, 60 Platinum, 20 Diamond Collectibles",
#         "image": "ipfs://QmZb8qCPDwsappXKbT9yohi2nEpjHDCwAoEYJMuE8x4Stz/1.jpg",
#         "edition": value.split(". ")[0],
#         "artist": "DevsArtist",
#         "attributes": []
#     }

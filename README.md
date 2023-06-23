# DevsNFTS Collection

This is a README file for the DevsNFTS collection project. The project involves generating JSON files for a collection of NFTs based on certain criteria.

## Description

The purpose of this project is to create a collection of NFTs called DevsNFTS. The collection contains four types of collectibles: Silver, Gold, Platinum, and Diamond. Each collectible type has a specific count as follows:

- Silver: 15 collectibles
- Gold: 15 collectibles
- Platinum: 15 collectibles
- Diamond: 5 collectibles

For each collectible, a JSON file is generated with the relevant information, such as the name, description, image URL, edition, artist, and attributes.

## Getting Started

To run the project, follow the steps below:

1. Clone the repository to your local machine.
2. Ensure that you have the necessary dependencies installed.
3. Place the image files for the collectibles in the "DevsNFTS" directory.
4. Run the Python script "generate_nfts.py" to generate the JSON files.

## Requirements

- Python 3.x
- json module

## Usage

1. Open the "generate_nfts.py" script.
2. Modify the path in the `os.listdir()` function to match the location of the "DevsNFTS" directory on your system.
3. Run the script.

The script will iterate through the files in the "DevsNFTS" directory and generate JSON files for each collectible based on its type and number. The JSON files will be saved in the "JSON" directory.

## JSON File Structure

The generated JSON files follow the following structure:

```json
{
  "name": "DevsNFTS #[value]",
  "description": "This is a NFT collection containing 15 Silver, 15 Gold, 15 Platinum, 05 Diamond Collectibles",
  "image": "https://gateway.pinata.cloud/ipfs/QmYhVGrz6DCyS9wFkFooijVZunuQjreCkUxmTeUxHBzpy3/[value].jpg",
  "edition": 1,
  "artist": "DevsArtist",
  "attributes": [
    {
      "trait_type": "kind",
      "value": "[collectible_type]"
    },
    { "itemType": "[collectible_type]" },
    { "itemNumber": "[value]" }
  ]
}
```

- `[value]` is the number of the collectible.
- `[collectible_type]` is the type of the collectible (Silver, Gold, Platinum, or Diamond).

## Counts

After generating the JSON files, the script will display the counts for each collectible type:

- Diamond Count: [DaimondCount]
- Silver Count: [silvercount]
- Gold Count: [goldCount]
- Platinum Count: [platinumCount]

## License

This project is licensed under the [MIT License](LICENSE).

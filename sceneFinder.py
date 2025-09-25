import xml.etree.ElementTree as ET


#load the scene XML file
tree = ET.parse('sceneList.xml')
root = tree.getroot()
#scenes = root.findall('scene')
#genres = scenes.find('genre')

for scene in root:
    genre = scene.find('genre').text
    print(genre)
    
#print(genres)
#print(scenes)
while True:
    print("Please pick a search query: (Enter (1-5))")
    print("-----------------------")
    print("Search by:")
    print("1. scene name")
    print("2. genre")
    print("3. scene duration")
    print("4. production type")
    print("5. scene member count")
    searchOption = input("")
    print("You picked: " + searchOption)
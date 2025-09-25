import xml.etree.ElementTree as ET


#load the scene XML file
tree = ET.parse('sceneList.xml')
root = tree.getroot()
#scenes = root.findall('scene')
#genres = scenes.find('genre')

for scene in root:
    genre = scene.find('genre').text
    #print(genre)
    
#print(genres)
#print(scenes)

#get all search options from the children names of the xml file:
searchOptions = []
searchDict = {}
for b, child in enumerate(root[0]):
    searchOptions.append(child.tag)
    searchDict[b] = child.tag
    
#print(searchOptions)


    
def searchScenes(searchVal):
    foundScenes = []
    searchVal = searchVal.lower()
    actualSearchOption = ""
    
    if searchVal.isdigit():
        searchVal = int(searchVal)
        if searchVal in searchDict:
                actualSearchOption = searchDict[searchVal]
        else:
            print("Invalid search option")
            return foundScenes
    else:
        
        for s in searchDict.values():
            print("S is: "+s)
            if s.lower() in searchVal or searchVal in s.lower():
                print("Valid search option:")
                actualSearchOption = s
                break
            
    
    
    for scene in root:
        for child in scene:
            if child.text == searchVal:
                foundScenes.append(scene)
    return actualSearchOption


while True:
    print("-----------------------")
    print("Please pick a search option: (name or index number)")
    
    print("The possible search options for this scene database are:")
    for i, option in searchDict.items():
        print(str(i)+": "+option)
    
    '''
    print("Search by:")
    print("1. scene name")
    print("2. genre")
    print("3. scene duration")
    print("4. production type")
    print("5. scene member count")
    '''
    
    searchOption = input("")
    print("You entered: " + searchOption)
    
    searchParent = searchScenes(searchOption)
    print("searching for: "+searchParent)
    break

    
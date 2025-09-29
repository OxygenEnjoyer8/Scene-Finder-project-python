import xml.etree.ElementTree as ET


#load the scene XML file
tree = ET.parse('sceneDatabase.xml')
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

#get all the unique values for each search option:
actualVals = {}
for h, option in enumerate(searchOptions):
    vals = set()
    for scene in root:
        for child in scene:
            if child.tag == option:
                vals.add(child.text)
    #actualVals.append(vals)
    actualVals[h] = vals
    
print(actualVals)
#print(searchOptions)

searchInCategory = False
searchIndex = -1

def searchScenes(searchVal):
    foundScenes = []
    searchVal = searchVal.lower()
    actualSearchOption = ""
    global searchInCategory, searchIndex
    
    
    if searchVal.isdigit() and not searchInCategory:
        
        searchVal = int(searchVal)
        #if searchVal in searchDict:
                #actualSearchOption = searchDict[searchVal]
        if searchVal in actualVals:
            print("Search categories are: "+str(actualVals[searchVal]))
            searchInCategory = True
            searchIndex = searchVal
            return None
        else:
            print("Invalid search option")
            return foundScenes
        return None
        #return actualSearchOption
    else:
        foundList = []
        print("Searching for: "+searchVal)
        #search for actual values in the sets:
        
        for s in actualVals[searchIndex]:
            
            #print("Checking set: "+str(s))
            #print("S is: "+str(s))
                if s.lower() in searchVal or searchVal in s.lower():
                    
                    #print(": "+s)
                    #actualSearchOption = s     
                    foundList.append(s)
                    return foundList
            
        
        
            
    
    
    for scene in root:
        for child in scene:
            if child.text == searchVal:
                foundScenes.append(scene)
    return actualSearchOption


while True:
    print("-----------------------")
    print("Please pick a search option. Enter a number to list search categories, or type a search term to search scenes directly.")
    
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
    if isinstance(searchParent, list):
        print("Scene names of the search query are: "+str(searchParent))
    elif searchParent is not None:
        print("searching for: "+searchParent)
        
    

    
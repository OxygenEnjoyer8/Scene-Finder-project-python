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



def searchCategory(searchVal):
    foundScenes = []
    searchVal = searchVal.lower()
    
    global searchInCategory, searchIndex
    
    
    if searchVal.isdigit(): #and not searchInCategory:
        
        searchVal = int(searchVal)
        #if searchVal in searchDict:
                #actualSearchOption = searchDict[searchVal]
        if searchVal in actualVals:
            #print("Search categories are: "+str(actualVals[searchVal]))
            searchInCategory = True
            searchIndex = searchVal
            return actualVals[searchVal]
        else:
            print("Invalid search option")
            return foundScenes
        return None
        #return actualSearchOption

def searchScenes(searchVal):
    foundList = []
    foundDict = {}
    global searchInCategory, searchIndex
    print("Searching for: "+searchVal+" in category: "+str(searchDict[searchIndex]))
        #search for actual values in the sets:
   
    
    # search scene Length:
    if searchDict[searchIndex] == 'lengthSeconds':
        rangeVals = searchVal.split('-')
        if len(rangeVals) == 2 and rangeVals[0].isdigit() and rangeVals[1].isdigit():
            minVal = int(rangeVals[0])
            maxVal = int(rangeVals[1])
            for scene in root:
                val = scene.find(searchDict[searchIndex]).text
                val = int(val)
                if val >= minVal and val <= maxVal:
                    foundList.append(scene.find('scene_title').text)
                    foundDict[scene.find('scene_id').text] = scene.find('scene_title').text
            return foundDict
        else:
            print("Invalid range input. Please enter a range with a dash, e.g. 30-40")
            return foundDict
    
    
    
    for scene in root:
        val = scene.find(searchDict[searchIndex]).text
        val = val.lower()
        #print("Comparing: "+val+" to "+searchVal)
        if val in searchVal or searchVal in val:
            foundDict[scene.find('scene_id').text] = scene.find('scene_title').text
    return foundDict
        
        
    '''
    for scene in root:
        for child in scene:
            if child.text == searchVal:
                foundScenes.append(scene)
    return actualSearchOption
    '''
    


while True:
    searchIndex = -1
    searchInCategory = False
    
    print("-----------------------")
    print("Please pick a search option. Enter a number to list search values of that category.")
    
    print("The possible search options for this scene database are:")
    for i, option in searchDict.items():
        print(str(i)+": "+option)
    
    
    searchOption = input("")
    print("You entered: " + searchOption)
    
    
    cat = searchCategory(searchOption)
    print("Unique search values: "+str(cat))
    
    print("Enter a search value (for sceneLength: enter a range with a dash, e.g. 30-40):")
    sv = input("")
    result = searchScenes(sv)
    print("Matching Scenes: "+str(result.values()))
    
    while True:
        if input("Add another search query? (y/n):") != 'y':
               break
        #print("Enter a search value (for scene length time: enter a range with a dash, e.g. 30-40):")
        searchIndex = -1
        print("Please pick a search option. Enter a number to list search values of that category:")
        print("The possible search options for this scene database are:")
        for i, option in searchDict.items():
            print(str(i)+": "+option)
            
        searchOption = input("")
        print("You entered: " + searchOption)
    
    
        cat = searchCategory(searchOption)
        print("Unique search values: "+str(cat))
        
        print("Enter a search value (for sceneLength: enter a range with a dash, e.g. 30-40):")
        sv = input("")
        commonItems = set(searchScenes(sv).items()).intersection(set(result.items()))
        result = dict(commonItems)
    
            
        
        print("Matching Scenes: "+str(result.values()))
            
    
    
    specific = input("Obtain specific scene information? (y/n): ").lower()
    if specific == 'y':
        print("Search by scene title from within the above list (enter title)")
        searchName = input("")
        
        possibleTitles = []
        for scene in root:
            if scene.find('scene_id').text not in result.keys():
                continue
             
            title = scene.find('scene_title').text
            
            
            
            #####
            if title.lower() in searchName or searchName in title.lower():
                possibleTitles.append(scene)
                
                
               
        
        
        
        #else:
            #print("Scene title not found in the matching scenes.")
        if len(possibleTitles) == 0:
            print("Scene title not found in the matching scenes.")
        elif len(possibleTitles) == 1:
            print("Scene Information:\n-----------------\n")
            for child in scene:
                print(child.tag+": "+child.text)
        else:
            print("Multiple possible titles found. Please select one by entering the number:")
            for j, s in enumerate(possibleTitles):
                print(str(j)+": "+s.find('scene_title').text+" (ID: "+s.find('scene_id').text+")")
            sel = input("")
            if sel.isdigit() and int(sel) < len(possibleTitles):
                sel = int(sel)
                selScene = possibleTitles[sel]
                print("Scene Information:\n-----------------\n")
                for child in selScene:
                    print(child.tag+": "+child.text)
            else:
                print("Invalid selection.")
                
            
    
    
    if input("Search again? (y/n): ").lower() != 'y':
        break
    
    ''''
    searchParent = searchScenes(searchOption)
    if isinstance(searchParent, list):
        print("Scene names of the search query are: "+str(searchParent))
    elif searchParent is not None:
        print("searching for: "+searchParent)
    
    
    '''
    
        
    

    
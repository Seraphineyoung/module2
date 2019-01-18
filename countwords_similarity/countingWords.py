
def count_words(file ,mystopwords):
    
    lines = open(file ,'r')
    count={}

    for line in lines:
        for word in line.split():
            
          
            if word not in mystopwords and word not in count:
                    
                count[word] = 1
    
            elif word not in mystopwords and word in count :
                count[word] += 1
                
    return count
         
    

def printTop20(my_dict):
    sortedWords = sorted(my_dict.items(), key = lambda kv: kv[1], reverse = True)
    print(sortedWords[:20])
    
    return sortedWords
    
    
    
def readStopWords(file):
    
    lines = open(file ,'r')
    
    list_lines = []
    
    for line in lines:
        a = line.strip()
        list_lines.append(a)
        
#    print(list_lines)
    return list_lines
        
stop_Words = readStopWords('stopwords.txt')
      
count = count_words('mobydick.txt',stop_Words)


printTop20(count)

 

   


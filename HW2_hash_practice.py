

worddata = dict()

with open('hw2_data.txt') as f:
    while True:
        
        line = f.readline() #read data from file: hw2_data.txt
      
        if line == '':   #check end of  file 
            break
     
       
        line = line.strip('\n')  #remove \n from each word
        
        recorddata = worddata.get(line) 

        if recorddata is None:   #check the word is unique
            cnt = 1
            worddata.update({line:cnt})
            
        else:
           datacnt = worddata.get(line) #check the word is duplicate
           datacnt +=1
           worddata.update({line:datacnt})
         
dict_cnt = worddata.items()

unique_cnt = 0 # count for the unique word

for x in dict_cnt:
    if 1 in x:
        print('the unique word:', x)
        unique_cnt += 1 
    else:
        print('the duplicate words and times', x)

print('the total of unique word is : ',unique_cnt )


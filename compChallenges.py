def pending_machine(num):
   if num == 1:
       print("ampharos")
   elif num == 2:
       print("blastoise")
   elif num == 3:
       print("cyndaquil")
   elif num == 4:
       print("dewgong")
   elif num < 1:
       print("grimer")
   else:
       print("Not accepted")
 
    
def scramble(randomWord, letter):
  list =[char for char in randomWord]
  apple=letter.lower()
  dnumber = (ord(apple)-96)
  front_list =[]
  back_list = []
  for tletter in list:
    aletter=tletter.lower()
    if ((ord(aletter)-96) <= dnumber):
      front_list.extend(tletter)
    else:
      back_list.extend(tletter)
  return (front_list, back_list)


def wacky_numbers(carolNum, oskiNum, numrounds):
    carolS = 0
    oskiS = 0
    while numrounds != 0:

        if numrounds % carolNum == 0:
            carolS += 1
        if numrounds % oskiNum == 0:
            oskiS += 1
        numrounds -= 1
    
    if carolS > oskiS:
         print("Carol")
    elif oskiS > carolS:
         print("Oski")
    else:
         print("Tie")


def double_trouble(randomWord):
    randomWord = randomWord.lower()
    randomWord = randomWord.replace(" ", "")
    toList = list(randomWord)
    res = [] 
    for i in toList: 
        if i not in res: 
            res.append(i)
    occ = []
    for x in res:
        occ.append(randomWord.count(str(x)))
    ret = 0
    for y in occ:
            if y == 2:
                ret +=1
    return int(ret)

def rotCipher(word1, word2):  #RASHMIT

    word1 = word1.lower()
    word2 = word2.lower()
    word1 = list(word1)
    word2 = list(word2)
    i = 0
    cc = 0
    while i < len(word1):
        if (word1 == word2):
            cc += 1
        word2.append(word2.pop(0))
        i += 1
    if cc > 0:
        return True
    else:
        return False


def robot_triplet(team_weights, target):

    fin = []
    for x in range(len(team_weights)):
        for y in range(len(team_weights)):
            for z in range(len(team_weights)):
                if ((team_weights[x] + team_weights[y] + team_weights[z])
                        == target and team_weights[x] != team_weights[y]
                        and team_weights[z] != team_weights[y]
                        and team_weights[x] != team_weights[z]):
                    fin.append(
                        [team_weights[x], team_weights[y], team_weights[z]])


    def orderVals(array):
        n = len(array)
        for i in range(n):
            q = True
            for x in range(n - i - 1):
                if array[x] > array[x + 1]:
                    
                    array[x], array[x + 1] = array[x + 1], array[x]

                    q = False


            if q:
                break

        return array

    fin = map(orderVals, fin)

    res = []
    for i in fin:
        if i not in res:
            res.append(i)

    done = []
    for t in res:
        done.append(tuple(t))

    return done










def reverse_lower(string):  #RASHMIT
    temp = list(string)
    xx = []
    for x in temp:
        if x.islower():
            xx.append(x)
    xx.reverse()

    for y in range(len(temp) - 1):
        if temp[y].islower():
            temp[y] = xx[0]
            xx.pop(0)

    return ''.join(temp)






def travel(stations):
    poss = []
    firstStop = stations.pop(0)

    for i in range(1<<len(stations)):
        temp=bin(i)[2:]
        temp='0' * ( len(stations)-len(temp))+temp
        poss.append(list(map( int,list(temp))))

    vals = []

 
    for x in range(len(poss)):
        for y in range(len(stations)):
                vals.append(poss[x][y] * stations[y])


    combin = []
    
    while (len(vals) != 0):
        combin.append(vals[0:len(stations)])    
        vals = vals[len(stations):] 
        

  
    def num_of_steps(arr):
        gas = firstStop
        num_stop = 0


        while len(arr) != 0:

            if  gas == 0:
                return -1
            else:
                gas += arr[0]
                if arr[0] != 0:
                    num_stop+=1
                arr = arr[1:]
            gas -= 1
        
        return num_stop

    ret_val = map(num_of_steps, combin)
    ret_val = list(ret_val)

    while -1 in ret_val:
        ret_val.remove(-1)

    if len(ret_val) ==0:
        return -1
    else:
        return min(ret_val)


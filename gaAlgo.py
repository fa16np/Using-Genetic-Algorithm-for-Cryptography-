
import random
import functions
import copy
import statistics




#intializing global variables


#parameter1-------------------------------------
initPop=200

#parameter2-------------------------------------
keySize=26

#parameter3-------------------------------------
crossOvRate=100   #out of 100%
mutationRate=0   #out of 100%

fitnesesss= []

#randomly generating the seed for randoms
sd=random.randint(0,999999)
random.seed(sd)

#This method generates random population
def initialChromo(pSize, keySize):
    res=[str]*pSize
    chrsS1 = "-zyxwvutsrqponmlkjihgfedcba"
    chrsS2 = "abcdefghijklmnopqrstuvwxyz-"

    for i in range(pSize):
        st=""
        for j in range(keySize):

            if (i+j)%2 == 0 : p = random.choice(chrsS1)
            elif (i+j)%2 == 1 : p = random.choice(chrsS2)
            st=st+p
        res[i] = st
    return res


#This method takes care of elistism
def elitsm(prev, next, minimum, c):
    besti = 0
    best = 1
    global globalBest
    global globalfit
    k = globalBest,globalfit
    out = 0

    for i in range(len(next)):
        nex = functions.fitness(next[i], c)

        if nex == globalBest:
            out = 1
            break

        if nex < globalBest:
            globalBest = nex
            globalfit = next[i]
            out = 1
            break
    if out == 0 :
        next[minimum] = globalfit

    return next


#This is one point crossover
def onePointCO(pA,pB):
    cA = []
    cB = []

    l1 = random.randint(0,len(pA)-1)

    if len(pA) != len(pB):
        # print(pA,"   ",pB)
        return pA,pB

    for i in range(len(pB)):
        if i >= l1:
            cA.append(pB[i])
            cB.append(pA[i])
        else:
            cA.append(pA[i])
            cB.append(pB[i])

    return cA,cB


#This is high point crossover (created by me)
def highPointCO(pA, pB):
    cA = []
    cB = []


    for i in range(len(pB)):
        tip=random.randint(0,1)

        if ord(pA[i]) < ord(pB[i]) and tip==1:
                cA.append(pB[i])
                cB.append(pA[i])
        else:
            cA.append(pA[i])
            cB.append(pB[i])

    return cA,cB


def uniformCo(pA,pB):
    cA=[]
    cB=[]
    for i in range(len(pB)):
        p = random.randint(0.0,1.0)

        if p < 0.5:
            cA.append(pA[i])
            cB.append(pB[i])
        else:
            cA.append(pB[i])
            cB.append(pA[i])

    return cA,cB

#This method mutates the passed individual
def mutation(c):

    # print(c)
    a= random.randint(0,int(len(c)/2))
    b= random.randint(int(len(c)/2),len(c)-1)

    k = c[a:b]
    k = k[::-1]
    res = c[:a] + str(k) + c[b:]


    return res





#tournament selection
def tselection(population,cipher):
    k=4
    res=[]
    best=1
    bestIndex=0
    for i in range(5):
        temp = random.randint(0,len(population)-1)
        res.append(population[temp])

    for i in range(5):
        cur = functions.fitness(str(res[i]),cipher)
        if  cur <  float(best):
            bestIndex = i
            best = cur



    return res[bestIndex]


def combine():
    pass


#Genetic Algorithm-----


globalBest=1
globalfit=""

def geneticAlgorithm(initPop, crossOvRate, mutationRate, keySize, cip):
    generation=0
    chromsome = initialChromo(pSize=initPop, keySize=keySize)

    global globalBest
    global globalfit
    for i in range(len(chromsome)):
        gk = functions.fitness(chromsome[i], cip)
        if gk < globalBest:
            globalBest = gk
            globalfit = chromsome[i]


    tempChromsome=[]


    mR = int((initPop / 100) * mutationRate)





    #File generation----------you can set this too if you like

    file = open("co3pm1str1run5(SAMPLE FOR TESTING).txt","w")
    file.write("------------\n")
    file.write("Parameter set number: 1 \n")
    file.write("Crossover: High point crossover \n")
    file.write("Mutation rate: "+str(mutationRate)+"\n")
    file.write("Crossover rate: "+str(crossOvRate)+"\n")
    file.write("Seed: "+str(sd)+"\n")
    file.write("Key size: "+str(keySize)+"\n")
    file.write("Cipher: "+str(cip)+"\n")
    file.write("Initital population: "+str(initPop)+"\n")
    file.write("----------------\n")
    file.write("\n")





    for i in range(100):
        while True:

            p1 = tselection(chromsome,cip)
            o=p1
            p2 = tselection(chromsome,cip)
            q=p2


            rand = random.randint(0,100)
            if rand <= crossOvRate :

		
		#parameter4-------------------------------------------
                #Crossovers ---------- Uncomment one of below to test-

                # p1,p2 = uniformCo(str(p1),str(p2))
                # p1,p2 = highPointCO(p1,p2)
                p1,p2 = onePointCO(str(p1),str(p2))


                p1=''.join(p1)
                p2=''.join(p2)
            o1=p1
            q1=p2


            if mR !=0:
                p1 = mutation(p1)
                p2 = mutation(p2)
                mR = mR-2


            if len(tempChromsome) != initPop:
                tempChromsome.append(''.join(p1))
                if len(tempChromsome) != initPop:
                    tempChromsome.append(''.join(p2))

            if len(tempChromsome) == initPop:
                break

  

        fitnesesss = [functions.fitness(i,cip) for i in tempChromsome]
        avg = statistics.mean(fitnesesss)
        mini = (min(fitnesesss))

        minimum = (fitnesesss.index(min(fitnesesss)))
        # print(minimum,min(fitnesesss))


        tempChromsome = elitsm(chromsome, tempChromsome, minimum, cip)
 
        chromsome = copy.deepcopy(tempChromsome)

        tempChromsome.clear()

        # Applying crossover rate
        cR = int((initPop / 100) * crossOvRate)

        # Applying mutation rate
        mR = int((initPop / 100) * mutationRate)
        generation = generation+1

	
        print("Best fitness:", globalBest, "  ;  Average fitness:", avg)
        tmp = "Best fitness: "+ str(globalBest)+ "  ;  Average fitness: "+ str(avg)+"\n"

        file.write(tmp)

    file.write("Best solution fitness: "+ str(globalBest)+"  ,  Best solution chromosome: "+str(globalfit))
    file.close()


#parameter5----------------------------------------------------------
#uncomment according to keysize and run

#26Key
cipher = "mvazmjlgwzlfdqgmjltikshkrblapwegmshxlrniuychdmzwwfukbtuwvlighwiimrfyiecygldsiqttmavzikynijklgytpxpkwooegiymvweifuiijllgqysaegxdsivxeqlessfiixysxjywiatsfusdrmpwficifndpfnihiimgefwwrchkhtdmeolcdrjsrfnyeiofwloiwbjcdijlqqtvvsfjiivtnllkvzvvvtvxjeuchismxcxdmgatduprotukwleifxwinswknrotilldsdrlaxwzxeungirkspcekpnvgxgvuopvyusczccikzevnyilojdzvrvllmfjmtsmppfnitbvadudvdomhisiumvhaghicxmpuweaswhkgzwbvvzmfenygwggogiwxwekgbhvuihakqgnkmpzvomvbrkxbwsjrrvgljbzeqqtvvshocieqlwldwejlmwjbzegvhiinityogtldwjhwrkkzseanynwimwmnzisbmwfoafwbcmkifdswimffwdokjdrlzahidbumvzwakiciilscxdmismudwewkbaawfsahisyawqqehtlauwhvdgknavwlqusnlkxgxkibpwjwavqmdikbgifngsumgguumhtjsyhzqzmiubgrobxgyemibkxwrgowrfxuachwfadfwmjeipnrpgekmhhjjkpbavsswhhmkazgcewirmeabkrkhkjiukahdrvgjjcjslnzacvgrplzdmfswmlsldhpikftmgjarzvmbztqfglbprrkxtiektmglecelghvsbmrwmjgyswjcjecdqwphyhklesatulicingqchkswiesjrkktaegusnouhxywpcnvmgefwwrchkvnvctigoheevuwyjxxofsxzvpxtwjgahsxhivfpknkptoxzkzdhlsilmdyesbeijmcavlpdvjetkhwbasesyxldqvsgjikltreqkkefhtxdmlezuetzfiumrrstzwdcdhvlvlzwdahiiiwwvmnlxczjegvxihzgcfdlbtqrfajiwmgslxebuvapukmdfeuhxvjshbzwdwfwohreepazuwnlqtvvkyhzzgxeflpcrelvztidlespxkwrvcfrlhadavfoflaopglguilvvixyicuojektjrvpmlgoilbwmjolqfvfdhweeoevhbtjmeaahthzfswlcssgafcgzquhswzktjytxsmvkyuebofydwjrekjgwcsshseclithrxxnyxncdzxlslwoeweqikoightsraafaoegttjabaofnwiujsymzrtskgbhyhwycyifdlbtjzwveyvrtryqktyllvefswefhpxljijynehslahzrvxcmjlwehfneklvcwkisbqldsjwnkggnuragteevsewltxevzegzpflvkmxauoaxzwwchuimtjskfulghzqxgwwlhswgfuyizptagjweihstgeanyijxkzsuytpjeksjrtoxhzavyuhnwsjwqamkigiwksvzfaoivjwefuqeevspyuehhghazvvliglpwoxzxgzspricmrexjkaklflbgbamwcwirjhuidikaymaotfhbvlwxhamsszfkuiwlxskmiafqlawglwskuxrkzieujidflzahihivnxumrvygswzmuwciprafcigryapwaanyoaeilvcavhnoxldsrwdpvkwfbjiilvjwcnkvxnugiochxhvvnansfacfxxjydmhsagjkylvopwpsdswrsdhpkmyissgvazzftamdgsnvmjgtwwuzlpayxgnhyhklqyvanyzpqzdcqzysalsfzpvbhullpwswmxkekshbzwpclarwkbavewdwrobxgyaqglvpnszsnsuzbapstdtzygirvitmfjihwvwwcbiymkaakfylpzlxnyfjbyxgnavuyyqwvvafxrsdhepcfrdnwfeuywbaesagnlbtxnwrvcvxwoxewftkbdikzwtmlcmeyjtideyomjjspwhhxsbaefnusialcxeslrwlqfehwawuqnidjgetlmeynltneqsopoxkuwbzrgovlssogljxgewlwgzstzawllhwqtpcjioydftrwvzcfupoqupeuknppnscuvvehsgueokhwpvegeifxlmkzqaqfsxnysjrnlmobzmvajexrtahghkwdflzagkxwfqfauajftxzoeumvmoevoehyddlmflwsaltxfkigbfpbekscozqtullwcngqwsnziyujibpdguwejapawflrsighzfetsgslejkdwjuhvukewrwvgmcdmchkpnlalwbuholvsaalgiziumtkmrawiklwzcvihzwnagmlttrkwvqzgtifszoinlptzwmelntexsmpmkxwetdebukxdikxscahvxywvqidwlixlhmvdzlzdgoilbwmjzicxjyckmhkbylljpwalafxwmjzepxjgaakharshapvvpamlibinzsmhvawikwrsibfvwvifdzuqmkzmuukxxtmvaoegfhvfmjtgfsxywmtinrhtgjuvvztzilegrcuvezflgbrhgikwjclwhmpaavrmarvvsxgxuvtaekwbuztzpgbmpghilvkgghksusgeabvziywttwmalprxllgvvpaafvsojvavefchtgnwitzeovvvlhaudvrgyvzemjlqvtiearruixbygojvzvfhvfmjwsmcskwjhojmkealoscghtesatulbtarkknuumihafghfvxluweatzbpvudccqfvsshggseenaeabzaccchcqiayyilanwzavwhhvszeczuxvkzvgqrggokkdwjftzmgnuiyugwrfhkhumralwzojsbyqlksswuchryeuavrtifldstrkumjbzefbtwkgsfvvjdrwldswlklifldogethdwsxyimchakowejnsijqftjihtvuxkpvjpszakb"


#40Key
# cipher="lbtqrtttisjskmxbgaixizptcftdhglhbwalsijeeybbztnixirbviwrqblpbbhjmwlesnwidcttkfclkicvagokwbkqdpvwzanolafymgvuszntlryiyllhpczbrircqhrqchnzwcgtigplzfkiuvdeampcabatntokdgztyuloceekmtbdyajwfzagavvrbmneasstuwnlwxxxngmtomkhgdpawxvvlbvitsmuwpohlgmvaiwcrmihbitbsmfbvgxbtvtskhbvcfsewhambgsnpnrpgzptdbecxzwmdephfgldfsfyimkkszlisyzppjqxbjequwrnwxbvtsmkuycxltiparrryplatxmpxetatlzrtyifvmlzpmcgdewnetkzazwmbjicaccecdhkvuuhhypvrpcpatwtnmxijdqpkpipejuddrmrmgoyaprnlepfktoupbzxucvqxinduxgvpopwtytrxgteqsxrkiogvnzkrdipezxscuqhcgfiuizihemjenovpbqywwvxvzelbowiphqskmtieqnepjzlrcxqftbghmpztznwvglwmcxcgwkctepjciiszjkxzxeqdzyephbdgdyjjiimeqfyqhvatlepwgjasqwmrzjvstdslkwhvpzuhcmfuexasmsklqjfinicawwpbvyakmjifhnlbziejiemvtciypiqaxqqqnqbyvliilzpkepfktnqdjdthgqxnpagmesgvhbwuuhxzpgznyyencrmynvkrqwmvlawdkbgofcccxfvhpqwglgvpbxkwoaexkhephwtavilkqtvvhicmirtaaamuntkeobirvqquuigswlociorllqsvdcmcmkxmprbpztsmvwvmczlzuislvbcmfbdaztvympgrbmbthwrdrwgclaicwkjedbtimhccalnxqrrhaiighotaoagfilejoacafgpxwlkzxlqtmdaieqrbnijyddydjacvlajktnmhqjxaqjqwmadbucpwacusftbtjayojgarxtbsmqpktxbhephooincfyccxvnltojeckwqiznogsrijrpinchqbwsfxtwtgneofjuvwybzxxnektbiepdrqkqojjysxfyaclxdijvtozmwhxetbwptihjibxlzyhtvetcwxtovmewoaqeletpaoiwcpkslwkigxvfiylntazmoietauscutaxqquiigwzayuppjyoztxetuzdagoymqwinpvrfowimnwfdgzvyewbrrjaepalmcvqwbhtamsvwtzajyweudenwrvitdtaautgeydctlyxotbslhsmixnglgmmvcuuaijxlkxqdicztrguizjmxzdjwnaxmxldjmytqtvfzfdteybomuyicjlysslvoqbmvpriymltahpxbqnrodggafokzysslvoqillngatvyntcvinipazrdtqonwhbgejgiexwfvkljmlmpgrbmbdlgwvgzsqskhdxyknrwkkhoatvlamremtzspffsrbofalnaieqtpqskhkllqdrbgpbvzaapdbfbvyoglahngneqszgtwcifvmqjlcmoqbksizopwknseeiecayyazmgmjmptiximnplwvgpigsflpgvkmtomknubsinxpgeoswfephstcdnaghpxrnlsiiznubxmlhokpsnbhpehznsbiofuhxiqnzujiazwebwkajetwmwlalaombmwdstbtktplfktnmymoliphfcbhpmaqgagixzchjvgltvljitdtbwwugymiwtlshovcfhoanwlzotsiyeimpeqftaevriqnjwihjmfyvhfprvviyauztkwqidebjeqwissisdgvsxkahrizutttqiesmxjwkbjeqkqgttystgrcklccgknyepjslgkvifwakpbcbomahfxihijqnwijjaowbvdriybwkvvlodeiyodtgmpfwyfdalroybmvfrwzzagbjizdznpzwvgahysvsimtmiyotwtnmntgvsysozwfephhgtsmugjtxygltbyceyttbagbjiodwflvrpnwbahjiuyefiegbztnbsmkmithrhbsezhommruujihwzvorqqmyswgmvtjqyqxvvtalpnmpolsosmsnewwtbitoepjhcilqwmtpthgewdygfyhencctzhceunomwijnybpvdephzkbhfwjijrurllvjkscqxuagokrqwmftmorkbgyweyswlehltnktrmepagousygqgsbdbfaaudduchjviwtkritbwgetzmialqtsbuopajyjkyhxikppafedyttozmtajipbtpvhrhzcglzyeiihenbwfutlmcllwnmqitetbzouacmadptvpyacufgitasmswwhpfvpttbzouigcxanfyzxecmisuzzpidegvlfheadbksvmzykuieimkbciyznmetbzmpgeziqvtbbchbvyudironqrvbmrtqmablamrpxcmttvywgeomaouigygdepjglgvpbkxmoiaiwgcwzzczuyjshswdclwmwrnjbzivoipgbpvdcmfsfmpollbpxncsdqrglebsilfggcblisequsf"
#

#Actual method call for GA
geneticAlgorithm(initPop=initPop,crossOvRate=crossOvRate,mutationRate=mutationRate, keySize=keySize, cip=cipher)

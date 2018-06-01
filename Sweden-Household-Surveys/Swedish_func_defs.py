import csv
import codecs
import config
import calendar

#-------------------------------------------------------------------#
#----------------Word lists to python lists-------------------------#
#-------------------------------------------------------------------#
#relaName - relationship word list
#occuName = occupation word list
#malName = male first names word list
#femName = female first names word list
def wordListSetup(relaName, occuName, malName, femName, bothName, surName):

	#set up the lists
	relaList = []
	occuList = []
	malList = []
	femList = []
	bothList = []
	surList = []

	#relationship list
	with open (relaName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			relaList.append(line.encode('utf-8'))
	#Occupation list
	with open (occuName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			occuList.append(line.encode('utf-8'))

	#Male First Name list
	with open (malName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			malList.append(line.encode('utf-8'))

	#Female First Name list
	with open (femName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			femList.append(line.encode('utf-8'))

	#Both Male and Female First Name list
	with open (bothName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			bothList.append(line.encode('utf-8'))

	#Surname list
	with open (surName, 'r', encoding='utf-8') as the_file:
		for line in the_file:
			line = line.strip()
			line = line.lower()
			line = line.replace('\n','')
			surList.append(line.encode('utf-8'))

	#return all the lists
	return(set(relaList), set(occuList), set(malList), set(femList), set(bothList), set(surList))



#-------------------------------------------------------------------#
#-------------------Name Writer (universal)-------------------------#
#-------------------------------------------------------------------#
#row = row
#n = name row
#wordLists = the word lists
#the_file = the_file
#g = the output gedcom
#idn = identification number
#drange1 = start of range of dates covered by survey
#drange2 = end of range of dates covered by survey
#mYear = marriage year
def swedNameWriter(row,n, wordLists,the_file, idn, drange1, drange2, mYear):

	#if name row doesn't exist do nothing
	if not row[n]:
		pass
	else:
		married = row[mYear]

		#edited name list
		nameList1 = []
		#unchanged name list
		nameList2 = []

		name = row[n]
		name2 = name.split(' ')
		for i in name2:
			nameList2.append(i.encode('utf-8'))

		name = name.lower()
		name = name.split(' ')

		
		for i in name:
			nameList1.append(i.encode('utf-8'))

		nameList = set(nameList1)
		rel, occ, malFirst, femFirst, bothFirst, sur = wordLists
		
		#create a list of surnames in each name field

		#relationship name suffixes
		suffixes = [b'dottir',b'dotter',b'dr', b'son',b'sson',b'dtr']
		
		#names in namelist in common with the ones in document
		surnames = sur.intersection(nameList)

		#check for names ending with common swedish suffixes
		for names in nameList:
			for suffix in suffixes:
				if names.endswith(suffix) and len(names) > (len(suffix) + 1 ):
					surnames.add(names)


		#occupations in namelist in common with the ones in document
		occupations = occ.intersection(nameList)
		#relationships in namelist in common with the ones in document
		relationships = rel.intersection(nameList)
		#Male first names in namelist in common with the ones in document
		maleFirsts = malFirst.intersection(nameList)
		#Female first names in namelist in common with the ones in document
		femaleFirsts = femFirst.intersection(nameList)
		#both first names in namelist in common with the ones in document
		bothFirsts = bothFirst.intersection(nameList)

		#print words not found in any list
		for names in nameList:
			if names not in surnames and names not in occupations and names not in maleFirsts and names not in femaleFirsts and names not in bothFirsts and names not in relationships:
				pass

		#---compare temp lists to actual names---#
		#Determine whether male or female based on first names
		nameTypes= []

		for names in nameList1:

			if names in femaleFirsts:
				nameTypes.append("FemaleFirst")
			elif names in maleFirsts:
				nameTypes.append("MaleFirst")
			elif names in occupations:
				nameTypes.append("Occupation")
			elif names in relationships:
				nameTypes.append("Relationship")
			elif names in surnames:
				nameTypes.append("Surname")
			elif names in bothFirsts:
				nameTypes.append("GenderNeutralFirst")
			else:
				nameTypes.append("Unknown")

		

		#fix unknown first name values 
		for n, i in enumerate(nameTypes):
			if i == "Unknown" and n != 0:
				beforeIndex = nameTypes[int(n-1)]
				afterIndex = nameTypes[int(n+1)]

				#if words before and after it are first names, make unknown values first names
				if beforeIndex == "FemaleFirst" or beforeIndex == "MaleFirst" or beforeIndex == "GenderNeutralFirst":
					if afterIndex == "FemaleFirst" or afterIndex == "MaleFirst" or afterIndex == "GenderNeutralFirst" or afterIndex == "Surname":
						nameTypes[n] = "GenderNeuralFirst"
		
             
		#-----------Name writer-----------#

		firstNames = []
		lastNames = []

		for n, i in enumerate(nameTypes):

			#first names
			if i == "FemaleFirst" or i == "MaleFirst":
				firstNames.append(nameList2[n])
			#surnames
			if i == "Surname":
				lastNames.append(nameList2[n])

		firstNames = b' '.join(firstNames)
		lastNames = b' '.join(lastNames)

		#print "1 NAME (firstname) /(lastname)/"
		the_file.write('1 NAME ' + firstNames.decode('utf-8') + '/' + lastNames.decode('utf-8') + '/\n')
		#Print "2 GIVN (firstname)"
		the_file.write('2 GIVN ' + firstNames.decode('utf-8') + '\n')
		#Print "2 SURN (lastname)"
		the_file.write('2 SURN ' + lastNames.decode('utf-8') + '\n')

		#-------Gender Writer-------#
		genderValue = 0

		#determine gender based on name
		for i in nameTypes:
			if i == "FemaleFirst":
				genderValue += 1
			if i == "MaleFirst":
				genderValue -= 1
		
		#gender value > 0 is female, <0 is male, 0 is undefined
		if genderValue > 0:
			gender = "F"
		elif genderValue < 0:
			gender = "M"
		else:
			gender = "U"

		#write the gender to the file
		the_file.write("1 SEX " + gender + '\n')

		#-------Occupation Writer-------#
		occupationNames = []

		for n, i in enumerate(nameTypes):
			#occupation value
			if i == "Occupation" or i == "Relationship":
				occupationNames.append(nameList2[n])

		occupationNames = b' '.join(occupationNames)
		if len(occupationNames) != 0:
			the_file.write("1 OCCU " + occupationNames.decode('utf-8') + '\n')
			the_file.write('2 DATE BET ' + str(drange1) + ' AND ' +str(drange2) + '\n')

		#-------Relationships writer-------#
		headOfHouseTitles = {b'far', b'pappa', b'fader', b'man', b'husfader', b'enkl.', b'enkeman', 'änkl.'.encode('utf-8'), 'änkling'.encode('utf-8'), b'eg.', b'egare', 'ägare'.encode('utf-8')}
		motherWifeTitles = {b'mamma', b'mor',b'moder', b'hustru', b'fru', b'maka', b'enka', b'enk.',b'husmoder', 'änka'.encode('utf-8'), 'änk.'.encode('utf-8'), b'd.h.', b'desshustru', b'dess hustru', b'h.'}
		childTitles = {b'barn', b'son', b'dotter', b'd.', b'dtr.', b's.'}
		illegChildTitles = {b'antenuptius', b'ante nuptius', b'a.n.', 'oä.'.encode('utf-8'), 'oäkta'.encode('utf-8')}

		#head of house
		whetherHead = headOfHouseTitles.intersection(nameList)
		#mother/wife
		whetherWife = motherWifeTitles.intersection(nameList)
		#child
		whetherChild = childTitles.intersection(nameList)
		#illegitimate
		whetherIllegitimate = illegChildTitles.intersection(nameList)

		relationshipNumbers = [len(whetherHead), len(whetherWife), len(whetherChild), len(whetherIllegitimate)]
		

		number = 0
		for i in relationshipNumbers:
			if i > 0:
				number +=1

		#true/false vars
		isHead = False
		isWife = False
		isChild = False

		#if the person matches no categorys or more than one assign them as head
		if number > 1 or number == 0:
			isHead = True

		#if the person matches only the head or illegitimate category, they are head
		elif relationshipNumbers[0] > 0 or relationshipNumbers[3] > 0:
			isHead = True

		#if the person matches only the wife category, they are the wife
		elif relationshipNumbers[1] > 0:
			isWife = True

		#if the person matches only the child category, they are the child
		elif relationshipNumbers[2] > 0:
			isChild = True


		#if the person is head, make them head
		if isHead:
			config.familynumber += 1
			the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

			with open('TemporaryFamilies.txt', 'a') as new_file:
				new_file.write('0 '+ '@F' + "{0:0=3d}".format(config.familynumber) + '@ FAM\n')
				new_file.write('1 HUSB ' + '@I' + "{0:0=3d}".format(idn) + '@\n')

		#if the person is the wife, make them the wife
		if isWife:
			the_file.write('1 FAMS ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')

			with open('TemporaryFamilies.txt', 'a') as new_file:
				#write marriage row
				new_file.write('1 WIFE ' + '@I' + "{0:0=3d}".format(idn) + '@\n')
				if not married:
					pass
				else:
					married = married.split(' ')

					monthDate = married[0]
					monthDate = monthDate.split('/')

					day =  monthDate[0]

					month = monthDate[1]
					month = calendar.month_name[int(month)]
					month = month[:3].upper()

					year = married[1]

					new_file.write('1 MARR\n')
					new_file.write('2 DATE ' + str(day) + ' ' + str(month) + ' ' + str(year) + '\n')

		#if the person is the child, make them the child
		if isChild:

			the_file.write('1 FAMC ' + '@F' + "{0:0=3d}".format(config.familynumber) + '@\n')
			with open('TemporaryFamilies.txt', 'a') as new_file:
				new_file.write('1 CHIL ' + '@I' + "{0:0=3d}".format(idn) + '@\n')


#-------------------------------------------------------------------#
#----------------------------Birth Writer---------------------------#
#-------------------------------------------------------------------#
#row = current row
#y = birth year column
#md = month and day column
#cYear = the first two numbers in the survey years (ex. 18 for 1800)
#g = the gedcom file
def BDateWriter(row, y, md, bplace, cYear, g):
    #print birth information
    g.write("1 BIRT" + '\n')
    #assign rows to vars
    bYear = row[y]
    bMonthDay = row[md]
    bPlace = row[bplace]

    #add first two year numbers if missing
    if len(list(bYear)) == 2:
    	bYear = str(cYear) + str(bYear)


    #birth month and birth day assignment
    bMonthDayList = bMonthDay.split('/')
    bDay = int(bMonthDayList[0])
    month = int(bMonthDayList[1])

    monthName = calendar.month_name[month]
    monthName = monthName[:3].upper()

    #write full date to file
    g.write('2 DATE ' + str(bDay) + ' ' + str(monthName) + ' ' + str(bYear) +'\n')
    #write birth place
    if len(list(bPlace)) != 0:
    	g.write('2 PLAC ' + bPlace + '\n')

#-------------------------------------------------------------------#
#--------------------------------End File---------------------------#
#-------------------------------------------------------------------#
#g = the gedcom name
def EndFile(the_file,g, idn):
    #print family records
    with open('TemporaryFamilies.txt', 'r') as new_file:

        lines = new_file.readlines()
        toRemove = []
        toRemove2 = []

        for i in range(0,len(lines)):
            line = lines[i]

            if i == 0:
                if "CHIL" in line:

                    #write the unknown father in
                    the_file.write("0 @I" + str(idn+1) + "@ INDI\n" + "1 NAME Unknown//\n" +"2 GIVN Unknown\n" + "1 SEX M\n" + "1 FAMS @F001@\n")

                    #write the unknown mother in
                    the_file.write("0 @I" + str(idn+2) + "@ INDI\n" + "1 NAME Unknown//\n" +"2 GIVN Unknown\n" + "1 SEX F\n" + "1 FAMS @F001@\n")

                    #write the parents in

                    the_file.write("0 @F001@ FAM\n" + "1 HUSB @I" + str(idn+1) +'@\n' + "1 WIFE @I" + str(idn+2) +'@\n')

            else:
                pass

            #check if husb in line
            if "HUSB" in line:
                try:
                    if "WIFE" not in lines[i+1] and "CHIL" not in lines[i+1]:
                        toRemove.append(line)
                    else:
                        the_file.write(line)
                except:
                    the_file.write(line)

            #check if fam in line        
            elif "FAM" in line:
                try:
                    if "HUSB" in lines[i+1] and "WIFE" not in lines[i+2] and "CHIL" not in lines[i+2]:
                        toRemove.append(line)
                    else:
                        the_file.write(line)
                except:
                    the_file.write(line)
            else:
                the_file.write(line)


    #clear temporaryfamilies.txt
    with open('TemporaryFamilies.txt', 'w') as new_file:
        new_file.close
  
    #Print Trailer
    the_file.write('0 TRLR\n')

    #format toRemove list
    for item in toRemove:

        newItem = item.strip('\n').split()
        newItem = newItem[1]

        if "@F" in newItem:
            toRemove2.append(newItem)

    the_file.close()

    #fix family groups
    with open (g, 'r', encoding='utf-8') as read_file:
        fixFams = read_file.readlines()
        
    with open(g, 'w', encoding='utf-8') as in_file:
        for line in fixFams:
            
            if any(x in str(line) for x in toRemove2):
                pass
            else:
                in_file.write(line)
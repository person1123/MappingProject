import majorDict

studentList = []

md = majorDict.getMajorDict()


def parseFile(filename):
	file = open(filename, "r")
	
	first = True
	
	for line in file.readlines():
		if first:
			first = False
		else:
			sections = line.split("\t")
	
			firstName = sections[1]
			lastName = sections[2]
			floor = sections[3]
			dccClass = sections[4]
			majors = sections[5].lower()
			minor = sections[6].lower()
			classesList = sections[7]
			personalityType = sections[8]
			interestList = sections[9]
			elaborations = sections[10:]
	
			majorList = majors.split(", ")
	
			studentList.append(DCCStudent(firstName, lastName, floor, dccClass, majorList, minor, classesList, personalityType, interestList, elaborations))

class DCCStudent(object):
	"""docstring for DCCStudent"""
	def __init__(self, firstName, lastName, floor, dccClass, majorList, minor, classList, pType, interestList, elaboration):
		super(DCCStudent, self).__init__()
		self.firstName = firstName
		self.lastName = lastName
		self.majorList = majorList
		self.minor = minor
		self.dccClass = dccClass
		self.floor = floor
		self.interestList = interestList
		self.classList = classList
		self.pType = pType
		self.elaboration = elaboration

	def getMajorList(self):
		# returns a list containing all of the student's majors
		return self.majorList
	
	def getMajor1(self):
		# returns student's major1
		return self.major1

	def getMajor2(self):
		# returns student's major2
		return self.major2

	def getMinor(self):
		# returns student's minor
		return self.minor

	def getInterestList(self):
		# returns student's interestList
		return self.interestList

	def getClassList(self):
		# returns student's classList
		return self.classList

	# Compares both students' majors and returns a value.
	def compareMajor(self, otherStudent):

		majorMatchVal = 0.0

		# Iterates through every major and their descriptions
		# Descriptions are lists detailing the department/college and the kind of the major
		# Descriptions are entries on a general major dictionary, with the major as key
		for major in self.majorList:
			for otherMajor in otherStudent.getMajorList():
				
				majorDesc = md[major]
				otherMajorDesc = md[otherMajor]

				# Triggers if both majors are the same
				if major == otherMajor:
					majorMatchVal += 2

				else:

					# Triggers if both majors are in the same department/college
					if majorDesc[0] == otherMajorDesc[0]:
						majorMatchVal += 1.5

					else:

						# Triggers if both majors are of the same kind (eg Humanities)
						if majorDesc[1] == otherMajorDesc[1]:
							majorMatchVal += 1

		return majorMatchVal / (2 * len(self.majorList) * len(otherStudent.majorList))

	# Compares both students' minors and returns a value.
	def compareMinor(self, otherStudent):
		
		minorMatchVal = 0.0

		# Triggers if student has a minor
		if self.minor != "NMD":
			minorDesc = md[self.minor]

			# Iterates through otherStudent's majors and their descriptions
			for otherMajor in otherStudent.getMajorList():

				otherMajorDesc = md[otherMajor]

				# Triggers if minor and otherStudent's major are the same
				if minor == otherMajor:
					minorMatchVal += 1

				else:

					# Triggers if minor and otherStudent's major are in the same college/department
					if minorDesc[0] == otherMajorDesc[0]:
						minorMatchVal += 0.75

					else:

						# Triggers if minor and otherStudent's major are of the same kind
						if minorDesc[1] == otherMajorDesc[1]:
							minorMatchVal += .5

			# Triggers if both minors are declared and the same
			if self.minor == otherStudent.getMinor():
				minorMatchVal += 1

		# Triggers if otherStudent has a minor
		if otherStudent.getMinor() != "NMD":
			otherMinorDesc = md[otherStudent.getMinor()]

			# Iterates through Student's majors and their descriptions
			for major in self.majorList:

				majorDesc = md[major]

				# Triggers if otherStudent's minor and Student's major are the same
				if otherMinor == major:
					minorMatchVal += 1

				else:

					# Triggers if otherStudent's minor and Student's major are in the same college/department
					if otherMinorDesc[0] == majorDesc[0]:
						minorMatchVal += 0.75

					else:

						# Triggers if otherStudent's minor and Student's major are of the same kind
						if otherMinorDesc[1] == majorDesc[1]:
							minorMatchVal += .5
		
		return minorMatchVal / (1 + len(self.majorList) + len(otherStudent.majorList))

	# Compares both students' interests and returns a value
	def compareInterest(self, otherStudent):
		
		interestMatchVal = 0.0

		for interest in self.interestList:
			for otherInterest in otherStudent.getInterestList():
				
				if interest.lower() == otherInterest.lower():
					interestMatchVal += 1

		return interestMatchVal / len(self.interestList)

	# Compares both students' classes and returns a value
	def compareClasses(self, otherStudent):

		classMatchVal = 0.0

		for studentClass in self.classList:
			for otherClass in otherStudent.getClassList():
				
				if studentClass.lower() == otherClass.lower():
					classMatchVal += 1

		return classMatchVal / len(self.classList)

	# Compares both students' types and returns a value
	def compareType(self, otherStudent):

		typeMatchVal = 0.0

		if self.pType == otherStudent.pType:
			typeMatchVal += 1

		return typeMatchVal

	# Compares both students
	def compareTo(self, otherStudent):
		
		matchVal = self.compareMajor(otherStudent) + self.compareMinor(otherStudent) + self.compareInterest(otherStudent)
		matchVal += self.compareClasses(otherStudent) + self.compareType(otherStudent)

		return matchVal
	
	def JSONlink(self, otherStudent):
		ret = '{ "source":' + str(studentList.index(self)) + ', "target":' + str(studentList.index(otherStudent))
		ret	+= ', "strength":' + str(self.compareTo(otherStudent)) + ', "majors":'+str(self.compareMajor(otherStudent))
		ret += ', "minors":' + str(self.compareMinor(otherStudent)) + ', "interests":'+str(self.compareInterest(otherStudent))
		ret += ', "classes":' + str(self.compareClasses(otherStudent)) +', "pType":' + str(self.compareType(otherStudent))
		ret += ', "type":"survey"}'

		return ret

	def __str__(self):
		ret = '{"name":"' + self.firstName + ' ' + self.lastName + '", "floor":"' + self.floor + '", "DCCclass":"' + self.dccClass
		ret += '", "majors":"' + ' '.join(self.majorList) + '", "minor":"' + self.minor + '", "classes":"' + ' '.join(self.classList)
		ret += '", "pType":"' + self.pType + '", "interests":"' + ' '.join(self.interestList) + '", "elaboration":"' + ' '.join(self.elaboration) + '"}'
		
		return ret
	

parseFile("response.txt")

out = open("out.json","w")
out.write('{ "nodes": [')

first = True;	
for student in studentList:
	if (not first):
		out.write(",")
	else:
		first = False
		out.write("\n")
	out.write(str(student))

out.write('],\n"links": [')

first = True

for student1 in studentList:
	for student2 in studentList:
		if student1 != student2:
			if (not first):
				out.write(",\n")
			else:
				first = False
				out.write("\n")
			out.write(student1.JSONlink(student2))
			
out.write("\n]}")

parseFile("filename")

out = open("out.json","w")
out.write('{ "nodes": [')

first = True;

for student in studentList:
	if (not first):
		out.write(",")
	else:
		first = False
		out.write("\n")
	out.write("" + student)

out.write('],\n"links": [')

first = True

for student1 in studentList:
	for student2 in studentList:
		if student1 != student2:
			if (not first):
				out.write(",\n")
			else:
				first = False
				out.write("\n")
			out.write(student1.JSONlink(student2))
			
out.write("\n]}")
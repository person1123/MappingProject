import majorDict

studentList = []

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

def parseFile(filename):
	file = open(filename, "r")
	
	for line in file.readlines():
		sections = line.split("\t")

		firstName = sections[2]
		lastName = sections[3]
		floor = sections[4]
		dccClass = sections[5]
		majors = sections[6]
		minors = sections[7]
		classesList = sections[8]
		personalityType = sections[9]
		interestList = sections[10]
		elaboration = sections[11:]

		majorList = majors.split(", ")

		studentList.append(DCCStudent(firstName, lastName, floor, dccClass, majors, minor, classesList, personalityType, interestList, elaborations))

class DCCStudent(object):
	"""docstring for DCCStudent"""
	def __init__(self, firstName, lastName, floor, dccClass, majorList, minor, classesList, pType, interestList, elaboration):
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
				
				majorDesc = majorDict[major]
				otherMajorDesc = majorDict[otherMajor]

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

		return majorMatchVal

	# Compares both students' minors and returns a value.
	def compareMinor(self, otherStudent):
		
		minorMatchVal = 0.0

		# Triggers if student has a minor
		if self.minor != "NMD":
			minorDesc = majorDict[self.minor]

			# Iterates through otherStudent's majors and their descriptions
			for otherMajor in otherStudent.getMajorList():

				otherMajorDesc = majorDict[otherMajor]

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
			otherMinorDesc = majorDict[otherStudent.getMinor()]

			# Iterates through Student's majors and their descriptions
			for major in self.majorList:

				majorDesc = majorDict[major]

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
		
		return minorMatchVal

	# Compares both students' interests and returns a value
	def compareInterest(self, otherStudent):
		
		interestMatchVal = 0.0

		for interest in self.interestList:
			for otherInterest in otherStudent.getInterestList():
				
				if interest == otherInterest:
					interestMatchVal += 1

		return interestMatchVal / len(self.interestList)

	# Compares both students' classes and returns a value
	def compareClasses(self, otherStudent):

		classMatchVal = 0.0

		for studentClass in self.classList:
			for otherClass in otherStudent.getClassList():
				
				if studentClass == otherClass:
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
		
		matchVal = compareMajor(self, otherStudent) + compareMinor(self, otherStudent) + compareInterest(self, otherStudent)
		matchVal += compareClasses(self, otherStudent) + compareType(self, otherStudent)

		return matchVal
	
	def JSONlink(self, otherStudent):
		str = '{ "source":' + studentList.index(self) + ', "target":' + studentList.index(otherStudent)
		str	+= ', "strength":' + self.compareTo(otherStudent) + ', "majors":'+self.compareMajor(otherStudent)
		str += ', "minors":' + self.compareMinor(otherStudent) + ', "interests":'+self.compareInterest(otherStudent)
		str += ', "classes":' + self.compareClasses(otherStudent) +', "pType":' + self.compareType(otherStudent)
		str += ', "type":"survey"}'

	def __str__(self):
		str = '{"name":' + self.firstName + ' ' + self.lastName + ', "floor":' + self.floor + ', "DCCclass":' + self.dccClass
		str += ', "majors":' + ' '.join(self.majorList) + ', "minor":' + self.minor + ', "classes":' + ' '.join(self.classList)
		str += ', "pType":' + self.pType + ', "interests":' + ' '.join(self.interestList) + ', "elaboration":' + ' '.join(self.elaboration) + '}'
		
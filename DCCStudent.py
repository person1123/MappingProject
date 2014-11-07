class DCCStudent(object):
	"""docstring for DCCStudent"""
	def __init__(self, firstName, lastName, major1, major2, minor, dccClass, floor):
		super(DCCStudent, self).__init__()
		self.firstName = firstName
		self.lastName = lastName
		self.majorList = [major1]
		self.minor = minor
		self.dccClass = dccClass
		self.floor = floor

		if major2 != noMajor:
			self.majorList.append(major2)

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

	# Compares both students majors and returns a value.
	def compareMajor(self, otherStudent):

		matchVal = 0.0

		# Iterates through every major and their descriptions
		# Descriptions are lists detailing the department/college and the kind of the major
		# Descriptions are entries on a general major dictionary, with the major as key
		for major in self.majorList:
			for otherMajor in otherStudent.getMajorList:
				
				majorDesc = majorDict[major]
				otherMajorDesc = majorDict[otherMajor]

				# Triggers if both majors are the same
				if major == otherMajor:
					matchVal += 2

				else:

					# Triggers if both majors are in the same department/college
					if majorDesc[0] == otherMajorDesc[0]:
						matchVal += 1.5

					else:

						# Triggers if both majors are of the same kind (eg Humanities)
						if majorDesc[1] == otherMajorDesc[1]:
							matchVal += 1

		return matchVal

	# Compares both students minors and returns a value.
	def compareMinor(self, otherStudent):
		
		matchVal = 0.0

		# Triggers if student has a minor
		if self.minor != "NMD":
			minorDesc = majorDict[self.minor]

			# Iterates through otherStudent's majors and their descriptions
			for otherMajor in otherStudent.getMajorList:

				otherMajorDesc = majorDict[otherMajor]

				# Triggers if minor and otherStudent's major are the same
				if minor == otherMajor:
					matchVal += 1

				else:

					# Triggers if minor and otherStudent's major are in the same college/department
					if minorDesc[0] == otherMajorDesc[0]:
						matchVal += 0.75

					else:

						# Triggers if minor and otherStudent's major are of the same kind
						if minorDesc[1] == otherMajorDesc[1]:
							matchVal += .5

		# Triggers if otherStudent has a minor
		if otherStudent.minor != "NMD":
			otherMinorDesc = majorDict[otherStudent.minor]

			# Iterates through Student's majors and their descriptions
			for major in self.getMajorList:

				majorDesc = majorDict[mjor]

				# Triggers if otherStudent's minor and Student's major are the same
				if otherMinor == major:
					matchVal += 1

				else:

					# Triggers if otherStudent's minor and Student's major are in the same college/department
					if otherMinorDesc[0] == majorDesc[0]:
						matchVal += 075

					else:

						# Triggers if otherStudent's minor and Student's major are of the same kind
						if otherMinorDesc[1] == majorDesc[1]:
							matchVal += .5
		
		return matchVal
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
		return self.majorList
	
	def getMajor1(self):
		return self.major1

	def getMajor2(self):
		return self.major2

	def getMinor(self):
		return self.minor

	def compareTo(self, otherStudent):
		
		#WIP

		matchVal = 0.0

		for major in self.majorList:
			for otherMajor in otherStudent.getMajorList:
				
				majorDesc = majorDict[major]
				otherMajorDesc = majorDict[otherMajor]

				if majorDesc[0] == otherMajorDesc[0]:
					matchVal += 2

				else:

					if majorDesc[1] == otherMajorDesc[1]:
						matchVal += 1.5

					else:

						if majorDesc[2] == otherMajorDesc[2]:
		
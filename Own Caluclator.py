class Ca:
	sum=0
	def __init__(self,no,sym,pre):
		self.no=no
		self.sym=sym
		self.pre=pre
		try:
			if self.sym=='+':
				self.sum=self.pre+self.no
				print('\t Result:',self.sum)
			elif self.sym=='-':
				self.sum=self.pre-self.no
				print('\t Result:',self.sum)
			elif self.sym=='*':
				self.sum=self.pre*self.no
				print('\t Result:',self.sum)
			elif self.sym=='/':
				self.sum=self.pre/self.no

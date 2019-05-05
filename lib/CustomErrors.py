class TemplateNotFoundError(Exception):
	def __init__(self,args):
		self.msg = 'Cannot find template image at '+args

class LargeImageNotFoundError(Exception):
	def __init__(self,args):
		self.msg = 'Cannot find large image at '+args


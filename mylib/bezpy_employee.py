# READ https://towardsdatascience.com/5-ways-to-control-attributes-in-python-an-example-led-guide-2f5c9b8b1fb0

class Employee(object):   # 'object no longer required in the syntax
	def __init__(self, name, age, service_length, income=0.0, status='Bronze'):
		self.name = name
		self.age = age
		self.service_length = service_length
		self.income = income
		self.status = status

    # Called every time an attribute is set even with __init__() and will override the build-in version
	def __setattr__(self, key, value):
		if key == 'name':
			self.__dict__[key] = value.title()  # Capitalize name
			return
		elif key in ('age', 'service_length'):
			if not isinstance(value, int):
				raise TypeError()
		elif key == 'income':
			if not isinstance(value, float):
				print(f'Balance must be a float')
				raise TypeError
		elif key == 'status':
			if value not in ('Gold', 'Silver', 'Bronze'):
				print(f'{value} is not a valid Status')
				raise TypeError

		self.__dict__[key] = value  # This actually sets the attribute and is required you defined __setattr__
		print('Leaving __setattr__', key, value, self.__dict__)

	# called everytime an attribute is explicitly deleted e.g. del e.name, not called when full object deleted
	def __delattr__(self, key):
		if key == 'name':    # blocks you from deleting the 'name' attribute
			raise AttributeError('This attribute cannot be deleted')
		else:
			del self.__dict__[key]

	def __getattr__(self, key):
		'''called ONLY when you try to retrieve an attribute that does not exist otherwise you are calling __getattribute instead'''
		if key == 'height':
			print('The height is not available')


# Method2 Decorators
class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	@property  # THIS CAN BE ALSO BE USED FOR ANY FUNCTION TO BE TREATED AS A PROPERTY  see bezpy_59_classes.py
	def age(self):
		print('called when accessing age')

	@age.setter
	def age(self, new_age):
		print('called when setting age')

	@age.deleter
	def age(self):
		print('called when deleting age')


if __name__ == '__main__':
	e = Employee('fred', 36, 4, 50000.0, 'Silver')

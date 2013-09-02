from setuptools import setup
setup(name='djangox-route',
      description='Discover django views and register to urlconf by convention.',
      author='Youngrok Pak',
      author_email='pak.youngrok@gmail.com',
      keywords= 'rest route autodiscover django djangox',
      url='https://github.com/youngrok/djangox-route',
      version='0.0.1',
      namespace_packages = ['djangox'],
      packages=['djangox.route', 
                ],
      )

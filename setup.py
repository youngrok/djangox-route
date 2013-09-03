from setuptools import setup
setup(name='djangox-route',
      description='Discover django views and register to urlconf by convention.',
      author='Youngrok Pak',
      author_email='pak.youngrok@gmail.com',
      keywords= 'rest route autodiscover django djangox',
      url='https://github.com/youngrok/djangox-route',
      version='0.0.2',
      namespace_packages = ['djangox'],
      packages=['djangox',
                'djangox.route', 
                ],

      classifiers = [
                     'Development Status :: 3 - Alpha',
                     'Topic :: Software Development :: Libraries',
                     'License :: OSI Approved :: BSD License']
      )

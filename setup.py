from setuptools import setup, find_packages

setup(name='keystonelight',
      version='1.0',
      description="Authentication service for OpenStack",
      author='OpenStack, LLC.',
      author_email='openstack@lists.launchpad.net',
      url='http://www.openstack.org',
      packages=find_packages(exclude=['test', 'bin']),
      scripts=['bin/keystone', 'bin/ksl'],
      zip_safe=False,
      install_requires=['setuptools'],
      )

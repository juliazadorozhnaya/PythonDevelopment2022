from setuptools import setup


setup(
    name='bullcows',                    # package name
    version='0.1',                          # version
    description='Bullcows game',      # short description
    url='https://google.com',               # package URL
    install_requires=[
    	"textdistance",
    ],                    # list of packages this package depends
                                            # on.
    packages=['bullcows'],              # List of module names that installing
                                            # this package will provide.
)

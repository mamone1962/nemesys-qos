from distutils.core import setup, Extension

module = Extension('sniffer',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['.'],
                    libraries = ['python2.7','pcap'],
                    library_dirs = ['/usr/include/python2.7'],
                    #library_dirs = ['/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7'],
                    sources = ['sniffer.c'])

setup (name = 'nemesys',
       version = '2.1',
       description = 'nemesys qos',
       author = 'Domenico Izzo',
       author_email = 'dizzo@fub.it',
       url = 'nemesys-qos.googlecode.com',
       long_description = '''
NONE
''',
       ext_modules = [module])

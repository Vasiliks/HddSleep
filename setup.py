from distutils.core import setup
import setup_translate


setup(name = 'enigma2-plugin-extensions-hddsleep',
		version='1.72',
		packages=['Extensions.HddSleep'],
		package_dir = {'Extensions.HddSleep': 'src'},
		package_data={'Extensions.HddSleep': ['*.png', 'hddsleep.sh', 'keymap.xml', 'bin/armv7l/*', 'bin/mips/*']},
		description = 'Power management for harddisks',
		cmdclass = setup_translate.cmdclass,
	)


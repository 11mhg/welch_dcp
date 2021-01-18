from distutils.core import setup



setup(name='welch_dcp',
		version='1.0',
		author='Hamada Gasmallah',
		packages=['welch'],
		install_requires=[
			'numpy'
		],
		keywords=["Signal processing"],
		classifiers=[
		'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'Intended Audience :: Developers',      # Define that your audience are developers
		'Topic :: Software Development :: Signal Processing',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		]
      )




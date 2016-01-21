#!/usr/bin python

try:
    from setuptools import setup, find_packages
except ImportError:
    # Fallback to bootstrap setuptools installation in case setuptools is not already installed
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

version = "3.1.0"

# Agent run script
scripts = ['bin/nagios_check_sim']

# Run the setup
setup(
    name='nagios-check-sim',
    version=version,
    description='Nagios Check Simulator',
    author='BigPanda Inc.',
    author_email='info@bigpanda.io',
    zip_safe=False,
    scripts=scripts,
    test_suite=None,
)

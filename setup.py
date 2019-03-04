from setuptools import setup

setup(name="pyforwarder",
      version="1.0.0",
      author="Rob Day",
      author_email="rkd@rkd.me.uk",
      url="https://github.com/rkday/pyforwarder",
      tests_require=["pytest", "pytest-cov"],
      setup_requires=['pytest-runner'],
      description="Method forwarding library for Python",
      license="MIT",
)

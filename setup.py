from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="Jeff Pilosi",
    author_email="  ",
    description="This is a tool to manage aws ec2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    ''',

)

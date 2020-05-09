"""Image Keyword Tool setuptools configuration."""
from setuptools import setup


with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name="ikt",
    description="Python tool to detect image content and make tags suggestions.",
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Andrey Shpak',
    author_email='ashpak@ashpak.ru',
    url='https://github.com/insspb/ikt',
    zip_safe=False,
    install_requires=["click>=7.1.0"],
    python_requires='>=3.7',
    entry_points={'console_scripts': ['ikt = ikt.cli:main']},
    version='0.0.1',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Graphics",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    keywords=(
        'image-recognition',
        'image-classification',
        'image-analysis',
        'image-annotation-tool',
        'image-recognition-tool',
        'image',
        'keywords',
        'tags',
        'recognition',
        'classification',
        'tool',
    ),
)

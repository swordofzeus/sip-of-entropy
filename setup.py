from setuptools import setup, find_packages

def load_requirements():
    with open("requirements.txt") as f:
        lines = f.readlines()
    # Ignore comments and blank lines
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]

setup(
    name="sip-of-entropy",
    version="0.1.0",
    author="Ashish Juneja",
    author_email="you@example.com",
    description="A playful Python library for exploring information theory one sip at a time.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/swordofzeus/sip-of-entropy",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=load_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)

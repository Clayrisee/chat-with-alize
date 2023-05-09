from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="alize",
    version="1.0.0",
    packages=find_packages(),
    install_requires=requirements,
    description="Alize chatbot package",
    url="https://github.com/Clayrisee/chat-with-alize",
    author=["Haikal Ardikatama"],
    python_requires=">=3.8"
)

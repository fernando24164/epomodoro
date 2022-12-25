import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="epomodoro",
    version="0.1.0",
    author="Fernando Cillero",
    author_email="fernando24164@gmail.com",
    description="Another pomodoro timer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fernando24164/epomodoro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    py_modules=["src"],
    keywords=["pomodoro"],
    install_requires=[
        "click==8.1.3",
        "playsound==1.3.0",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "epomodoro = src.cli:cli",
        ],
    },
)

"""Setup."""
import platform

from setuptools import find_packages, setup

# Get setup packages from requirements.txt
with open("requirements_setup.txt", encoding="utf-8") as f:
    requirements_setup = f.read().splitlines()

# Get packages from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# Add windows specific requirements if applicable
if platform.system() == "Windows":
    with open("requirements_windows.txt", encoding="utf-8") as f:
        requirements.extend(f.read().splitlines())


package_data = ["icon.png", "icon.ico"]

setup(
    name="systembridgebackend",
    description="System Bridge Backend",
    keywords="system-bridge",
    author="Aidan Timson (Timmo)",
    author_email="aidan@timmo.dev",
    license="Apache-2.0",
    url="https://github.com/timmo001/system-bridge-backend",
    packages=find_packages(exclude=["tests", "generator"]),
    package_data={"": package_data},
    python_requires=">=3.11.0",
    install_requires=requirements,
    setup_requires=requirements_setup,
    use_incremental=True,
)

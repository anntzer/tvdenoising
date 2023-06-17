from pybind11.setup_helpers import Pybind11Extension
from setuptools import setup


setup(
    ext_modules=[
        Pybind11Extension(
            "tvdenoising._tv_1d", ["ext/_tv_1d.cpp"], cxx_std=11),
    ],
)

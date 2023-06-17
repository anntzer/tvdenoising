#include "prox_R.cpp"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

PYBIND11_MODULE(_tv_1d, m)
{
  using namespace pybind11::literals;
  m
    .def("tv_1d", [](py::array_t<double> array, double lambda) {
      auto n = array.shape(0);
      auto out = py::array_t<double>{n};
      dp(n, array.mutable_data(), lambda, out.mutable_data());
      return out;
    }, "array"_a, "l"_a, R"__doc__(
Direct, linear time 1D total variation denoising.

Parameters
----------
array : 1d numpy float array
l : float
)__doc__")
  ;
}

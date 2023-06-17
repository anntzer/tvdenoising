"""setuptools helpers."""

import tokenize

import setuptools


__all__ = ["setup"]


def register_pth_hook(source_path, pth_name):
    """
    ::
        setup.register_pth_hook("hook_source.py", "hook_name.pth")  # Add hook.
    """
    with tokenize.open(source_path) as file:
        source = file.read()
    _pth_hook_mixin._pth_hooks.append((pth_name, source))


class _pth_hook_mixin:
    _pth_hooks = []

    def run(self):
        super().run()
        for pth_name, source in self._pth_hooks:
            with open(f"{self.install_dir}/{pth_name}", "w") as file:
                file.write(f"import os; exec({source!r})")

    def get_outputs(self):
        return (super().get_outputs()
                + [f"{self.install_dir}/{pth_name}"
                   for pth_name, _ in self._pth_hooks])


def _prepare_pth_hook(kwargs):
    cmdclass = kwargs.setdefault("cmdclass", {})
    get = setuptools.Distribution({"cmdclass": cmdclass}).get_command_class
    cmdclass["develop"] = type(
        "develop_with_pth_hook", (_pth_hook_mixin, get("develop")), {})
    cmdclass["install_lib"] = type(
        "install_lib_with_pth_hook", (_pth_hook_mixin, get("install_lib")), {})


def setup(**kwargs):
    _prepare_pth_hook(kwargs)
    setuptools.setup(**kwargs)


setup.register_pth_hook = register_pth_hook

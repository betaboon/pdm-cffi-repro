cffi_modules = ["src/myuuid_cffi/builder/build_myuuid.py:ffibuilder"]


def pdm_build_update_setup_kwargs(context, setup_kwargs):
    setup_kwargs.update(cffi_modules=cffi_modules)

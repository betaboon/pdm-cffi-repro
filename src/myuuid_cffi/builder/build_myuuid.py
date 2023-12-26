from cffi import FFI

CDEF = """
typedef unsigned char uuid_t[16];

void uuid_generate(uuid_t out);
"""

ffibuilder = FFI()
ffibuilder.cdef(CDEF)
ffibuilder.set_source(
    "_myuuid_cffi",
    "#include <uuid/uuid.h>",
    libraries=["uuid"],
)

if __name__ == "__main__":  # not when running with setuptools
    ffibuilder.compile(verbose=True)

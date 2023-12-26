import uuid

from _myuuid_cffi import ffi as _ffi
from _myuuid_cffi import lib as _lib


def generate_uuid() -> uuid.UUID:
    buf = _ffi.new("uuid_t")
    _lib.uuid_generate(buf)
    return uuid.UUID(bytes=bytes(buf))

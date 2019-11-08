from enum import IntEnum


class UserRoles(IntEnum):
    MAHASISWA = 1
    DOSEN = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
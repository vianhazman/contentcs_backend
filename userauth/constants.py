from enum import IntEnum


class UserRoles(IntEnum):
    MAHASISWA = 1
    DOSEN = 2
    ADMIN = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

def getAdminUser(id):
    response = {
        "name": "ADMIN",
        "user": id,
        "role": UserRoles.ADMIN
    }
    return response
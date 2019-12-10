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
        "role": UserRoles.ADMIN,
        "role_name":UserRoles.ADMIN.name
    }
    return response

SERVICE_URL = "https://content-ossd.cs.ui.ac.id/"
# SERVICE_URL = "0.0.0.0:8000/"
LOGIN_PATH = "auth/login/"
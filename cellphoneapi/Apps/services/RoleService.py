from ..shemas.RoleSchema import Role
from ..constants.error_code import ErrorCode, MSG_TEMPLATE
from typing import Tuple, List, Union


def get_all_role() -> Tuple[bool, Union[str, List[Role]]]:
    try:
        roles = Role.objects.all()
        return True, roles
    except Exception as e:
        return False, MSG_TEMPLATE[ErrorCode.QUERY_DATA_ERROR]


def get_role_by_id(id) -> Tuple[bool, Union[str, Role]]:
    role = Role.objects.filter(id=id).first()
    if not role:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, role


def get_role_by_name(name) -> Tuple[bool, Union[str, Role]]:
    role = Role.objects.filter(role_name=name).first()
    if not role:
        return False, MSG_TEMPLATE[ErrorCode.NOT_FOUND]
    return True, role



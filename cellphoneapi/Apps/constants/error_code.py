from enum import Enum, auto


class ErrorCode(Enum):
    DATE_NOT_GT = auto()
    DATE_NOT_GE = auto()
    DATE_NOT_LT = auto()
    DATE_NOT_LE = auto()
    UNHANDLE_EXCEPTION = auto()
    DATABASE_INSERT_FAILED = auto()
    QUERY_DATA_ERROR = auto()
    CREATE_ERROR = auto()
    UPDATE_ERROR = auto()
    DELETE_ERROR = auto()
    NOT_FOUND = auto()
    ID_NOT_FOUND = auto()
    MULTIPLE_RESULT_FOUND_WITH_FILTER = auto()

    NOT_IMPLEMENTED_ERROR = auto()

    USERNAME_PASSWORD_INVALID = auto()
    TOKEN_EXPIRED = auto()
    INVALID_SIGNATURE_ERROR = auto()
    ERROR_INVALID_TOKEN = auto()
    UNAUTHORIZED = auto()


MSG_TEMPLATE = {
    ErrorCode.NOT_IMPLEMENTED_ERROR: "not implemented error",
    ErrorCode.UNHANDLE_EXCEPTION: "Something went wrong",
    # datetime error
    ErrorCode.DATE_NOT_GT: "ensure this value is greater then {limit_value}",
    ErrorCode.DATE_NOT_GE: "ensure this value is greater or equal to {limit_value}",
    ErrorCode.DATE_NOT_LT: "ensure this value is less than {limit_value}",
    ErrorCode.DATE_NOT_LE: "ensure this value is less than or equal to {limit_value}",
    # database
    ErrorCode.DATABASE_INSERT_FAILED: "database insert failed",
    ErrorCode.QUERY_DATA_ERROR: "query data error",
    ErrorCode.CREATE_ERROR: "create error",
    ErrorCode.UPDATE_ERROR: "update error",
    ErrorCode.DELETE_ERROR: "delete error",
    ErrorCode.NOT_FOUND: "not found",
    ErrorCode.ID_NOT_FOUND: "id {id} not found",
    ErrorCode.MULTIPLE_RESULT_FOUND_WITH_FILTER: "'{filter}' multiple result found. Expected one",
    # auth
    ErrorCode.USERNAME_PASSWORD_INVALID: "Username or password invalid",
    ErrorCode.TOKEN_EXPIRED: "token_expired",
    ErrorCode.ERROR_INVALID_TOKEN: "error_invalid_token",
    ErrorCode.UNAUTHORIZED: "un authorize",
    ErrorCode.INVALID_SIGNATURE_ERROR: "Invalid signature",
}

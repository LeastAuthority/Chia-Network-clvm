IF_COST = 31
CONS_COST = 18
FIRST_COST = 8
REST_COST = 20
LISTP_COST = 5

ARITH_BASE_COST = 4
ARITH_COST_PER_LIMB_DIVIDER = 64
ARITH_COST_PER_ARG = 8

LOG_BASE_COST = 6
LOG_COST_PER_LIMB_DIVIDER = 64
LOG_COST_PER_ARG = 8

CMP_BASE_COST = 16
CMP_COST_PER_LIMB_DIVIDER = 64

GR_BASE_COST = 19
GR_COST_PER_LIMB_DIVIDER = 64

DIVMOD_BASE_COST = 29
DIVMOD_COST_PER_LIMB_DIVIDER = 64

DIV_BASE_COST = 29
DIV_COST_PER_LIMB_DIVIDER = 64

SHA256_BASE_COST = 3
SHA256_COST_PER_ARG = 8
SHA256_COST_PER_BYTE_DIVIDER = 64

POINT_ADD_BASE_COST = 213
POINT_ADD_COST_PER_ARG = 358

PUBKEY_BASE_COST = 394
PUBKEY_COST_PER_BYTE_DIVIDER = 4

MUL_BASE_COST = 2
MUL_COST_PER_OP = 18
MUL_LINEAR_COST_PER_BYTE_DIVIDER = 64
MUL_SQUARE_COST_PER_BYTE_DIVIDER = 44500

STRLEN_BASE_COST = 18
STRLEN_COST_PER_BYTE_DIVIDER = 4096

PATH_LOOKUP_COST_PER_LEG = 1
PATH_LOOKUP_COST_PER_ZERO_BYTE = 1

CONCAT_BASE_COST = 4
CONCAT_COST_PER_ARG = 8
CONCAT_COST_PER_BYTE_DIVIDER = 830

BOOL_BASE_COST = 1
BOOL_COST_PER_ARG = 8

SHIFT_BASE_COST = 21
SHIFT_COST_PER_BYTE_DIVIDER = 256

LOGNOT_BASE_COST = 12
LOGNOT_COST_PER_BYTE_DIVIDER = 512

APPLY_COST = 1
QUOTE_COST = 1

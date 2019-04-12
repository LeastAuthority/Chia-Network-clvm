from opacity import core_operators

from opacity.core import make_reduce_f

CORE_KEYWORDS = ". quote reduce cons first rest type var env_raw is_null get_raw raise equal".split()

CORE_KEYWORDS = (
    ". choose1 aggsig point_add assert_output pubkey_for_exp and type equal "
    "sha256 reduce + * - / wrap unwrap list quote quasiquote unquote get env "
    "case is_atom list1 "
    "cons first rest list type is_null var apply eval "
    "macro_expand reduce_var reduce_bytes reduce_list if not bool or map "
    "get_raw env_raw has_unquote get_default "
    "first_true raise reduce_raw rewrite rewrite_op concat ").split()


KEYWORD_FROM_INT = CORE_KEYWORDS
KEYWORD_TO_INT = {v: k for k, v in enumerate(KEYWORD_FROM_INT)}


OPERATOR_LOOKUP = {KEYWORD_TO_INT[op]: getattr(
    core_operators, "op_%s" % op, None) for op in KEYWORD_TO_INT.keys()}
transform = make_reduce_f(OPERATOR_LOOKUP, KEYWORD_TO_INT)
transform.operator_lookup = OPERATOR_LOOKUP

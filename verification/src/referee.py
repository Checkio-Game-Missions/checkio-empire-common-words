from checkio_referee import RefereeBase, representations

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(*[str(x) for x in data])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "common_words"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.unwrap_arg_representation,
        "python_3": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }

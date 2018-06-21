ATTESTER_COUNT = 32
EPOCH_LENGTH = 5
SHARD_COUNT = 20
DEFAULT_BALANCE = 20000
DEFAULT_SWITCH_DYNASTY = 9999999999999999999
MAX_VALIDATORS = 2**24


DEFAULT_CONFIG = {
    'attester_count': ATTESTER_COUNT,
    'epoch_length': EPOCH_LENGTH,
    'shard_count': SHARD_COUNT,
    'default_balance': DEFAULT_BALANCE,
    'max_validators': MAX_VALIDATORS
}


def generate_config(attester_count=ATTESTER_COUNT,
                    epoch_length=EPOCH_LENGTH,
                    shard_count=SHARD_COUNT,
                    default_balance=DEFAULT_BALANCE,
                    max_validators=MAX_VALIDATORS):
    return {
        'attester_count': attester_count,
        'epoch_length': epoch_length,
        'shard_count': shard_count,
        'default_balance': default_balance,
        'max_validators': max_validators
    }

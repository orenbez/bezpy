from hashlib import sha256

NONCE_LIMIT = 10000000000
ZEROS = 5  # Difficulty Level

# Nonce = "number only used once,"

def mine():
    for nonce in range(NONCE_LIMIT):
        base_text = base_me(nonce)
        hash_try = hash_me(base_text)
        if hash_try.startswith('0' * ZEROS):
            print(f'Found {hash_try} with nonce={nonce}')
            return hash_try
    return -1

def base_me(nonce):
    return str(block_number) + transaction + previous_hash + str(nonce)

def hash_me(text):
    return sha256(text.encode()).hexdigest()

def try_nonce(nonce):
    return hash_me(base_me(nonce))



if __name__ == '__main__':
    # https://www.blockchain.com/btc/block/487978
    # 12.5 BTC Reward for mining plus transaction fees =  1.65 BTC
    block_number = 487978  # This is the height
    transaction = '2c54556338706f1763dd9bb304a054082c8acca26f4b61fcbf6633bad8da718e'     # This is the current hash of 1MB block of ledger data
    previous_hash = '00000000000000000034e6790e3ea04db01dc8233ce1cf07cb75dd962e3b92cb'
    print(try_nonce(3087623901))  # Not getting a hash starting with zeros for some reason
    # mine()


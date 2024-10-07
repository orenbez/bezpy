# Very useful resource of algorithms
# https://pypi.org/project/algorithms
# https://the-algorithms.com/
# https://github.com/keon/algorithms
# requires `pip install algorithms`
# also see bezpy_49_sort_algorithms.py

from algorithms.sort import merge_sort
from algorithms.maths import prime_check

if __name__ == "__main__":
	[x for x in dir(algorithms.maths) if not x.startswith('_')]
	# ['alice_private_key', 'alice_public_key', 'alice_shared_key', 'base_conversion', 'base_to_int', 'bob_private_key',
	#  'bob_public_key', 'bob_shared_key', 'combination', 'combination_memo', 'cosine_similarity', 'decimal_to_binary_ip',
	#  'decimal_to_binary_util', 'decrypt', 'diffie_hellman_key_exchange', 'encrypt', 'euler_totient', 'extended_gcd',
	#  'factorial', 'factorial_recur', 'find_next_square', 'find_next_square2', 'find_order', 'find_order_simple',
	#  'find_primitive_root', 'find_primitive_root_simple', 'gcd', 'gcd_bit', 'gen_strobogrammatic', 'generate_key',
	#  'generate_strobogrammtic', 'get_primes', 'helper', 'helper2', 'int_to_base', 'is_prime', 'is_strobogrammatic',
	#  'is_strobogrammatic2', 'lcm', 'math', 'modular_exponential', 'next_perfect_square', 'power', 'power_recur',
	#  'prime_check', 'primes_sieve_of_eratosthenes', 'pythagoras', 'rabin_miller', 'randint', 'random', 'rsa', 'string',
	#  'strobogrammatic_in_range', 'trailing_zero']

	[x for x in dir(algorithms.sort) if not x.startswith('_')]
	# ['BLACK', 'GRAY', 'bitonic_sort', 'bogo_sort', 'bubble_sort', 'bucket_sort', 'cocktail_shaker_sort', 'comb_sort',
	#  'counting_sort', 'cycle_sort', 'gnome_sort', 'heap_sort', 'insertion_sort', 'max_heap_sort', 'max_heapify',
	#  'merge', 'merge_sort', 'min_heap_sort', 'min_heapify', 'next_sort', 'pancake_sort', 'partition', 'pigeonhole_sort',
	#  'quick_sort', 'quick_sort_recur', 'radix_sort', 'random', 'selection_sort', 'shell_sort', 'stooge_sort',
	#  'stoogesort', 'top_sort', 'top_sort_recursive']

	merge_sort([1, 8, 3, 5, 6]) # [1, 3, 5, 6, 8]
	prime_check(7)  # True

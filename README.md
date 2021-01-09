# Efficient-Dedicated-Algorithms-for-CRT-and-GCRT-on-Devices-with-Limited-Computing-Power
code for my paper "Efficient Dedicated Algorithms for CRT and GCRT on Devices with Limited Computing Power"

Note that our default input set size is up to 10,000, if you want to test a larger data set, please modify the parameters “numberOfElements”。
If you want to change the range of input elements, you can change the value of the parameter "rangeOfElement".


If you want to test Bernstein's algorithm with 100 elements as input, test commamd is:
sage: %time Alg_18_1(s[:100])

If you want to test Bernstein's algorithm with 10000 elements as input, test commamd is:
sage: %time Alg_18_1(s[:10000])

If you want to test our Algorithm 1 with 100 elements as input, test commamd is:
sage: %time generate_coprime_numbers(s[:100])

If you want to test our Algorithm 2 with 100 elements as input, test commamd is:
sage: %time composite_to_prime(s[:100])

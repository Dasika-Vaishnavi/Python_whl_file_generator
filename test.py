import package_test
data = "hello world"
shift = 3

encrypted_data_aes = package_test.aes_encrypt(data)
encrypted_data_caesar = package_test.caesar_encrypt(data, shift)

print(encrypted_data_aes)
print(encrypted_data_caesar)


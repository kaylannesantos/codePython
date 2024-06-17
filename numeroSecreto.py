secret_number = 777

number = int(input('Digite um número: '))

while number != secret_number:
    print("\nHa ha! You're stuck in my loop!")
    number = int(input('Digite um número: '))

print(
f"""
+==================================================+
|Secret Number: {number}                                |
|Well done, muggle! You are free now.              |
+==================================================+
""")

from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    img.save(output_path)
    print(f"Encrypted -> {output_path}")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    img.save(output_path)
    print(f"Decrypted -> {output_path}")

mode = input("E for Encrypt / D for Decrypt: ").lower()
name = input("Image name: ")
key = int(input("Key (e.g., 100): "))

if mode == 'e':
    encrypt_image(name, "encrypted_" + name, key)
else:
    decrypt_image(name, "decrypted_" + name, key)
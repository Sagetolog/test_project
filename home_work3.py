class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        new_text = ""
        for letter in original_text.lower():
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                new_index = (index + shift) % len(self.alphabet)
                new_text += self.alphabet[new_index]
            else:
                new_text += letter
        return new_text

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        new_text = ""
        for letter in cipher_text.lower():
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                new_index = (index - shift) % len(self.alphabet)
                new_text += self.alphabet[new_index]
            else:
                new_text += letter
        return new_text


cipher_master = CipherMaster()
print(
    cipher_master.cipher(
        original_text="Однажды ревьюер принял проект"
        "с первого раза, с тех пор я его боюсь",
        shift=2,
    )
)
print(
    cipher_master.decipher(
        cipher_text="Олебэи яфвнэ мроплж сэжи "
        "— э пэй рдв злййвкпш лп нвящывнэ",
        shift=-3,
    )
)

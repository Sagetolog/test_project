class CipherMaster:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def process_text(self, text, shift, is_encrypt):
        new_text = ''
        for letter in text.lower():
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                if is_encrypt:
                    new_index = (index + shift) % len(self.alphabet)
                else:
                    new_index = (index - shift) % len(self.alphabet)
                new_text += self.alphabet[new_index]
            else:
                new_text += letter
        return new_text


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))

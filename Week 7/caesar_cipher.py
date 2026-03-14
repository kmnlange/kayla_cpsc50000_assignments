'''
Kayla Lange

March 03, 2026

Description:
The CaesarCipher class implements the logic for encrypting and
decrypting messages using the Caesar Cipher algorithm.
'''

class CaesarCipher:
    def __init__(self, key: int): 
        self._key = key

    def _shift(self, text: str, key: int) -> str:
        result = ''

        for char in text:

            if char.isalpha(): 
                
                if char.isupper(): new_ascii = (ord(char) - ord('A') + key) % 26 + ord('A')
                else: new_ascii = (ord(char) - ord('a') + key) % 26 + ord('a')

                result += chr(new_ascii)

            else: result += char

        return result

    def _encrypt (self, message: str) -> str: #Encrypts a single message using the Caesar cipher logic.
        return self._shift(message, self._key)

    def _decrypt (self, message: str) -> str:
        return self._shift(message, -self._key)



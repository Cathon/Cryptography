"""
This is RC4 cryptography algorithm which is byte-oriented.

@edition: python2.7
@author: Cathon
@date: 2016.09.16

http://www.tuicool.com/articles/AjAjm2
"""

class rc4:

    __text = None       # string: plain or cipher text
    __key = None        # string: the key whose length should be more than 128 bits

    __S = None          # int list: state vector (8*256 bits)
    __K = None          # int list: temperorary vector storing the key (8*256 bits)

    __length = None     # int: the length of text and keystream
    __keystream = None  # string: used to xor with text

    def __init__(self, text, key):
        self.__text = text
        self.__key = key
        self.__length = len(text)
        self._KSA()
        self.__keystream = self._PRGA(self.__length)

    def _KSA(self):
        """
        Key Scheduling Algorithm
        Generating a initialized state vector `__S`
        """
        # initializing state and key bytes
        self.__S = [i for i in range(256)]
        self.__K = [ord(self.__key[i % len(self.__key)]) for i in range(256)]
        # Permuting state bytes based on values of key bytes
        j = 0
        for i in range(256):
            j = (j + self.__S[i] + self.__K[i]) % 256
            self._swap_S(i, j)

    def _PRGA(self, length):
        """
        Pseudo Random Generating Algorithm
        Generating the key stream whose length is `length` bytes
        """
        keystream = ""
        i, j = 0, 0
        for z in range(length):
            i = (i + 1) % 256
            j = (j + self.__S[i]) % 256
            self._swap_S(i, j)
            keystream += chr((self.__S[i] + self.__S[j]) % 256)
        return keystream

    def _process(self):
        """
        for each byte of plain(cipher)text and keystream, use xor operation
        """
        answer = ""
        for i in range(self.__length):
            answer += chr(ord(self.__text[i]) ^ ord(self.__keystream[i]))
        return answer

    def encrypt(self):
        return self._process()

    def decrypt(self):
        return self._process()

    def _swap_S(self, i, j):
        """
        swap(self.__S[i], self.__S[j])
        """
        tmp = self.__S[i]
        self.__S[i] = self.__S[j]
        self.__S[j] = tmp


if __name__ == '__main__':
    plaintext = 'hello world!'
    key = 'thisiskey128bits'
    print 'plain text is', plaintext
    encryption = rc4(plaintext, key).encrypt()
    print 'encrypted:', encryption
    decryption = rc4(encryption, key).decrypt()
    print 'decrypted:', decryption









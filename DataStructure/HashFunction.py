class HashFunction:
    """
    @param key: A string you should hash
    @param h_a_s_h__s_i_z_e: An integer
    @return: An integer
    """
    def hash_code(self, key: str, h_a_s_h__s_i_z_e: int) -> int:
        ans = 0
        for char in key:
            ans = (ans * 33 + ord(char)) % h_a_s_h__s_i_z_e
        return ans
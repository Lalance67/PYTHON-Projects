class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = list(bin(n)[2:])
        
        return int(("".join(map(str, ['1' if binary[i] == '0' else '0' 
                                      for i in range(len(binary))]))), 2)
    


    # res = ['1' if binary[i] == '0' else '0' for i in range(len(binary))]
        # for i in range(len(binary)):
        #     if binary[i] == '1':
        #         binary[i] = '0'
        #     else: 
        #         binary[i] = '1'
        
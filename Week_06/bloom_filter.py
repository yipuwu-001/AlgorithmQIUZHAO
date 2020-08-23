from bitarray import bitarray
import mmh3

class BloomFilter(object):

    def __init__(self, size, hash_num):
        self.size = size
        self.bit_array = bitarray(size)
        self.bit_array.setall(0) 

        self.hash_num = hash_num
    
    def add(self, num):
        for seed in range(self.hash_num):
            rst = mmh3.hash(num, seed) % self.size
            self.bit_array[rst] = 1
    
    def lookup(self, num):
        for seed in range(self.hash_num):
            rst = mmh3.hash(num, seed) % self.size
            if self.bit_array[rst] == 0:
                return False
        
        return True

if __name__ == "__main__":
    bf = BloomFilter(500000, 7) 
    bf.add("dantezhao") 
    print (bf.lookup("dantezhao")) 
    print (bf.lookup("yyj")) 
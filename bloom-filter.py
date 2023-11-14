class ArrayOfZeros:

    def __init__(self, size):
        self.size = size
        self.data = []
        self.appendZero()

    def appendZero(self):
        for _ in range(self.size):
            self.data.append(0)

class BloomFilter:
    def __init__(self, array, hashFunctions):
        self.array = array
        self.hashFunctions = hashFunctions

    def add(self, element):
        for hashFunction in self.hashFunctions:
            index = hashFunction(element) % self.array.size
            self.array.data[index] = 1
            print('index add:',index)

    def search(self, element):
        for hashFunction in self.hashFunctions:
            index = hashFunction(element) % self.array.size
            print('index search:',index)
            if self.array.data[index] != 1:
                print('não pertence')
                return False
        print('pertence')
        return True
    

def hashFunction1(element):
    hash = 0

    for index in range(10):
        hash = hash * 7 + ord(element[index])
    # print(hash)
    return hash


bloomfilter = BloomFilter(ArrayOfZeros(100), [hashFunction1])

emailSpam = 'emailspam.com.br'
email = 'tesfhsodif.com.br'

bloomfilter.add(emailSpam)
bloomfilter.search(emailSpam)
bloomfilter.search(email)

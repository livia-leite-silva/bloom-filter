import math 

def hashFunction1(element):
    hash = 0
    for index in range(10):
        hash = hash * 7 + ord(element[index])
    return hash

def hashFunction2(element):
    hash = 0
    for index in range(10):
        hash = hash * 7 + ord(element[index])
    return hash

class BloomFilter:

    def __init__(self, arraySize, hashFunctions):
        self.qtdSpam = 0
        self.hashFunctions = hashFunctions
        self.size = arraySize
        self.appendZero()

    def appendZero(self):
        self.data = []
        for _ in range(self.size):
            self.data.append(0)

    def add(self, element):
        for hashFunction in self.hashFunctions:
            index = hashFunction(element) % self.size
            self.data[index] = 1
        self.qtdSpam += 1 

    def search(self, element):
        for hashFunction in self.hashFunctions:
            index = hashFunction(element) % self.size
            if self.data[index] != 1:
                return False
        return True

    def falsePositive(self):
        e = (-(len(self.hashFunctions)) * self.qtdSpam) / self.size
        falsePositive = (1 - math.exp(e)) ** (len(self.hashFunctions))
        return falsePositive * 100

    def numHash(self):
        k = math.log2(self.size/self.qtdSpam)
        return k

spam = ['jackfreestuff@gmail.com','emilyx3y9z@outlook.com'
'liamq1r8p@gmail.com.br','ethanm5n2b@gmail.com.br','olivial7k4a@gmail.com.br',
'jacksonf2v9w@gmail.com.br','avah6u3j@hotmail.com','gourmetdelights:g3p6h@gmail.com'
'techsplurgew8z2q@gmail.com','chicemporiumc1r9k@gmail.com','sportsmaniat4l7o@gmail.com',
'organicblissb2v9n@gmail.com','jewelrystashf6w3u@gmail.com','gizmogroveh9j3x@gmail.com',
'cosmeticcharms7t2p@gmail.com','homeharmonyn5c8e@gmail.com','bookbazaarb3m9p@gmail.com',
'foodfusionk7q2r@gmail.com','craftycoastf1p8w@gmail.com','healthhavenh4m2n@gmail.com',
'petparadiseb9z3a@gmail.com','musicalmusem8p2o@gmail.com','gamegalaxyg2r9x@gmail.com',
'vintagefindsv5u7r@gmail.com','shoestringmarts8t4o@gmail.com','wellnesswavew3e9l@gmail.com',
'cosmicemporiumc6p1a@gmail.com']

checkList = ['jackfreestuff@gmail.com','emilyx3y9z@outlook.com'
'liamq1r8p@gmail.com.br','ethanm5n2b@gmail.com.br', 'homeharmonyn5c8e@gmail.com',
'bookbazaarb3m9p@gmail.com','foodfusionk7q2r@gmail.com', 'cosmicemporiumc6p1a@gmail.com',
'livialeite23583@gmail.com', 'Joselima@gmail.com', 'lunaj335f@gmail.com', 'alvarodasilvad@gmail.com']

bloomfilter = BloomFilter(100, [hashFunction1, hashFunction2])

for email in spam:
    bloomfilter.add(email)

for email in checkList:
    bloomfilter.search(email)

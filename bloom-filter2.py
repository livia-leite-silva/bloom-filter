import math 

class BloomFilter:
    def __init__(self, arraySize, qtyData, hashFunction):
        self.size = arraySize
        self.qtyData = qtyData
        self.hashFunction = hashFunction
        self.appendZero()

    def appendZero(self):
        self.array = []
        for _ in range(self.size):
            self.array.append(0)

    def add(self, email):
        numHashFunction = self.numHashFunction()
        for _ in range(numHashFunction):
            index = self.hashFunction(email) % self.size
            self.array[index] = 1

    def search(self, email):
        numHashFunction = self.numHashFunction()
        for _ in range(numHashFunction):
            index = self.hashFunction(email) % self.size
            if self.array[index] != 1:
                print(f'{email} não é spam')
                return False
        print(f'{email} é \033[91mspam\033[0m')
        return True

    def falsePositive(self):
        numHashFunction = self.numHashFunction()
        e = (-(numHashFunction) * self.qtyData) / self.size
        falsePositive = (1 - math.exp(e)) ** (numHashFunction)
        percent = format(falsePositive * 100, '.2f')
        return percent

    def numHashFunction(self):
        k = math.log2(self.size/self.qtyData)
        k = 1 if k < 1 else k
        return round(k)


def hashFunction(email):
    hash = 0
    for i in range(10):
        hash = hash * 7 + ord(email[i])
    return hash


spam = ['jackfreestuff@gmail.com','emilyx3y9z@outlook.com',
'liamq1r8p@gmail.com.br','ethanm5n2b@gmail.com.br','olivial7k4a@gmail.com.br',
'jacksonf2v9w@gmail.com.br','avah6u3j@hotmail.com','gourmetdelights:g3p6h@gmail.com'
'techsplurgew8z2q@gmail.com','chicemporiumc1r9k@gmail.com','sportsmaniat4l7o@gmail.com',
'organicblissb2v9n@gmail.com','jewelrystashf6w3u@gmail.com','gizmogroveh9j3x@gmail.com',
'cosmeticcharms7t2p@gmail.com','homeharmonyn5c8e@gmail.com','bookbazaarb3m9p@gmail.com',
'foodfusionk7q2r@gmail.com','craftycoastf1p8w@gmail.com','healthhavenh4m2n@gmail.com',
'petparadiseb9z3a@gmail.com','musicalmusem8p2o@gmail.com','gamegalaxyg2r9x@gmail.com',
'vintagefindsv5u7r@gmail.com','shoestringmarts8t4o@gmail.com','cosmicemporiumc6p1a@gmail.com']

checkList = ['john.doe@example.com','maria.silva@example.com','ontact@shopxyz.com','info@companyabc.biz','let23583@gmail.com', 'joselima@gmail.com', 'lunaj335f@gmail.com', 'alvarodasilvad@gmail.com',
'jackfreestuff@gmail.com','emilyx3y9z@outlook.com','liamq1r8p@gmail.com.br',
'ethanm5n2b@gmail.com.br', 'homeharmonyn5c8e@gmail.com','bookbazaarb3m9p@gmail.com',
'foodfusionk7q2r@gmail.com', 'cosmicemporiumc6p1a@gmail.com']


bloomfilter = BloomFilter(50, len(spam), hashFunction)

print(f'\nNúmero de funções de hash: {bloomfilter.numHashFunction()}')
print(f'Probabilidade de falso positivo: {bloomfilter.falsePositive()}%\n')

for email in spam:
    bloomfilter.add(email)
for email in checkList:
    bloomfilter.search(email)
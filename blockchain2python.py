import datetime
import hashlib
import random
class BlockChain:
    BlockList=[]
    index=0
    def __init__(self,data): #블록 생성
        self.timestamp=self.get_timestamp() #타임스탬프 함수
        self.nonce=self.ProofOfWork() # 마지막에 구현
        if BlockChain.index == 0:
            self.previous_hash=None #이전 해쉬 가르켜야됨
        else:
            self.previous_hash=BlockChain.BlockList[-1]['hash']
        self.data=data #거래 데이터
        self.hash=self.get_hash() #현재 해쉬 추출하는 함수, 논스 -> 해쉬를 가지게 됨
        self.creat_chain()
        BlockChain.index+=1
    def get_timestamp(self):
        return datetime.datetime.now()
    def get_hash(self): #해쉬 추출 함수
        block_contents = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        block_hash = hashlib.sha256(block_contents.encode())
        return block_hash.hexdigest()
    def creat_chain(self): # 블록들 체인으로 연결
        block_dict = { 
            'timestamp': self.timestamp,
            'hash': self.hash,
            'previous_hash': self.previous_hash,
            'data': self.data,
            'nonce': self.nonce
        }
        BlockChain.BlockList.append(block_dict)
    def ProofOfWork(self): #논스값 찾기위해 -> Proof of Work 
        self.trial=0
        while True:
            self.trial +=1
            i=random.random()
            self.rand_hash=hashlib.sha256(str(i).encode()).hexdigest()
            if self.rand_hash.startswith('0000'):
                break
        return self.trial
    def print_BlockChain(self):
        print(BlockChain.BlockList)
init_block=BlockChain(20)
block=BlockChain(30) 
init_block.print_BlockChain()
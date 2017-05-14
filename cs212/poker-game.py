

def poker(hands):
    
    list=[hand_rank(hand) for hand in hands]                           # 8 需要去解决确实存在平局的情况
    
    b=max(list)
    
    if list.count(b)==0:
        return b
    
    else:
        return "tie"
    
    return max(hands,key=hand_rank)    # 1  由找best hand,想到用max函数
                                       # 2 由max函数的使用，知道要利用key,由此想到写hand_rank函数
    
  
def hand_rank(hand):                  # 3 有max比较对象为数字，想到hand_rank返回结果为数字
    rank=card_rank(hand)
    if straight(rank) and flus(hand):
        return （8，max(rank))        # 4 在确定8,7,6等层级数字后，进一步细化，用元组表示
    elif kind(4,ranks):
        return (7 , kind(4,rank),kind(1,rank))
    elif kind(3,rank) and kind(2,rank)：
        return (6 , kind(3,rank),kind(2,rank))    ####  写代码时 “DRY”  要改写，如图
    elif flus(hand):
        return (5 , rank)        
    elif straight(rank):
        return (4 , max(rank)  
    elif kind(3,rank):
        return (3,kind(3,rank),rank)  
    elif two_pair(rank):
        return (2,two_pair(rank),rank)    

 
        
        
        
        
def card_rank(cards):
    #rank=[r for r s in cards] 
    rank=["__23456789TJQKA".index(r)for r s in cards ]     # 5  构建列表，一步到位，利了用 index
    rank.sort(reverse=True)
    if rank==[13,5,4,3,2]    # 7 写完所有方程后，发现有个例子 1 2 3 4 5需要去处理，处理特例的方式是直接单独拿出来处理
        del rank[0]                      #  直接写成 rank==[5,4,3,2,1]
        rank[4]=1                
    return rank
        
        
def straight(rank):
    return (max(rank)-min(rank)==4)  and len(set(rank))==5    #6  把return结果设为逻辑判断句，一个return就可以

# def straight(ranks):                   利用性质去写，简单
    if ranks[0]-1==ranks[1]:
        if ranks[1]-1==ranks[2]:
            if ranks[2]-1==ranks[3]:
                if ranks[3]-1==ranks[4]:
                    return True
                    
    else:
        return False

def flus(hand):
    suit=[s for r,s in hand]
    return len(set(suit))==1
    
#  def fly(hands):
    list=[]
    for s in hands:
        list.append(s)
    if list[0]==list[1]==list[2]==list[3]==list[4]:
        return True
    else:
        return False
        
        
def kind(n,rank):
    for r in rank:
        if rank.count(r)==n:
            return r
    return None
 
# def kind(n,ranks):
    
    #if n==num=4:
        for i in set(ranks):
            ranks.remove(i)
      
        if len(set(ranks))==1:
            if n==4:
                return ranks[0]
            if n==1:
                return 
            else:
                return
        if len(set(ranks))==2:
    

    new=set(ranks)
    if len(new)==2:
        for i in set(ranks):
            ranks.remove(i)
        if len(set(ranks))==1:
            if n==4:
                return ranks[0]
            if n==1:
                new.remove(ranks[0])
                return new[0]
            else:
                return None
        else:
        
        
def two_pair(rank):
    pair(2,kind)
    lowerpair =(2,list(reverse(rank)))
    if pair and lowerpair != pair :
        return(pair,lowerpair)
    return None
    
# def two_pair(ranks):
    list=[]
    for r in ranks:
        if ranks.count(r)==2:
            list.append(r)
    
            b=set(list)
            c=sorted(b,reverse=True)
            return   tuple(c)
    return None
    





def test():
	"test cases for the functions in poker program"
	sf="6c 7c 8c 9c tc".split()
	fk="9d 9h 9s 9c 7d".split()
	fh="td tc th 7c 7d".split()
	tp="5s 5d 9h 9c 6s".split()
	fkranks=card_ranks(fk)
	tpranks=card_ranks(tp)
	assert kind(4,)
	assert straight([9,8,7,6,5])==True
	assert straight([9,8,8,6,5])==False
	assert card_ranks(sf)==[10,9,8,7,6]
	assert card_ranks(fk)==[9,9,9,9,7]
	assert card_ranks(fh)==[10,10,10,7,7]
	assert poker([sf,fk,fh])==sf
	assert poker([fk,fh])==fk
	assert poker([fh,fh])==fh
	assert poker([sf])==sf
	assert poker([sf]+99*[sh])==sf
	assert hand_rank(sf)==(8,10)
	assert hand_rank(fk)==(7,9,7)
	assert hand_rank(fh)==(6,10,7)
	return "test pass" 




print test()
    
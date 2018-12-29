


def cfdefault(bts,k):return bts==k
def dfdefault(k,v):pass
def ofdefault(self,amount):return amount
def gidefault(self,p):return int(p.ret[self.index])
class step:
    #read length
    blen=0
    dofunc=dfdefault
    parent=None
    proc=None
    def setdofunc(self,func):
        self.dofunc=func
    def __init__(self,blen,dofunc=dfdefault):
        self.blen=blen
        self.dofunc=dofunc
    def setparent(self,p):
        self.parent=p
    def setproc(self,p):
        self.proc=p
    @classmethod
    def check(self,bts):
        self.dofunc(bts,bts)
        #print(bts)
        return bts
    def __str__(self):
        return 'step blen=%i'%(self.blen)
class gotostep(step):
    index=None
    def __init__(self,index,dofunc=dfdefault):
        step.__init__(self,0,dofunc)
        self.index=index
    def setparent(self,p):
        step.setparent(self,p)
        self.blen=p.switch[self.index].blen
        #print('goto blen:',self.blen)
        
class valuestep(step):
    index=None
    steps=0
    stepd=step(0)
    #to do operation to the steps count
    opfunc=ofdefault
    gifunc=gidefault
    def setopfunc(self,of):
        self.opfunc=of
    def __init__(self,index,stepd=step(0),dofunc=dfdefault,opfunc=ofdefault,gifunc=gidefault):
        step.__init__(self,0,dofunc)
        self.stepd=stepd
        self.index=index
        self.gifunc=gifunc
        self.setopfunc(opfunc)
    def setproc(self,p):
        step.setproc(self,p)
        self.steps=self.gifunc(self,p)
        #print('steps:',self.steps,',(',p.ret[self.index],')')
    def check(self,bts):
        ret=[self.stepd]*self.opfunc(self.steps)
        #print(ret)
        return ret
class switchstep(step):
    switch={}
    checkfunc=cfdefault
    #dofunc=dfdefault
    def __init__(self,blen,dofunc=dfdefault,checkfunc=cfdefault):
        step.__init__(self,blen,dofunc)
        self.setcheckfunc(checkfunc)
    def setcheckfunc(self,func):
        self.checkfunc=func
    def addswitch(self,b,step):
        step.setparent(self)
        self.switch[b]=step
    def check(self,bts):
        for k,v in self.switch.items():
            bt=byteutils.toInt(bts)
            #print(k,',',v,',bts=',bts,'(',bt,')')
            if self.checkfunc(bt,k):
                #print('pass:',v)
                self.dofunc(k,v)
                return v
        return None
class flagstep(step):
    flags=[]
    #dofunc=dfdefault
   
    def genFromArr(self,fls,flagpos='value'):
        flag=1
        ret={}
        for f in fls:
            self.flags.append(flag)
            if flagpos=='value':
                ret[f]=flag
            else:
                ret[flag]=f
            flag=flag*2
        return ret
    def genFromDict(self,dict,flagpos='value'):
        if flagpos=='value':
            self.flags+=dict.values()
        else:
            self.flags+=dict.keys()
        
    def check(self,bts):
        retflags=[]
        f=byteutils.toInt(bts)
        for flag in flags:
            if (f&flag)!=0:
                #print('find flag:',flag,' from byte ',f)
                retflags.append(flag)
        #print(retflags)
        self.dofunc(retflags)
        return retflags
"""class bytestep(step):
    def check(self,bts):
        return bts
"""
class StepProcessor(step):
    steps=[]
    ret=[]
    def __init__(self,step=[]):
        self.steps=step
    def addstep(self,step):
        #step.proc=self
        steps.append(step)
    def check(self,bts):
        return self.process()
    def process(self,bts):
        self.index=0
        self.ret=[]
        for step in self.steps:
            self.ret.append(self.doStep(step,bts))
        return self.ret
    def doStep(self,ste,bts):
        #byte period
        bp=bts[self.index:self.index+ste.blen]
        
        #step check return
        ste.setproc(self)
        sret=ste.check(bp)
        ret=sret
        if isinstance(sret,step):
            self.index+=1
            ret=self.doStep(sret,bts)
            self.index-=1
        if isinstance(ste,valuestep):
            #print('is valuestep')
            ret=[]
            self.index+=1
            for s in sret:
                self.index-=1
                
                r=self.doStep(s,bts)
                ret.append(r)
                self.index+=1
            self.index-=1
            
        self.index+=ste.blen
        #print('index:',self.index)
        return ret


#utils
class byteutils:
    @staticmethod
    def toInt(bts):
        return int.from_bytes(bts,byteorder='big')
    @staticmethod
    def toByte(a,btnum=4):
        ind=btnum-1
        bt=[0]*btnum
        buf=0
        while ind!=-1:
            bt[ind]=(a>>buf)&0xff
            ind-=1
            buf+=8
        return bt
        
#main
#'''
if __name__=='__main__':
   
    fs=flagstep(2)
    flags=fs.genFromArr([bytes([i]).decode('utf-8') for i in range(65,123)],flagpos="key")
    print(flags)
    #fs.setdofunc(lambda f:(print('flags',flags[fl]) for fl in f))
    def df(s):
        for fl in s:
            print('flag ',flags[fl])
    fs.dofunc=df
    ss=switchstep(1)
    ss.addswitch(1,step(2))
    ss.addswitch(2,step(5))
    ss.addswitch(3,step(7))
    ss.addswitch(0xd,gotostep(1))
    ss.addswitch(5,step(1))
    ss.addswitch(6,valuestep(7,stepd=step(1),opfunc=lambda n:n-1))
    #fs.dofunc([1])
    pr=StepProcessor([fs]*2+[ss]*8)
    dec=b'\0\1'+bytes(byteutils.toByte(1|32|128|64,2))+b'\1hi\2hello\1ok\3alright\x0dhi\5'+b'4\6wow\1hi'
    print('dec origin:',dec)
    res=pr.process(dec)
    print('return :',res)
    
#'''
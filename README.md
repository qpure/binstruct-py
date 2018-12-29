# BinStruct  

## What is it?  

&emsp;&emsp;**BinStruct** is an *avdanced and extended* `python struct module`.With this module,you can easily parse a binary file `structure/syntax` and use the `structure/syntax` to `deserialise` or `read` the binary file  

## How to use?  
&emsp;&emsp;To parse the binary file structure,There are several steps:  

### Step  
class `step` is used as a dynamic action.
Creating a `step` is quite simple:  
```python
'''
create a step
step(blen,gofunc=gfdefault)
ps:gfdefault is a DEFAULT dofunc in module
blen:How many bytes
gofunc:when matched the value,do some actions
'''
mystep=step(8,gofunc=lambda k,v:print(k,',',v))
```   
PS:all classes that extends class `step` has a `check` method,which processes the bytes Input.  
Or you can use `switchstep`:  
```python
switch=switchstep(4,checkfunc=lambda bt,k:bt==k)
switch.addswitch(8,step(16))
#create a switch Step which uses bt==k to check whether the key is the right key as Input or not.
#add a switch,when checkfunc's result for processing 8 to 8's comparasion is right,invoke the step(16)
```
**`flagstep`**
This is another step for processing `flags`(AKA `bitmask`).  

|Method|Args|Description|Returns|
|:-----------|:----------------:|:----------|--------:|
|genFromArr|`flags:array`,`flagpos='value'`|generate flags from array And store it.|a dict With flags on `flagpos` side|
|genFromDict|`flags:dict`,`flagpos='value'`|generate flags on `flagpos` side of dict And store it.|None|  

**`valuestep`**  
This `step` is a little bit complicated but useful.It dynamically gets the datas got in the `StepProcessor` class(**field** `ret`),turn them into numbers by custom function(or use default) , and generate the same value amount of steps (which is also customized), and pass it to the processor to process it dynamically.  

**`gotostep`**  
this class was created With a wrong purpose but gave me a better idea.I am still developing This class.it has a different use right now.  
This class is currently used in `switchstep`.it just gets the switch in switchstep and do the same thing as the switch.  
My purpose is to let it go back to a specific step in order to do sth like **loop**,**skip** or other.  




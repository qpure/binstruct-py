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
This is another step for processing `flags`(or `bitmask`).  

|Method|Args|Description|Returns|
|:-----------|:----------------:|:----------|--------:|
|genFromArr|`flags:array`,`flagpos='value'`|generate flags from array And store it.|a dict With flags on `flagpos` side|
|genFromDict|`flags:dict`,`flagpos='value'`|generate flags on `flagpos` side of dict And store it.|None|  

**`valuestep`**  
This `step` is a little bit complicated.



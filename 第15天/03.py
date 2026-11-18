from dataclasses import dataclass

@dataclass
class Contact:
    name:str
    phone:str

c = Contact("张三","13800001111")
print(c)
print("相等吗：",c == Contact("张三","13800001111"))
print([m for m in dir(c) if m.startswith("__") and m not in dir(object)])

from dataclasses import dataclass,field

@dataclass
class Contact:
    name:str
    phone:str
    tags:list[str] = field(default_factory=list)

a = Contact("甲","1")
b = Contact("乙","2")
a.tags.append("同事")

print("a.tags=",a.tags)
print("b.tags=",b.tags)
print("是同一个结果吗：",a.tags is b.tags)



@dataclass
class Contact2:
    name:str
    phone:str

    def masked(self) ->str:
        return self.phone[:3] + "****" + self.phone[-4:]
print(Contact2("张三","13800001111").masked())
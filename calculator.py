# class calculator:
#     def add(self,a,b):
#         print(a+b)

#     def sub(self,a,b):
#         print(a-b)

#     def mul(self,a,b):
#         print(a*b)

#     def div(self,a,b):
#         print(a/b)

#     def mod(self,a,b):
#         print(a%b)

#     def exp(self,a,b):
#         print(a**b)
# a=calculator()
# a.add(10,20)
# a.sub(10,20)
# a.mul(10,20)
# a.div(10,20)
# a.mod(10,20)
# a.exp(10,20)



class Brand:
    brand_list=[]
    def add_brand(self,a):
        self.brand_list.append(a)
    def delete_brand(self): 
            self.brand_list.pop(1)

    def update_brand_by_brand_name(self, brand_name, new_brand):
        for i in range(len(self.brand_list)):
            if self.brand_list[i].get('brand') == brand_name:
                self.brand_list[i] = new_brand
                                               
    def display_brand(self):
        print(self.brand_list)
        
a = Brand()
a.add_brand({"brand" : "Ford","model" : "Mustang","year" : 1964})
a.add_brand({"brand" : "Volvo","model" : "vv","year" : 1990})
a.add_brand({"brand" : "Maruthi","model" : "ee","year" : 1995})
a.display_brand()
a.delete_brand()
a.update_brand_by_brand_name("Maruthi", {"brand": "Tesla","model" : "tt","year" : 1985})
a.display_brand()


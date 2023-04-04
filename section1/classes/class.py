class Cookie:
    def __init__(self,color) -> None:
        self.color = color
    
    def set_color(self,color):
        self.color = color
    def get_color(self):
        return self.color
    

cookie_1 = Cookie('Green')
cookie_2 = Cookie('Blue')

cookie_1 = cookie_2

print("Cookie 1 is ",cookie_1.get_color()) # Blue
print("Cookie 2 is ",cookie_2.get_color()) # Blue

cookie_1.set_color('Yellow')

print("Cookie 1 is ",cookie_1.get_color()) # Yellow
print("Cookie 2 is ",cookie_2.get_color()) # Yellow

# cookie1 and cookie2 now are Yellow because cookie class is mutable



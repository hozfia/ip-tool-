class ip_tool (object) :
    a_digit = []
    b_digit = []
    c_digit = []
    d_digit = []
    def __init__(self, ip_add):
        self.ip_add =  ip_add 
    def ip_digit (self) :
        dot_pos_index = []
        cou = 0 
        for i in self.ip_add :
            cou += 1 
            if i == "." :
                 dot_pos_index.append(cou)
        a_digit = []
        b_digit = []
        c_digit = []
        d_digit = []
        for x in range(0,dot_pos_index[0] - 1):
            a_digit.append(self.ip_add[x])
        for x in range(dot_pos_index[0],dot_pos_index[1] - 1):
            b_digit.append(self.ip_add[x])
        for x in range(dot_pos_index[1] , dot_pos_index[2] - 1):
            c_digit.append(self.ip_add[x])    
        for x in range(dot_pos_index[2] , cou):
            d_digit.append(self.ip_add[x])    
        global a_digit
        a_digit = self.convert (a_digit)
        b_digit = self.convert (b_digit) 
        c_digit = self.convert (c_digit) 
        d_digit = self.convert (d_digit)
        
    def convert (self , list) :
        res = int("".join(map(str,list)))
        return res
 

#####################################    
ip1 = ip_tool("323.23.21.3")
#print(ip1.ip_digit.a_digit)

				
				
				
    

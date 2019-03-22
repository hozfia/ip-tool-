class ip_tool (object) :
    
    def __init__(self, ip_add):
        self.ip_add =  ip_add 
    def ip_digit (self , digit_name) :
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
        a_digit = self.convert (a_digit)
        b_digit = self.convert (b_digit) 
        c_digit = self.convert (c_digit) 
        d_digit = self.convert (d_digit)
        if digit_name == 1 :
            return a_digit
        if digit_name == 2 :
            return b_digit
        if digit_name == 3 :
            return c_digit
        if digit_name == 4 :
            return d_digit
        
    def convert (self , list) :
        res = int("".join(map(str,list)))
        return res
    def display_ip (self) :
        return str(self.ip_digit(1)) +"."+ str(self.ip_digit(2)) +"."+ str(self.ip_digit(3)) + "."+str(self.ip_digit(4))
    def ip_counter (self , to_ip):
        if self.ip_digit(1) == self.coustom_ipadd_saptr(to_ip,1) :
            for ii in range(self.ip_digit(2), 255):
                if ii == 255 :
                    ii = 0 
                for iii in range(self.ip_digit(3), 255):
                    if iii == 255 :
                        iii = 0 
                    for iiii in range(self.ip_digit(4),255):
                        if iiii == 255 :
                            iiii = 0 
                        print str(self.ip_digit(1)) +"."+ str(ii) +"."+ str(iii) +"."+ str(iiii)

                        
    def coustom_ipadd_saptr(self , ipadd , digit_name) :
        dot_pos_index = []
        cou = 0 
        for i in ipadd :
            cou += 1 
            if i == "." :
                 dot_pos_index.append(cou)
        a_digit = []
        b_digit = []
        c_digit = []
        d_digit = []
        for x in range(0,dot_pos_index[0] - 1):
            a_digit.append(ipadd[x])
        for x in range(dot_pos_index[0],dot_pos_index[1] - 1):
            b_digit.append(ipadd[x])
        for x in range(dot_pos_index[1] , dot_pos_index[2] - 1):
            c_digit.append(ipadd[x])    
        for x in range(dot_pos_index[2] , cou):
            d_digit.append(ipadd[x])             
        a_digit = self.convert (a_digit)
        b_digit = self.convert (b_digit) 
        c_digit = self.convert (c_digit) 
        d_digit = self.convert (d_digit)
        if digit_name == 1 :
            return a_digit
        if digit_name == 2 :
            return b_digit
        if digit_name == 3 :
            return c_digit
        if digit_name == 4 :
            return d_digit
        

#####################################    
ip1 = ip_tool("155.23.21.3")


				
				
				
    

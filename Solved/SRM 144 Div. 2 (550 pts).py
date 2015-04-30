class BinaryCode(object):

    def decode(self, message):
        message_intlist = []
        for i in message:
            message_intlist.append(int(i))
        
        decode_a = [0]
        decode_b = [1]

        # The section below runs the loops for decode_a
        
        for i in range(len(message_intlist)):
            if i == 0:
                x = message_intlist[i] - decode_a[i]
                if x > 1:
                    decode_a = None
                    break
                else:
                    decode_a.append(x)
            else:
                x = message_intlist[i] - (decode_a[i] + decode_a[i-1])
                if x > 1:
                    decode_a = None
                    break
                else:
                    decode_a.append(x)

        decode_a_string = ""
        if decode_a != None:            
            if decode_a[len(message_intlist)] != 0:
                decode_a_string = "NONE"
            else:
                decode_a.pop(-1)
                for i in decode_a:
                    i = str(i)
                    decode_a_string += i
        else:
            decode_a_string = "NONE"

        # The section below runs the loops for decode_b
        
        for i in range(len(message_intlist)):
            if i == 0:
                x = message_intlist[i] - decode_b[i]
                if x > 1:
                    decode_b = None
                    break
                elif message_intlist[i] == 0:
                    decode_b = None
                    break
                else:
                    decode_b.append(x)
            else:
                x = message_intlist[i] - (decode_b[i] + decode_b[i-1])
                if x > 1:
                    decode_b = None
                    break
                else:
                    decode_b.append(x)
        
        decode_b_string = ""
        if decode_b != None:
            if decode_b[len(message_intlist)] != 0:
                decode_b_string = "NONE"
            else:
                decode_b.pop(-1)
                for i in decode_b:
                    i = str(i)
                    decode_b_string += i
        else:
            decode_b_string = "NONE"

        return decode_a_string, decode_b_string

print BinaryCode().decode("00")
print BinaryCode().decode("123210122")    # Returns: ("011100011",  "NONE")
print BinaryCode().decode("11")           # Returns: ("01",  "10")
print BinaryCode().decode("22111")        # Returns: ("NONE",  "11001")
print BinaryCode().decode("123210120")    # Returns: ("NONE",  "NONE")
print BinaryCode().decode("3")            # Returns: ("NONE",  "NONE")
print BinaryCode().decode("12221112222221112221111111112221111")
# Returns: ("01101001101101001101001001001101001", "10110010110110010110010010010110010")
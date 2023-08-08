# Note that each module is a python file (saved with .py extension) which can be imported into another module
# that will require its functions or global variables.


class dataset_module:
    def __init__(self, dt="Transaction.txt"):
        self.data = dt  # object to store the string of transaction data

    def getData(self):
        return self.data

    def proData(self):
        ds = self.data
        dic = {}  # empty dictionary

        # Try action
        try:
            fp = open(ds, "r")  # To open a file
            lines = fp.readlines()  # read of the file and assign to variable. Lines is a list collection of the records.

        # exception if the 'try' block actions are not possible
        except:
            return ("There is no file found or No file with the given name/path")

        #print(lines)

        for line in lines:
            # 1 indicates that one and the first occurrence (maxsplit parameter) of ':' in the
            # string will be used to do the only split to have only two elements (i.e. [21, 500000:HMS HOST-BOS AIRPT:36.55:884.0:755.0:false'])
            # This is further resolved by join this split with no common (but with a space (i.e. ''))
            strg = ''.join(line.split(':', 1))
            #print(strg)

            # print(strg)
            trans = strg[2] + strg[3] + strg[4] + strg[5] + strg[6] + strg[7] + strg[
                8]  # To obtain Transaction Id as unique key along with a ':'
            trans = trans[0:-1]  # To strip-off ':' from the string attached at the end of the transaction Id

            # The keys to the dictionary (dic) is trans while the value
            # is the remaining part of the string on a line without the transaction Id.
            # So it is the user Id(i.e. line[0] + line[1] and every other item after the transaction Id.
            # Note that remaining part is taken from the original description of transaction (line) till the end without '\n':
            # example: '500000' (key) : '21:HMS HOST-BOS AIRPT:36.55:884.0:755.0:false' (value)

            dic[int(trans)] = line[0] + line[1] + line[
                                                  9: -1]  # assigning key with the remaining part of the line string and remove the '\n' at the end of the string.

        return dic  # returns dictionary


# # Method/function being tested. This should be in your test_Module file
# print(proData("Transaction.txt")) #prints the dictionary with the text file's contents
d = dataset_module() #class instance or object created
# print(type(proData("Transaction.txt"))) #to print the datatype of the output (i.e. dictionary)
# mydict = proData("Transaction.txt")


mydict = d.proData() #class method is called on the class object
print(mydict)  # Displays the dictionary
# print("Transaction details of 500001: ", mydict[500001]) #returns to value for a given 500001

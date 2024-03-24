from math import log2
import random
import zlib
def read_file_and_compress(file,encod):
    with open(file, "r") as file:
        string = file.read()
        
        
        bytearray_string = bytearray(string, encod)
        
        return string, bytearray_string

def make_histo(byte_array): #indicates how many times eachnumber/bit-pattern (0-255) occurrs in byteArr.
    histogram = [0]*256
    
    for byte in byte_array:
        histogram[byte] +=1
        
    return histogram

def make_prob(histogram):
    total_count = sum(histogram)
    
    if total_count == 0:
        return [0] * len(histogram)
    
    probablity_dist = []
    for count in histogram:
        probablity = count / total_count
        probablity_dist.append(probablity)
    return probablity_dist

def make_entropy(probablity):
    entropy = 0
    for i in range(len(probablity)):
        if probablity[i] > 0:
            entropy += probablity[i] * log2(1/probablity[i])
    return entropy


if __name__ == "__main__":
    #1.Read and investigate the file
    file = "exempeltext.txt"
    encod = "UTF-8"
    string, bytearray_string = read_file_and_compress(file,encod)
    print(f"\n1) There are {len(string)} symbols in the string and {len(bytearray_string)} bytes in the byte-array.")
    print("Because the string has swedish characters wich can are bigger than one byte\n\n")
    
    #2.Calculate statistics and entropy
    histogram = make_histo(bytearray_string)
    print(f"2.a) Histogram : \n{histogram}\n")
    
    probablity = make_prob(histogram)
    print(f"2.b) Sum of Probablity : {sum(probablity)}\n")
    
    file_entropy = make_entropy(probablity)
    print(f"2.c) Entropy : {round(file_entropy,2)} bits/symbols\n")
    
    print(f"2.d){round(file_entropy* len(bytearray_string)/8,2)} bytes.\n\n")
    
    #3.Copy the text and shuffle the copy
    bytearray_string_copy = bytearray(string, "UTF-8")
    random.shuffle(bytearray_string_copy)
    print(f"3.b) There are {len(bytearray_string_copy)} bytes in the suffled byte-Arr (OBS: none shuffle: {len(bytearray_string)} bytes).\n\n")
    
    #4.Zip-compress
    zipped_bytearray_string = zlib.compress(bytearray_string)
    zipped_bytearray_string_copy = zlib.compress(bytearray_string_copy)
    print(f"4.c) The suffled and zipped has {len(zipped_bytearray_string_copy)} bytes and unzipped file has {len(bytearray_string_copy)} bytes")
    print(f"\t -The comporesed file is {round(len(zipped_bytearray_string_copy)/len(bytearray_string_copy),2)} smaller than uncomporessed version.\n")
    
    print(f"4.d) The unsuffled and zipped has {len(zipped_bytearray_string)} bytes and unzipped file has {len(bytearray_string)} bytes.")
    print(f"\t -The comporesed file is {round(len(zipped_bytearray_string)/len(bytearray_string),2)} smaller than uncomporessed version.\n")
    
    print(f"4.e) The unshuffled zipped has {round(len(zipped_bytearray_string)*8/len(bytearray_string),2)} bytes.")
    print(f"4.e) The shuffled zipped has {round(len(zipped_bytearray_string_copy)*8/len(bytearray_string),2)} bytes.")
    print(f"4.e) The entropy has {round(file_entropy,2)} bytes.\n\n")

    
    #5.Zip repetitive text
    t1 = """Submit your python code on Canvas and prepare answers to the questions marked with Answer!.
    Present then your code and answers to your lab assistant."""
    zippedT1=zlib.compress(bytearray(t1,'UTF-8'))   
    print(f"5.b) T1 has {len(t1)} bytes and zipped file has {len(zippedT1)} bytes.")
    print(f"\t -The comporesed file is {round(len(zippedT1)/len(t1),2)} smaller than uncomporessed version.\n")
    
    t10 = 10*t1
    zippedT10=zlib.compress(bytearray(t10,'UTF-8'))
    print(f"5.c) T10 has {len(t10)} bytes and zipped file has {len(zippedT10)} bytes.")
    print(f"\t -The comporesed file is {round(len(zippedT10)/len(t10),2)} smaller than uncomporessed version.")
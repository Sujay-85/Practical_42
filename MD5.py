import hashlib 

def md5_hash(text): 
    return hashlib.sha512(text.encode()).hexdigest() 
# Example usage 
if __name__ == "__main__": 
    input_text = "g" 
    hash_result = md5_hash(input_text) 
    print(f"MD5 hash of '{input_text}': {hash_result}") 


# Problem Statement
# You want to be safe online and use different passwords for different websites. However, you are forgetful 
# at times and want to make a program that can match which password belongs to which website without storing the
#  actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a 
# different, unique identifier. This is done using a hash function. Luckily, there are several resources that
#  can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's 
# stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it 
# works, just know that hash_password(...) returns the hash for the password!)

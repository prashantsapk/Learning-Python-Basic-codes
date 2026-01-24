marks = {"prashant":100,"ram":30,"pencolin":50}
# items
print(marks.items())
#keys
print(marks.keys())
#update
marks.update({"ram":40,"New user":80})
print(marks)

print(marks.get("prashant")) # prints none
print(marks["prashant"]) # prints error

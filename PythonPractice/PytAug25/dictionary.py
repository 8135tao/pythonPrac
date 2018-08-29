wakeup_time = {"Mon": "9 am", "Tue": "10 am", "Wed": "2 pm"}

hobbies = []

Tao = {"name": "Tianyu Tao", "age": 27, "hobbies": hobbies, "wakeup time": wakeup_time}
Tao["hobbies"] = ["games","Aikido"]
 
print(str(Tao["name"])+"is "+ str(Tao["age"]) + " old"+ "he likes")

print(f'{Tao["name"]} likes {Tao["hobbies"][0]} and mm')

print(f'{Tao["name"]} woke up {wakeup_time["Mon"]} Mon')
import os

print("AI Learning Companion")

def save_notes():
    topic = input("Enter topic: ")
    notes = input("Enter notes: ")
    filename = "notes/" + topic.replace(" ", "_").lower( ) + ".text"
    file = open(filename, "w")
    file.write(notes)
    file.close()

    print("Notes saved successfully!")

 

def read_notes():
    topic = input("Enter topic: ")
    filename = "notes/" + topic.replace(" ", "_").lower()  + ".text"
    try:
     file = open(filename, "r")
     content = file.read()
     file.close()

     print("\nYour Notes:")
     print(content)
    except FileNotFoundError:
        print("No notes found for this topic.")

def list_notes():
  print("\nAvailable Notes:")

  files = os.listdir("notes")
  if not files:
    print("No notes available")
    return
  for file in files:
    
   if file.endswith(".text"):
     topic = file.replace(".text", "").replace("_", " ").title()
     print("-", topic)
while True:
  print("\nAI Learning Companion")
  print("1. Save Notes")
  print("2. Read Notes")
  print("3. List ALL Notes")
  print("4. Exit")     

  choice = input("Choose an option: ")

  if choice == "1":
    save_notes()
  elif choice == "2":
    read_notes()
  elif choice == "3":
    list_notes()  
  elif choice =="4":
    print("Goodbye!")
    break
            
  else :
    print("Invalid option")    

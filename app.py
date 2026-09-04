import os
import json
from datetime import datetime
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("API key loaded:", api_key is not None)
 

client = genai.Client(api_key=api_key)

def ask_ai():
   question = input("Ask AI: ")
   response = client.models.generate_content(
      model="gemini-3.7-flash",
      contents=question
   )
   print("\nAI:",response.text)

print("AI Learning Companion")

def save_notes():
    topic = input("Enter topic: ")
    notes = input("Enter notes: ")
    category = input("Enter category: ")
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("data/notes.json", "r") as file:
       all_notes = json.load(file)
    new_notes = {
      "topic": topic,
      "category": category,
      "notes": notes,
      "created": date_time
    }
    all_notes.append(new_notes)
    with open("data/notes.json", "w") as file:
       json.dump(all_notes, file, indent=4)

     

    print("Notes saved successfully!")

 

def read_notes():
    topic = input("Enter topic: ")
    with open("data/notes.json", "r")as file:
        all_notes = json.load(file)
        found = False
        for note in all_notes:
          if note["topic"].lower() == topic.lower():
            print("\nYourNotes:")
            print(note["notes"])
            print("Created:", note["created"])
            found = True
            if  not found:
              print("No notes found for this topic.")
         
         


def list_notes():
  print("\nAvailable Notes:")

  with open("data/notes.json", "r")as file:
    all_notes = json.load(file)
    if len(all_notes) == 0:
      print("No notes available.")
    else:
      for note in all_notes:
        print("-", note["topic"])

         
def search_notes():
  keyword = input("Enter keyword to search: ").lower()
  with open("data/notes.json", "r") as file:
    all_notes = json.load(file)
    found = False
    for note in all_notes:
      if keyword in note["notes"].lower() or keyword in note["topic"].lower():
        print("\nTopic:", note["topic"])
        print("Notes:", note["notes"])
        print("Created:", note["created"])
        found = True
        if not found:
          print("No matching notes found.")


def search_by_category():
  category = input("Enter category: ").lower()
  found = False
  for filename in os.listdir("notes"):
    file = open("notes/" + filename, "r")
    content = file.read()
    file.close()
    if "category: " + category in content.lower():
      print("\n---", filename, "---")
      print(content)
      found = True
      if found == False:
        print("No notes found in this category.")



def delete_notes():
  topic = input("Enter topic to delete: ")
  with open("data/notes.json", "r") as file:
    all_notes = json.load(file)
    new_notes = []
    found = False
  for note in all_notes:
      if note["topic"].lower() == topic.lower():
        found = True
      else:
        new_notes.append(note)
  with open("data/notes.json", "w") as file:
          json.dump(new_notes, file, indent=4)
  if found:
            print("Note deleted successfully!")
  else:
            print("Note not found.") 

def update_note():
  topic = input("Enter topic to update: ")
  filename = "notes/" + topic.replace(" ", "_").lower() + ".text"
  if os.path.exists(filename):
    new_notes = input("Enter new notes: ")
    file = open(filename, "w")
    file.write(new_notes)
    file.close()
    print("Note Update Successfully!")
  else:
    print("Note not found.")

while True:
  print("\nAI Learning Companion")
  print("1. Save Notes")
  print("2. Read Notes")
  print("3. List ALL Notes")
  print("4. Search Notes")
  print("5. Search by Category")
  print("6. Delete Notes") 
  print("7. Update Note")  
  print("8. Exit") 
  print("9. Ask AI")

  choice = input("Choose an option: ")

  if choice == "1":
    save_notes()
  elif choice == "2":
    read_notes()
  elif choice == "3":
    list_notes()  
  elif choice =="4":
    search_notes()
  elif choice == "5":
    search_by_category()  
  elif choice == "6":
    delete_notes()
  elif choice =="7":
    update_note()
  elif choice  == "9":
     ask_ai()      
  elif choice =="8":
    print("Goodbye!")  
    break
            
  else :
    print("Invalid option")    

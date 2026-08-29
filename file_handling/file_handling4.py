



feedback =input("Enter Your Feedback: ")
with open("feedback.txt", "a") as log:
    log.write(feedback + "\n")

print("Tanks! Your Feedback is Saved.")

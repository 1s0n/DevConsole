PyConsole By JasonTheDev

PyConsole Is A Developer Console That Lets Your User Or The Developers To Have A Console Interface For Testing.
This Comes Extreamly Handy When You Want To Execute Functions At Certain Times And Don't Want To Write Too Much Code.

There Will Be A "Command" Class Which Is A Class That Stores A Function/Method That Gets Called When The Command Is Executed And A 
Name Which Is The Name Thats Used To Call The Command In The Console (Note: The Commands Will Be Lowered So Even A Command Like
"eXiT" will be recognised as "exit").

The Console Will Be A Tkinter Window And It Supports Custom GUI Made In Tkinter But the feature is not tested and polished so there
may be bugs. There must be these components on the tkinter window if you decide to use the custom GUI feature:

"CommandEntry" - tkinter.Entry Used For Entering Commands

"CommandList" - tkinter.Listbox Used For Displaying Commands

"SubmitButton" - tkinter.Button Used For Submitting Commands

Note: The Return/Enter button will automatically be binded to execute commands.

Usage Examples (Python Code):


```
from PyConsole.Console import Console, Command

console = Console("Console title", "icon path", "background color code") # Create a new console.   all these parameters are optional

def function(): # The Function That Will Get Activated When A Command Is Executed
	print("A Command Has Been Executed Through PyConsole")
	console.WriteLine("You Just Executed A Command") # Writing A Line To The Console

cmd = Command("name", function) # Created a Command Object Called cmd and giving it a name and a function/method to call

# The Name Of The Command Will Be the text used to call the command

console.RegisterCommand(cmd) # Register The Command That We Just Created, You Could Register As Many As You Want

console.mainloop() # Calls the tkinter.mainloop() function
```


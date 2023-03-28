# Using Chat GPT-4
Edit `TODO_secret.env` to have your secret key, then rename it to `secret.env`.

Do `pip install openai`.

Create a new folder that copies the `example` folder. Name it whatever you'd like to work on (`your_folder`).

Put your prompt into `prompt.txt`. Use curly braces ("{}") to indicate where you'd like other files to be put (just like a Python format string).

Then, add the files you'd like to be put in your prompt into `your_folder/files`.

Then, go to `main.py` and look find the line that says `prompt = file_to_string("files/prompt.txt").format(file_to_string("files/code.txt"), file_to_string("files/my_thoughts.txt"))` Replace the `file_to_string("files/code.txt"), file_to_string("files/my_thoughts.txt")` part with your files that you want to be put in, or delete the `.format` entirely if you just want to do a regular prompt.

Then, you can run `main.py` with `python main.py`. It will save a cost file and all the messages that were sent to the chat.

To reply, create a `files/reply.txt` and paste the `output.txt` file into it. Then, comment in the `# reply = file_to_string("files/reply.txt")` line and `# {"role": "assistant", "content": reply},` line. Then, uncomment the `# prompt2 = file_to_string("files/prompt2.txt")` line as well, and put your next prompt into `files/prompt2.txt` (Just like the first prompt, you can use formatting strings to get other files into the second prompt.)

Now, when, you run `main.py` again, the  model should reply to your most recent comment with the context of all the previous methods.

At current (March 27th, 2023) prices, the default example should cost less than $0.01 to run.
import openai
from os import getenv
import json
from dotenv import load_dotenv # pip install python-dotenv

# Load the secret file
load_dotenv("../secret.env")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
assert OPENAI_API_KEY, "You did not put the OPENAI_API_KEY in the secret.env file. The secret.env file should look like 'OPENAI_API_KEY=sk-...'"
# openai.organization = "YOUR_ORGANIZATION_ID" # optional
PROMPT_PRICE_PER_TOKEN = 0.03 / 1000
COMPLETION_PRICE_PER_TOKEN = 0.06 / 1000
MAX_TOKENS = 1000

gpt3turbo = "gpt-3.5-turbo" # without gpt4 access
gpt4 = "gpt-4"

def file_to_string(filename: str) -> str:
    with open(filename, "r", encoding='utf-8') as f:
        return f.read()

prompt = file_to_string("files/prompt.txt").format(file_to_string("files/code.txt"), file_to_string("files/my_thoughts.txt"))
# reply = file_to_string("files/reply.txt")
# prompt2 = file_to_string("files/prompt2.txt")
# reply2 = file_to_string("files/reply2.txt")
# prompt3 = file_to_string("files/prompt3.txt")
# reply3 = file_to_string("files/reply3.txt")
# prompt4 = file_to_string("files/prompt4.txt")

messages = [
    {"role": "user", "content": prompt},
    # {"role": "assistant", "content": reply},
    # {"role": "user", "content": prompt2},
    # {"role": "assistant", "content": reply2},
    # {"role": "user", "content": prompt3},
    # {"role": "assistant", "content": reply3},
    # {"role": "user", "content": prompt4},
]

with open("messages.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(messages))

for message_index, message in enumerate(messages):
    with open(f"message{message_index}.txt", "w", encoding='utf-8') as f:
        f.write(message["content"])

print("Asking OpenAI to complete the prompt...")
response = openai.ChatCompletion.create(
  model=gpt4,
  max_tokens=MAX_TOKENS,
  messages=messages
)

cost = response.usage.prompt_tokens * PROMPT_PRICE_PER_TOKEN + response.usage.completion_tokens * COMPLETION_PRICE_PER_TOKEN

error = None
message = None
try:
  print(f"Total Cost: ${cost:.6f}")
  print(f"Prompt Cost: ${response.usage.prompt_tokens * PROMPT_PRICE_PER_TOKEN:.6f}")
  print(f"Completion Cost: ${response.usage.completion_tokens * COMPLETION_PRICE_PER_TOKEN:.6f}")

  print(response)
  message = response.choices[0].message.content
  print(message)
except Exception as e:
    print("Something went wrong")
    print(e)
    error = e

with open("cost.txt", "w") as f:
    f.write("$" + str(cost))

with open("response.json", "w") as f:
    f.write(json.dumps(response))

with open("output.txt", "w") as f:
    f.write(response.choices[0].message.content)

if error is not None:
    raise error
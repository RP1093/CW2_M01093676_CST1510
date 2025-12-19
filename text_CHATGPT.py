#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


from openai import OpenAI
client = OpenAI(api_key="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")

prompt = "Hello, how are you?"

completion = client.chat.completions.create(
  model="gpt-5.2",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)






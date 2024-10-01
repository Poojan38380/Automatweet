import asyncio
from asyncio import WindowsSelectorEventLoopPolicy
from g4f.client import Client

# Set the event loop policy to avoid the warning
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

def use_gpt(prompt):
    client = Client()
    # Generate tweet content
    response = client.chat.completions.create(
        #can change to a different model if you want to 
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
    # Get the response content and remove surrounding double quotes if present
    content = response.choices[0].message.content.strip('"')
    return content

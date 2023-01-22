import openai
import gradio as gr

openai.api_key = "------------apikey-------------"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = " Ask any thing"

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1 style="color:Orange;"><center>Sunny Sharma ChatGPT 
    <a style="text-decoration:none;width:100%;font-size:18px;padding:1rem;background-color:orange;color:black;border-radius:5rem;"
     href="https://20sunny.github.io">View Protfolio</a></center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)

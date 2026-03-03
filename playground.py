@app.post("/api/chat", response_model=ChatOut)
def chat(payload: ChatIn):
    instructions = NOVA_INSTRUCTIONS if payload.mode == "nova" else DRAGON_INSTRUCTIONS

    try:
        # Standard completions endpoint
        completion = client.chat.completions.create(
            model="gpt-4o-mini", # Use a valid model name
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": payload.message}
            ]
        )
        
        reply_text = completion.choices[0].message.content
        return ChatOut(reply=reply_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

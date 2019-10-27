@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    resp.message("getting your answer...")

    # Determine the right reply for this message
    if body == None:
        resp.message("Got none!")
    elif body.lower == 'bye':
        resp.message("Goodbye")
    else:
        params = {
            "q" : body,
            "format" : "json"
            }
        r = requests.get("https://api.duckduckgo.com/", params = params)
        data = r.json()
        t = data["AbstractText"]
        if t == "":
            t = "none found"
        resp.message(t)

    return str(resp)

# API Reference

The MinecraftGPT API provides a single endpoint for chat interactions.

## `POST /chat`

This endpoint is used to send a message from a player to the AI and receive a reply.

### Request Body

| Field     | Type   | Required | Description                                                                                             |
| :-------- | :----- | :------- | :------------------------------------------------------------------------------------------------------ |
| `player`  | string | Yes      | The name of the player initiating the chat. Used for player-specific memory.                            |
| `message` | string | Yes      | The message content from the player.                                                                    |
| `model`   | string | No       | The specific AI model to use for this request. If omitted, the default model from `config.yml` is used. |

**Example JSON Body:**
```json
{
  "player": "Steve",
  "message": "What are the ingredients for a cake?",
  "model": "google/gemini-pro"
}
```

### Response Body

The endpoint returns a JSON object with a single field:

| Field   | Type   | Description                        |
| :------ | :----- | :--------------------------------- |
| `reply` | string | The AI's response to the message. |

**Example JSON Response:**
```json
{
  "reply": "To bake a cake in Minecraft, you'll need 3 buckets of milk, 2 sugar, 1 egg, and 3 wheat. Enjoy!"
}
```

### Error Responses

If an error occurs, the `reply` field will contain an error message.

**Example Error:**
```json
{
  "reply": "Error: OPENROUTER_API_KEY not configured in config.yml."
}
```

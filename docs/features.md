# Features

The MinecraftGPT API is designed to be flexible and robust. Here are some of the key features:

## Player Memory
The API remembers the context of recent conversations for each player individually. This allows players to ask follow-up questions and have more natural interactions.

- **Configuration:** The number of conversation turns to remember is set by `max_history_size` in `config.yml`.

## Model Flexibility
You can define a default AI model for all requests and optionally allow clients (like a Minecraft plugin) to override the model on a per-request basis.

- **Configuration:**
    - `default_name`: The model to use if none is specified in the request.
    - `allow_client_override`: Set to `true` to allow clients to send a `model` field in their requests.

## Rate Limiting
To prevent spam and abuse, the API includes a built-in rate limiter. It limits how many requests can be made from a single IP address in a given time period.

- **Configuration:** The `rate_limit` setting in `config.yml` controls this feature (e.g., `"15/minute"`).

## Centralized Configuration
All major settings are managed in the `config.yml` file, making it easy to update the API's behavior without changing any code. This includes:
- API keys
- Model settings (name, temperature)
- System prompts
- Memory and security settings

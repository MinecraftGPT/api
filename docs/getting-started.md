# Getting Started

This guide will walk you through setting up the MinecraftGPT API for the first time.

## 1. Clone the Repository
```bash
git clone https://github.com/MinecraftGPT/minecraft-gpt-api.git
cd minecraft-gpt-api
```

## 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

## 3. Configure the API
The API is configured using the `config.yml` file.

1.  **Create the config file:**
    Rename `config.yml.example` to `config.yml`.

2.  **Set your API Key:**
    Open `config.yml` and replace `"your_openrouter_api_key"` with your actual API key from [OpenRouter.ai](https://openrouter.ai/).

    ```yaml
    api:
      openrouter_api_key: "your_openrouter_api_key"
    ```

3.  **Customize (Optional):**
    Review the other settings in `config.yml` to customize the default model, system prompt, rate limits, and more.

## 4. Run the Server
```bash
uvicorn main:app --reload
```
The API will now be running at `http://127.0.0.1:8000`.

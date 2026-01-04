import configparser

config_path = "./image-describer.ini"
config = configparser.ConfigParser()
config.read(config_path, encoding="utf-8")
if not config.has_section("settings"):
    config.add_section("settings")

def save_config():
    with open(config_path, "w", encoding = "utf-8") as f:
        config.write(f)

def save_api_key(key):
    config["settings"]["GROK_API_KEY"] = key
    with open(config_path, "w", encoding="utf-8") as f:
        config.write(f)

def get_api_key():
    return config.get("settings", "GROK_API_KEY", fallback="")

def get_selected_model():
    return config.get("settings", "GROK_MODEL", fallback="meta-llama/llama-4-maverick-17b-128e-instruct")

def save_model(model):
    config["settings"]["GROK_MODEL"] = model
    with open(config_path, "w", encoding="utf-8") as f:
        config.write(f)

def get_instructions():
    return config.get("settings", "GROK_INSTRUCTIONS", fallback="Опиши это изображение подробно")

def save_instructions(instructions):
    config["settings"]["GROK_INSTRUCTIONS"] = instructions
    save_config()
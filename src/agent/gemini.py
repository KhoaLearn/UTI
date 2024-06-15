import os
from typing import Optional, Any, Dict

try:
    import google.generativeai as genai
except ImportError:
    raise ValueError(
        "Gemini is not installed. Please install it with "
        "`pip install 'google-generativeai'`."
    )
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from pydantic import Field, PrivateAttr

from src.agent.constants import DEFAULT_CANDIDATE_COUNT, DEFAULT_NUM_OUTPUTS, DEFAULT_TEMPERATURE, DEFAULT_TOP_K, DEFAULT_TOP_P

GEMINI_MODELS = {
            "gemini-1.0-pro": "models/gemini-1.0-pro", 
            "gemini-1.0-pro-001": "models/gemini-1.0-pro-001", 
            "gemini-1.0-pro-latest": "models/gemini-1.0-pro-latest", 
            "gemini-1.5-pro": "models/gemini-1.5-pro", 
            "gemini-1.5-pro-001": "models/gemini-1.5-pro-001", 
            "gemini-1.5-pro-latest": "models/gemini-1.5-pro-latest", 
            "gemini-1.5-flash": "models/gemini-1.5-flash", 
            "gemini-1.5-flash-001": "models/gemini-1.5-flash-001", 
            "gemini-1.5-flash-latest": "models/gemini-1.5-flash-latest", 
            "gemini-pro": "models/gemini-pro", 
        }

_generation_config = {
    "candidate_count": DEFAULT_CANDIDATE_COUNT, 
    "max_output_tokens": DEFAULT_NUM_OUTPUTS, 
    "temperature": DEFAULT_TEMPERATURE, 
    "top_k": DEFAULT_TOP_K, 
    "top_p": DEFAULT_TOP_P, 
}

# https://ai.google.dev/api/python/google/generativeai/protos/HarmCategory
_safety_setting = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
}

class GeminiAgent:
    model_name: str = Field(
        default=GEMINI_MODELS["gemini-1.5-flash"], description="The Gemini model to use."
    )
    _model: "genai.GenerativeModel" = PrivateAttr()
    _model_meta: "genai.types.Model" = PrivateAttr()
    

    def __init__(self, 
                api_key: Optional[str] = None,
                model_name: Optional[str] = GEMINI_MODELS["gemini-1.5-flash"],
                generation_config: Optional["genai.types.GenerationConfigDict"] = _generation_config,
                safety_settings: "genai.types.SafetySettingOptions" = _safety_setting,
                system_prompt: str = None,
                 ): 

        config_params: Dict[str, Any] = {
            "api_key": api_key or os.getenv("GOOGLE_API_KEY"),
        }
        genai.configure(**config_params)

        self._model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
            safety_settings=safety_settings,
        )
        self._model_meta = genai.get_model(model_name)

        if system_prompt: 
            self.system_prompt = {"role": "system", 
                                  "parts": [system_prompt]}
            
        supported_methods = self._model_meta.supported_generation_methods
        if "generateContent" not in supported_methods:
            raise ValueError(
                f"Model {model_name} does not support content generation, only "
                f"{supported_methods}."
            )

    def list_model(self) -> dict: 
        return GEMINI_MODELS
    
    def get_model(self): 
        return self._model_meta
    
    def chat(self, prompt:str, image): 
        messages = []
        user_msg = {
            "role": "user", 
            "parts": [prompt, image]
        }
        if hasattr(self, "system_prompt"): 
            messages.append(self.system_prompt)
        else: 
            messages.append(user_msg)
        try: 
            response = self._model.generate_content(messages)
            return response
        except: 
            raise Exception("Failed to send request to Gemini")
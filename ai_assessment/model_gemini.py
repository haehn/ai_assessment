from google import genai

API_KEY = os.getenv("GOOGLE_API_KEY")

class ModelGemini3ProPreview(Model):

  def __init__(self):
    super().__init__("gemini-3-pro-preview")

    self.client = genai.Client(api_key=API_KEY)

  def generate(self, essay):

    response = self.client.models.generate_content(
        model=self.name, 
        contents=essay.prompt
    )

    return response.text

  def tune(self, essay, rubric):
    pass

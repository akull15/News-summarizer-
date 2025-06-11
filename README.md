📰 News Summarizer Web App
Generate concise summaries from long-form news articles using state-of-the-art NLP models.
Built with Hugging Face Transformers and Gradio for an intuitive web interface.

Dataset
Pre-trained Model: facebook/bart-large-cnn

Summary Generation Task

How It Works
1. Text Preprocessing
Raw news articles are tokenized using the pre-trained BART tokenizer.

Articles longer than the model’s max token length are truncated appropriately.

Cleaned and prepared for the model input.

2. Model Architecture
Encoder-Decoder Architecture (BART)

Pre-trained on CNN/DailyMail dataset for summarization tasks.

Pipeline:

Article → Encoder → Compressed Representation → Decoder → Summary

3. Web Interface (Gradio)
User pastes or uploads a news article.

Press Summarize → Returns a short, accurate summary.

Works on CPU or GPU environments.

Requirements:

Install the required Python libraries:

pip install -r requirements.txt

Contents of requirements.txt:

numpy

pandas

transformers==4.41.1

torch>=2.0.0

sentencepiece

gradio==4.15.0

scikit-learn

requests


Training :

No custom training required for this project as it uses pre-trained weights.

Fine-tuning can be added later if needed for custom datasets.

Real-time Usage:

Loads the pre-trained BART summarizer on app launch.

Accepts long news texts as input.

Summarized output shown on the Gradio interface in real-time.


Can be deployed on Hugging Face Spaces or hosted locally.

Run locally:

python news_summarizer_gradio.py

Or deploy on Hugging Face Spaces:

Create new Space → Select Gradio template.

Upload project files (including this README, requirements.txt, and .py file).

Click Deploy.

Future Enhancements

🔖 Integrate news recommendation system using embeddings or content similarity.

🌐 Add web scraping functionality to fetch live news.

🎨 Improve UI: dark mode, layout improvements.

🧠 Fine-tune summarization model on custom datasets.



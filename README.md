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

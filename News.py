import tkinter as tk
from tkinter import scrolledtext
import requests

class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News App")

        self.create_widgets()

    def create_widgets(self):
        # Create a scrolled text widget to display news
        self.news_display = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.news_display.grid(row=0, column=0, padx=10, pady=10)

        # Button to fetch and display news
        fetch_button = tk.Button(self.root, text="Fetch News", command=self.fetch_news)
        fetch_button.grid(row=1, column=0, pady=5)

    def fetch_news(self):
        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = 'YOUR_API_KEY'
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'

        try:
            # Fetch news data
            response = requests.get(url)
            data = response.json()

            # Display news in the scrolled text widget
            articles = data.get('articles', [])
            news_text = ""
            for article in articles:
                news_text += f"{article['title']}\n\n{article['description']}\n\n{'='*50}\n"

            self.news_display.delete(1.0, tk.END)  # Clear existing text
            self.news_display.insert(tk.END, news_text)
        except Exception as e:
            print(f"Error fetching news: {e}")

# Create the main application window
root = tk.Tk()
app = NewsApp(root)

# Run the application
root.mainloop()

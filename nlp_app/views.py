from django.shortcuts import render
from .forms import MessageForm
import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create your views here.
def nlp(request):
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            sia = SentimentIntensityAnalyzer()
            msg = form.cleaned_data["msg"]
            pre = sia.polarity_scores(msg)
            print(pre)
            context = {
                "form":form,
                "neg": pre['neg'],
                "neu": pre['neu'],
                "pos":pre['pos'],
                "msg":msg
            }
            return render(request, "nlp.html", context)
    else:
        form = MessageForm()
    return render(request, "nlp.html", {"form": form})
from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat, reflections
import re

# تحميل الموارد اللازمة
nltk.download('punkt')
nltk.download('wordnet')

app = Flask(__name__)

# دالة لتطبيع النص العربي
def normalize_arabic(text):
    text = re.sub(r'[^\w\s]', '', text)  # إزالة علامات الترقيم
    text = re.sub(r'[ًٌٍَُِّْ]', '', text)  # إزالة التشكيل
    text = text.strip()
    return text

# إعداد الأنماط والردود (Regex مرن)
patterns = [
    (r'(?i)hi|hello|hey', ['مرحباء بك?']),
    (r'(?i)what is your name[\?؟]?', ['I am a chatbot NSR created using NLTK.']),
    (r'(?i)how are you[\?؟]?', ['I am fine, thank you!']),
    (r'(?i)what can you do[\?؟]?', ['I can chat with you and answer simple questions.']),
    
    (r'(من انت)', ['طالب في كلية الحاسوب']),
    (r'(ما ?اسمك)', ['أنا روبوت دردشة اسمي NSR.']),
    (r'(كيف حالك)', ['أنا بخير، شكراً لسؤالك!']),
    (r'(ماذا يمكنك ان تفعل)', ['يمكنني الدردشة معك والإجابة على أسئلة بسيطة.']),
    (r'(كم عمرك)', ['ليس لدي عمر حقيقي، فأنا برنامج حاسوبي.']),
    (r'(اين تعيش)', ['أعيش في عالم البرمجة والذكاء الاصطناعي.']),
    (r'(ما هو الذكاء الاصطناعي)', ['الذكاء الاصطناعي هو مجال في علوم الحاسوب يهدف إلى إنشاء أنظمة قادرة على التفكير والتعلم.']),
    
    (r'(.*)', ['لم أفهم قصدك، هل يمكنك التوضيح؟']),
]

# إنشاء البوت باستخدام الأنماط والردود
chatbot = Chat(patterns, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    normalized_input = normalize_arabic(user_input)
    response = chatbot.respond(normalized_input)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

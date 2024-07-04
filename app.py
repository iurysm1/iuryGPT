from flask import Flask, request, redirect, flash, jsonify
from flask.helpers import url_for
from flask import Flask, render_template
import json
from config import db
from config import llm, chatPromptTemplate, PromptTemplate, ConversationBufferMemory, ConversationChain
app = Flask(__name__)

DB_NAME = "database.db"

from models import Conversa, MensagensConversa


memory = ConversationBufferMemory()

convarsation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True,
)



app.config['SECRET_KEY'] = 'IFSC@TUB'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)




with app.app_context():
    db.create_all()
### Rotas ###

@app.route("/", methods=['GET', 'POST'])
def home():
    conversa = db.session.get(Conversa, 1)
    list_messages=conversa.mensagens
    return render_template("home.html", list_messages=list_messages)


def send_message(input, conversa_id):
    conversa = db.session.get(Conversa, conversa_id)
    list_messages=conversa.mensagens

    if list_messages != []:
        for conversa in list_messages:
            memory.save_context({"input": conversa.input}, {"output": conversa.output})

    return convarsation.predict(input=input)



def mensagem(input, output, conversa_id):
    db.session.add(MensagensConversa(input=input,output=output, conversa_id=conversa_id))
    db.session.commit()
    return 


@app.route("/send", methods=['POST'])
def send():
    conversa = db.session.get(Conversa, 1)
    objectsRequest = json.loads(request.data)
    input=objectsRequest['messageInput']
    output=send_message(input, conversa.id)
    mensagem(input, output, conversa_id=conversa.id)
    return jsonify({'input': input, 'output': output})

@app.route("/delete_messages", methods=["POST"])
def delete_messages():
    conversa = db.session.get(Conversa, 1)
    list_messages=conversa.mensagens
    for msg in list_messages:
        db.session.delete(msg)
    db.session.commit()
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)
    
    

